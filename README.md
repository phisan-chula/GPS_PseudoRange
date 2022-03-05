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

|    |   PRN |       ECEF_X |       ECEF_Y |            ECEF_Z |   SVClkErr_m |
|---:|------:|-------------:|-------------:|------------------:|-------------:|
|  0 |    12 | -9.92491e+06 | -2.24184e+07 |      -1.02386e+07 |    -107675   |
|  1 |     2 |  1.95194e+07 | -1.28642e+07 |       1.21065e+07 |      59947.7 |
|  2 |    26 |  9.51897e+06 | -2.44655e+07 | -347290           |      74176.4 |
|  3 |    15 |  6.421e+06   | -2.56012e+07 |      -2.90709e+06 |     -32117.1 |
|  4 |    29 | -8.26555e+06 | -1.64976e+07 |       1.92344e+07 |     -12988.8 |
|  5 |    21 | -2.22995e+07 | -6.45859e+06 |       1.36156e+07 |      19513.5 |
|  6 |    30 | -1.80444e+07 | -1.95661e+07 | -289954           |      22534.8 |

===================== Result from LSQ =================
Reduce chi-square : 12.2 meter.
X:    506,077.0 meter  +/-2.4
Y: -4,882,270.9 meter  +/-7.0
Z:  4,059,621.3 meter  +/-4.2
dt:           250.7 nanosec  +/-151.5
dt:             7.5 m  +/-4.5

|    |   PRN |     Range_m |      Resid |
|---:|------:|------------:|-----------:|
|  0 |    12 | 2.50228e+07 | -3.70034   |
|  1 |     2 | 2.20754e+07 |  0.532437  |
|  2 |    26 | 2.19294e+07 | -1.16053   |
|  3 |    15 | 2.26771e+07 |  2.30593   |
|  4 |    29 | 2.10399e+07 | -1.62615   |
|  5 |    21 | 2.47574e+07 | -0.0120553 |
|  6 |    30 | 2.40327e+07 |  3.66062   |

