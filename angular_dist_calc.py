import math as m
import sys

input_1 = input("Enter RA of first target (deg): ")
input_2 = input("Enter Dec of first target (deg): ")
input_3 = input("Enter RA of second target (deg): ")
input_4 = input("Enter Dec of second target (deg): ")

ra_1 = m.radians(float(input_1))
dec_1 = m.radians(float(input_2))
ra_2 = m.radians(float(input_3))
dec_2 = m.radians(float(input_4))

if(ra_2 > ra_1):
    b = ra_2 - ra_1
else:
    b= ra_1 - ra_2

if(dec_2 > dec_1):
    c = dec_2 - dec_1
else:
    c = dec_1 - dec_2
    
a = m.acos(m.cos(b)*m.cos(c))

print(m.degrees(a))
