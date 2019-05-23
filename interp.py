#!/usr/bin/env python

# Interpolate between artificial contours in a CSV
import csv
import sys
import math

csv_file = sys.argv[1]
intervals = float(sys.argv[2])

def interpolate(x1, y1, x2, y2, t):
    x = x1 + (x2-x1) * t
    y = y1 + (y2-y1) * t
    #print(x,y)
    return (x,y)

def interval_to_fraction(x1,y1,x2,y2,interval):
    dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    num_points = math.floor(dist/interval)-1
    fraction = 1.0/num_points
    #print(num_points, fraction)
    return num_points, fraction

last_x = False
last_y = False
last_z = False

newcsv = "Easting,Northing,Elevation\n"

with open(csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x=float(row['Easting'])
        y=float(row['Northing'])
        z=float(row['Elevation'])

        if not last_z or (last_z!=z):
            last_x, last_y, last_z = x,y,z
            newcsv+=','.join([str(x),str(y),str(z)])+"\n"
            next
        else:
            num_points, fraction = interval_to_fraction(last_x,last_y,x,y,intervals)
            for i in range(1, num_points):
                (tx,ty)=interpolate(last_x,last_y,x,y, fraction*i)
                newcsv+=','.join([str(tx),str(ty),str(z)])+"\n"
            newcsv+=','.join([str(x),str(y),str(z)])+"\n"
            last_x, last_y, last_z = x,y,z

print(newcsv)
