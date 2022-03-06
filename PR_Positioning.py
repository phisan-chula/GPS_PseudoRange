#
PROG='''
 GNSS_PseudoRange :  determine a receiver 3D position from pseudorange 
                     measurement with psedorange with receiver clock-bias
                     using least-square adjusment
 Author : Phisan Santitamtnont, Faculty of Engineering, Chulalongkorn University
          email: phisan.chula@gmail.com
 Reference: Raquet John, Workshop on GNSS Data Application to Low Latitude
            Ionospheric Research, 6-17 May 2013, The Abdus Salam International 
            for Theoretical Physics, OH 45433, USA
'''
#
#
import pandas as pd
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
from lmfit import Parameters, fit_report, minimize

#######################################################################
class GPS_PR:
    UNKNOWN = ['X','Y','Z','dt']
    EarthRad = 6_371_000  # m
    v =	299_792_458 # meter per second
    def __init__(self):
        Meas = np.array( [  12, 25_022_759.323,
                             2, 22_075_351.532,
                            26, 21_929_350.580,
                            15, 22_677_087.545,
                            29, 21_039_894.608,
                            21, 24_757_444.127,
                            30, 24_032_696.422 ] )
        self.dfMeas = pd.DataFrame( Meas.reshape(-1,2) , columns=['PRN', 'Range_m'] )
        self.dfMeas['PRN'] = self.dfMeas['PRN'].map( '{:.0f}'.format )
        #############################################################
        SV_ECEF='''
        12 -9924909.896 -22418412.217 -10238600.462 -0.000359164
        2 19519446.654 -12864169.870 12106498.214 0.000199964
        26 9518973.908 -24465469.002 -347289.566 0.000247426
        15 6420995.137 -25601178.700 -2907089.329 -0.000107131
        29 -8265550.815 -16497554.935 19234406.500 -0.000043326
        21 -22299549.612 -6458590.524 13615554.839 0.000065090
        30 -18044425.181 -19566072.431 -289953.964 0.000075168
        '''
        self.dfSV = pd.read_csv( StringIO(SV_ECEF),delim_whitespace=True, header=None,
                            names=['PRN','ECEF_X','ECEF_Y','ECEF_Z', 'SVClkErr_s'] )
        self.dfSV['PRN'] = self.dfMeas['PRN'].map( '{:s}'.format )
        self.dfSV['SVClkErr_m'] = self.v* self.dfSV['SVClkErr_s']

    def Plot3D(self, RCV_ECEF ):
        plt.rcParams["figure.figsize"] = [20.00, 20.00]
        plt.rcParams["figure.autolayout"] = True
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        R = self.EarthRad
        u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
        x = R*np.cos(u) * np.sin(v)
        y = R*np.sin(u) * np.sin(v)
        z = R*np.cos(v)
        for iaxis,ch_axis in enumerate(self.UNKNOWN[:3]):
            z6 = np.zeros(6); z6[3+iaxis]=1.5*R
            ax.quiver(*z6.tolist(),arrow_length_ratio=0.1,color='k')
            z3 = np.zeros(3); z3[iaxis]=1.5*R
            ax.text( *z3.tolist() ,ch_axis, fontsize=20 )
        ax.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r, alpha=0.5)
        for i,row in self.dfSV.iterrows():
            X,Y,Z = RCV_ECEF
            ax.plot( [row.ECEF_X,X], [row.ECEF_Y,Y] ,[row.ECEF_Z,Z] )
            ax.scatter( row.ECEF_X,row.ECEF_Y,row.ECEF_Z, s=300, alpha=0.5  ) 
            ax.text( row.ECEF_X,row.ECEF_Y,row.ECEF_Z, f'SV-{row.PRN}', fontsize=15  ) 
        ax.text( X,Y,Z, 'RCV' , fontsize=20 ) 
        plt.show()

def residual( pars, gps_pr ):
    resid = list()
    for i,row in gps_pr.dfMeas.iterrows():
        prn = gps_pr.dfSV[gps_pr.dfSV.PRN==row.PRN].iloc[0]
        rcv = np.array( [pars['X'].value, pars['Y'].value, pars['Z'].value] )
        sat = np.array( [ prn.ECEF_X, prn.ECEF_Y, prn.ECEF_Z ] )
        dat_rng = row.Range_m + prn.SVClkErr_m # broadcasted SVClkErr
        mod_rng = np.linalg.norm( rcv-sat ) + gps_pr.v*pars['dt'].value 
        #import pdb; pdb.set_trace()
        resid.append( [mod_rng-dat_rng] )   #  model-data
    return resid

#############################################################
import argparse
parser = argparse.ArgumentParser(description=PROG)
parser.add_argument('-p','--plot', action='store_true',
        help='plot pseudorange positioning scenario') 
args = parser.parse_args()

gps_pr = GPS_PR()
print( gps_pr.dfSV[['PRN', 'ECEF_X', 'ECEF_Y', 'ECEF_Z', 'SVClkErr_m' ]].\
                     to_markdown(floatfmt=",.3f") )
X = [ 506_000, -4_882_000, 4_109_000, 0.0 ]  #  initial RCV ECEF + Rcv.Clk.Bias

# perform least-square adjustment computation via Levenberg-Marquadt algorithm
Unk = Parameters()
for i,unk in enumerate( gps_pr.UNKNOWN ):
    Unk.add( unk, value=X[i] ) 
result = minimize( residual, Unk,  args=(gps_pr,) )  
print( fit_report ( result ) )

print('=============== Result from LSQ ===============')
print( 'Reduce chi-square : {:,.1f} meter.'.format(result.redchi) )
RCV_ECEF = list() ; TAB=list()
for unk in result.var_names:
    val = result.params[unk].value
    std = result.params[unk].stderr
    if unk=='dt':
        val_nano = val*10E9  # nano sec
        std_nano = std*10E9  # nano sec
        TAB.append( [f'{unk:4s}', f'{val_nano:18.2f} ns', f'+/-{std_nano:3.0f} ns'] )
        TAB.append( [f'{unk:4s}', f'{gps_pr.v*val:15,.1f} m', f'+/-{gps_pr.v*std:3.1f} m'] )
    else:
        RCV_ECEF.append( val )
        TAB.append( [f'{unk:4s}', f'{val:12,.1f} m',  f'+/-{std:3.1f} m'] )
print( pd.DataFrame(TAB,columns=['Parameter','Value','Std']).to_markdown(stralign='right') )
print('==================PR Residuals =================')
gps_pr.dfMeas['Resid_m'] = result.residual
print( gps_pr.dfMeas.to_markdown(floatfmt=",.3f") )
if args.plot:
    gps_pr.Plot3D( RCV_ECEF )
#import pdb; pdb.set_trace()
