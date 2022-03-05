# GPS_PseudoRange
 GNSS_PseudoRange :  determine a receiver 3D position from pseudorange
                     measurement with psedorange with receiver clock-bias
                     using least-square adjusment
 Author : Phisan Santitamtnont, Faculty of Engineering, Chulalongkorn University
          email: phisan.chula@gmail.com
 Reference: Raquet John, Workshop on GNSS Data Application to Low Latitude
            Ionospheric Research, 6-17 May 2013, The Abdus Salam International 
            for Theoretical Physics, OH 45433, USA

![alt text](https://github.com/phisan-chula/GPS_PseudoRange/blob/main/GPS_PR_Positioning.png)

Result:

 PRN        ECEF_X        ECEF_Y        ECEF_Z     SVClkErr_m
0  12 -9.924910e+06 -2.241841e+07 -1.023860e+07 -107674.658385
1   2  1.951945e+07 -1.286417e+07  1.210650e+07   59947.699072
2  26  9.518974e+06 -2.446547e+07 -3.472896e+05   74176.448713
3  15  6.420995e+06 -2.560118e+07 -2.907089e+06  -32117.065818
4  29 -8.265551e+06 -1.649755e+07  1.923441e+07  -12988.808035
5  21 -2.229955e+07 -6.458591e+06  1.361555e+07   19513.491091
6  30 -1.804443e+07 -1.956607e+07 -2.899540e+05   22534.799483

===================== Result from LSQ =================
Reduce chi-square : 12.2 meter.
X:    506,077.0 meter  +/-2.4
Y: -4,882,270.9 meter  +/-7.0
Z:  4,059,621.3 meter  +/-4.2
dt:           250.7 nanosec  +/-151.5
dt:             7.5 m  +/-4.5
  PRN        Range_m  Resid
0  12 25,022,759.3 m -3.7 m
1   2 22,075,351.5 m  0.5 m
2  26 21,929,350.6 m -1.2 m
3  15 22,677,087.5 m  2.3 m
4  29 21,039,894.6 m -1.6 m
5  21 24,757,444.1 m -0.0 m
6  30 24,032,696.4 m  3.7 m
