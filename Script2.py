"""
Final Project Assignment 2
Team 6 Baldwin, Eli; Chen, Zihan
Time:
Date: 10/05/2019
IDCE302
Description: This code calculates the volume of rain water runoff from a place. The user inputs the shape of the place for which they want to calculate the runoff.
Then the user is prompted to enter the units of the input and the units they would like for the ouptut. The user is then prompted to enter a series of measurements based on the shape they input earlier.
The code then calculates and returns the volume of runoff.
"""

#import necessary modules
import math
import sys

#INPUT THE PARAMETERS
#the shape of the place
print('please choose the shape of the base(triangle/square/circle):')
x=raw_input()
#if the input is wrong prompt the user to change the input
while x!='circle' and x != 'triangle' and x!= 'square':
  print('You have entered an invalid word, please try again, this is case sensitive')
  x=raw_input()

#the units of the shape
print('please choose the unit(inch/foot/meter) of input:')
y=raw_input()
while y!='inch' and y!='foot' and y!='meter':
    print('You have entered an invalid word, please try again, this is case sensitive')
    y=raw_input()

#the units of the output
print('please choose the unit(cubic feet/gallons/cubic meters) of output:')
z=raw_input()
while z!='cubic feet' and z!='gallons' and z!='cubic meters':
    print('You have entered an invalid word, please try again, this is case sensitive')
    z=raw_input()
    

#DEFINE THE CALCULATION OF AREA AND VOLUME FOR DIFFERENT SHAPES. v is volume
def triangle(a,b,c,h):
    #a,b,c are sides of the triangle. h is the height of teh triangular prism.
    a = float(a)
    b = float(b)
    c = float(c)
    h = float(h)
    temp = math.sqrt(-a**4+2*(a*b)**2+2*(a*c)**2-b**4+2*(b*c)**2-c**4)
    v = (h/4)*temp
    return v

def square(a,b,h):
    #a and b are sides h is height
    area=float(a)*float(b)
    v=area*float(h)
    return v

def circle(r,h):
    #r is radius, h is height
    area=float(r)**2*math.pi
    v=area*float(h)
    return v

#DEFINE UNIT CONVERSION FOR EACH POSSIBLE COMBINATION OF UNITS
def unitchange(volume_raw):
    if y=='foot' and z=='cubic feet':
       #no conversion necessary
        volume_change= volume_raw
        return volume_change
    elif y=='inch' and z=='cubic feet':
        #conversion necessary
        volume_change = volume_raw*0.0005787
        return volume_change
    elif y=='meter' and z=='cubic feet':
        volume_change = volume_raw*35.31467
        return volume_change
    elif y=='inch' and z=='gallons':
        volume_change = volume_raw*0.004329
        return volume_change
    elif y=='foot' and z=='gallons':
        volume_change = volume_raw*7.4805
        return volume_change
    elif y=='meter' and z=='gallons':
        volume_change = volume_raw*264.17
        return volume_change
    elif y=='meter' and z=='cubic meters':
        volume_change = volume_raw
        return volume_change
    elif y=='inch' and z=='cubic meters':
        volume_change = volume_raw*0.000016387
        return volume_change
    elif y=='foot' and z=='cubic meters':
        volume_change = volume_raw*0.02832
        return volume_change
    #the input should not be wrong at this point, but just in case...
    else:
        print('The input is wrong')

#MAIN ROUTINE
#For triangle
if x=='triangle':
   #ask user to input parameters
    print('please input the length of side 1:')
    a=raw_input()
    print('please input the length of side 2:')
    b=raw_input()
    print('please input the length of side 3:')
    c=raw_input()
    print('please input the height:')
    h=raw_input()
    #calculate volume in input units
    volume_raw=triangle(a,b,c,h)
    #give output with unit conversion
    print ('The volume is '+str(unitchange(volume_raw))+' '+str(z))
#For square
elif x=='square':
    print('please input the length:')
    a=raw_input()
    print('please input the width:')
    b=raw_input()
    print('please input the height:')
    h=raw_input()
    volume_raw=square(a,b,h)
    print ('The volume is '+str(unitchange(volume_raw))+' '+str(z))
#For circle
elif x=='circle':
    print('please input the radius:')
    r=raw_input()
    print('please input the height:')
    h=raw_input()
    volume_raw=circle(r,h)
    print ('The volume is '+str(unitchange(volume_raw))+' '+str(z))

else:
    print('The input is wrong.')
    sys.exit(0)#stop the routine
