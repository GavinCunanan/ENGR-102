# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Gavin Cunanan
# Section: 417/517
# Assignment: LAB 2.10 More Linear Interpolation
# Date: 3 September 2025
#

import math

#variable positions
x1 = 8
x2 = -5
y1 = 6
y2 = 30
z1 = 7
z2 = 9
t1 = 12
t2 = 85


#slope formula for each of the variables
slope_x = (x2 - x1)/(t2 - t1)
slope_y = (y2 - y1)/(t2 - t1)
slope_z = (z2 - z1)/(t2 - t1)

#linear interpolation formula including the slopes for each variable 30
x = slope_x * (30 - t1) + x1
y = slope_y * (30 - t1) + y1
z = slope_z * (30 - t1) + z1

#output on the console
print("At time 30.0 seconds: ")
print ("x1 =", x, "m")
print ("y1 =", y, "m")
print ("z1 =", z, "m")

print("-----------------------")

#linear interpolation formula including the slopes for each variable 37.5
x = slope_x * (37.5 - t1) + x1
y = slope_y * (37.5 - t1) + y1
z = slope_z * (37.5 - t1) + z1

print("At time 37.5 seconds: ")
print ("x2 =", x, "m")
print ("y2 =", y, "m")
print ("z2 =", z, "m")

print("-----------------------")

#linear interpolation formula including the slopes for each variable 45.0
x = slope_x * (45 - t1) + x1
y = slope_y * (45 - t1) + y1
z = slope_z * (45 - t1) + z1

print("At time 45.0 seconds: ")
print ("x3 =", x, "m")
print ("y3 =", y, "m")
print ("z3 =", z, "m")

print("-----------------------")

#linear interpolation formula including the slopes for each variable 52.5
x = slope_x * (52.5 - t1) + x1
y = slope_y * (52.5 - t1) + y1
z = slope_z * (52.5 - t1) + z1

print("At time 52.5 seconds: ")
print ("x4 =", x, "m")
print ("y4 =", y, "m")
print ("z4 =", z, "m")

print("-----------------------")

#linear interpolation formula including the slopes for each variable 52.5
x = slope_x * (60 - t1) + x1
y = slope_y * (60 - t1) + y1
z = slope_z * (60 - t1) + z1

print("At time 60.0 seconds: ")
print ("x5 =", x, "m")
print ("y5 =", y, "m")
print ("z5 =", z, "m")