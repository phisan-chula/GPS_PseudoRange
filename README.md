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

Input pseudoranges and  broadcasted  satellite clock bias (SVClkErr_m):<br>

|    |   PRN |          ECEF_X |          ECEF_Y |          ECEF_Z |   SVClkErr_m |
|---:|------:|----------------:|----------------:|----------------:|-------------:|
|  0 |    12 |  -9,924,909.896 | -22,418,412.217 | -10,238,600.462 | -107,674.658 |
|  1 |     2 |  19,519,446.654 | -12,864,169.870 |  12,106,498.214 |   59,947.699 |
|  2 |    26 |   9,518,973.908 | -24,465,469.002 |    -347,289.566 |   74,176.449 |
|  3 |    15 |   6,420,995.137 | -25,601,178.700 |  -2,907,089.329 |  -32,117.066 |
|  4 |    29 |  -8,265,550.815 | -16,497,554.935 |  19,234,406.500 |  -12,988.808 |
|  5 |    21 | -22,299,549.612 |  -6,458,590.524 |  13,615,554.839 |   19,513.491 |
|  6 |    30 | -18,044,425.181 | -19,566,072.431 |    -289,953.964 |   22,534.799 |

===================== Result from LSQ =================<br>
Reduce chi-square : 12.2 meter.<br>
X:    506,077.0 meter  +/-2.4<br>
Y: -4,882,270.9 meter  +/-7.0<br>
Z:  4,059,621.3 meter  +/-4.2<br>
dt:           250.7 nanosec  +/-151.5<br>
dt:             7.5 m  +/-4.5<br>

==================PR Residuals =================<br>
|    |   PRN |        Range_m |   Resid_m |
|---:|------:|---------------:|----------:|
|  0 |    12 | 25,022,759.323 |    -3.700 |
|  1 |     2 | 22,075,351.532 |     0.532 |
|  2 |    26 | 21,929,350.580 |    -1.161 |
|  3 |    15 | 22,677,087.545 |     2.306 |
|  4 |    29 | 21,039,894.608 |    -1.626 |
|  5 |    21 | 24,757,444.127 |    -0.012 |
|  6 |    30 | 24,032,696.422 |     3.661 |


