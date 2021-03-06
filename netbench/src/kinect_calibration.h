/*
Netbench: program for commmunication with the Intel Atom and Microsoft Kinect onboard the quadrotor.  This program receives data from the Intel Atom, decompresses it, and publishes to predefined topics in the ROS system.

Author: Paul Gurniak (pgurniak@gmail.com)

Date created: March 16, 2012

Note that all files for this project can be found in our Git repository:
https://github.com/mlab/HAWK-basestation

*/

// Parameters taken from Nicolas Burrus's homepage for calibration of the Microsoft Kinect

// Color
#define fx_rgb 5.2921508098293293e+02
#define fy_rgb 5.2556393630057437e+02
#define cx_rgb 3.2894272028759258e+02
#define cy_rgb 2.6748068171871557e+02
#define k1_rgb 2.6451622333009589e-01
#define k2_rgb -8.3990749424620825e-01
#define p1_rgb -1.9922302173693159e-03
#define p2_rgb 1.4371995932897616e-03
#define k3_rgb 9.1192465078713847e-01

// Depth
#define fx_d 5.9421434211923247e+02
#define fy_d 5.9104053696870778e+02
#define cx_d 3.3930780975300314e+02
#define cy_d 2.4273913761751615e+02
#define k1_d -2.6386489753128833e-01
#define k2_d 9.9966832163729757e-01
#define p1_d -7.6275862143610667e-04
#define p2_d 5.0350940090814270e-03
#define k3_d -1.3053628089976321e+00


// Identity transform
float rotate[9] = {
  1.0, 0, 0, 0, 1.0, 0, 0, 0, 1.0};
/*
#define TRAN_X 0.0
#define TRAN_Y 0.0
#define TRAN_Z 0.0
*/
/*
float rotate[9] = {
  9.9984628826577793e-01, 1.2635359098409581e-03,
  -1.7487233004436643e-02, -1.4779096108364480e-03,
  9.9992385683542895e-01, -1.2251380107679535e-02,
  1.7470421412464927e-02, 1.2275341476520762e-02,
  9.9977202419716948e-01};
*/
float tran[3] = {
  1.9985242312092553e-02, -7.4423738761617583e-04, -1.0916736334336222e-02 };
