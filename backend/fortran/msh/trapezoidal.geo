// Template mesh geometry file for a rib waveguide.

d = 1; // grating period
dy= 0.5;

slab_w = 0.72;
slab_h = 0.13;
rib_w= 0.27;
rib_h= 0.13;

lc = 0; // background and unitcell edge
lc2 = lc/1; // rib
lc3 = lc/1; // slab

hy = dy/2 + slab_h; // 

Point(1) = {0, 0, 0, lc};
Point(2) = {0, -dy, 0, lc};
Point(3) = {d, -dy, 0, lc};
Point(4) = {d, 0, 0,lc};

// Slab
Point(5) = {d/2-slab_w/2, -hy+slab_h, 0, lc3};
Point(6) = {d/2+slab_w/2, -hy+slab_h, 0, lc3};
Point(13) = {d/2-slab_w/2, -hy, 0, lc3};
Point(14) = {d/2+slab_w/2, -hy, 0, lc3};

// Rib
Point(7) = {d/2-rib_w/2, -hy+slab_h, 0, lc2};
Point(8) = {d/2+rib_w/2, -hy+slab_h, 0, lc2};
Point(9) = {d/2-rib_w/2, -hy+slab_h+rib_h, 0, lc2};
Point(10) = {d/2+rib_w/2, -hy+slab_h+rib_h, 0, lc2};

Point(11) = {0, -hy+slab_h, 0, lc};
Point(12) = {d, -hy+slab_h, 0, lc};
Point(15) = {d/2+rib_w/2, 0, 0, lc};
Point(16) = {d/2-rib_w/2, 0, 0, lc};
Point(17) = {d/2+rib_w/2, -dy, 0, lc};
Point(18) = {d/2-rib_w/2, -dy, 0, lc};

Line(5) = {13, 5};
Line(6) = {5, 9};
Line(7) = {9, 10};
Line(8) = {10, 6};
Line(9) = {6, 14};
Line(10) = {14, 8};
Line(11) = {8, 7};
Line(12) = {7, 13};
Line(13) = {13, 14};
Line(14) = {1, 11};
Line(15) = {11, 2};
Line(16) = {4, 12};
Line(17) = {12, 3};
Line Loop(18) = {14, 15, 2, -17, -16, 4};
Line(19) = {11, 5};
Line(20) = {6, 12};
Line Loop(25) = {5, 6, 7, 8, 9, 10, 11, 12};
Plane Surface(26) = {25};
Line Loop(27) = {12, 13, -10, -11};
Plane Surface(28) = {27};
Line(32) = {1, 16};
Line(33) = {16, 9};
Line(34) = {10, 15};
Line(35) = {15, 16};
Line(36) = {15, 4};
Line Loop(37) = {6, -33, -32, 14, 19};
Plane Surface(38) = {37};
Line Loop(39) = {7, 34, 35, 33};
Plane Surface(40) = {39};
Line Loop(41) = {34, 36, 16, -20, -8};
Plane Surface(42) = {41};
Line(44) = {2, 18};
Line(45) = {18, 17};
Line(46) = {17, 3};
Line Loop(48) = {19, -5, 13, -9, 20, 17, -46, -45, -44, -15};
Plane Surface(49) = {48};


Physical Line(29) = {14, 15};
Physical Line(31) = {17, 16};
Physical Line(43) = {32, 35, 36};
Physical Line(47) = {44, 45, 46};

Physical Surface(1) = {38, 40, 42, 49};
Physical Surface(2) = {26};
Physical Surface(3) = {28};
