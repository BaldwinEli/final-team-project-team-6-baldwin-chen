import math
import sys

#INPUT THE PARAMETERS
print('please choose the shape of the base(trangle/cube/circle):')
x=raw_input()
if x!='trangle' or x!='cube' or x!='circle':
    print('The input is wrong')
    sys.exit(0)#stop the routine
print('please choose the unit(inch/foot/meter) of input:')
y=raw_input()
if y!='inch' or y!='foot' or y!='meter':
    print('The input is wrong')
    sys.exit(0)#stop the routine
print('please choose the unit(cubic foot/gallon/cubic meter) of output:')
z=raw_input()
if z!='cubic foot' or z!='gallon' or z!='cubic meter':
    print('The input is wrong')
    sys.exit(0)#stop the routine

#DEFINE THE CALCULATION OF DIFFERENT SHAPES
def trangle(a,b,h):
    area=int(a)*int(b)/2
    v=area*int(h)
    return v

def cube(a,b,h):
    area=int(a)*int(b)
    v=area*int(h)
    return v

def circle(r,h):
    area=int(r)**2*math.pi
    v=area*int(h)
    return v

#DEFINE UNIT CONVERSION
def unitchange(volume_raw):
    if y=='foot' and z=='cubic foot':
        volume_change= volume_raw
        return volume_change
    elif y=='inch' and z=='cubic foot':
        volume_change = volume_raw*0.0005787
        return volume_change
    elif y=='meter' and z=='cubic foot':
        volume_change = volume_raw*35.31467
        return volume_change
    elif y=='inch' and z=='gallon':
        volume_change = volume_raw*0.004329
        return volume_change
    elif y=='foot' and z=='gallon':
        volume_change = volume_raw*7.4805
        return volume_change
    elif y=='meter' and z=='gallon':
        volume_change = volume_raw*264.17
        return volume_change
    elif y=='meter' and z=='cubic meter':
        volume_change = volume_raw
        return volume_change
    elif y=='inch' and z=='cubic meter':
        volume_change = volume_raw*0.000016387
        return volume_change
    elif y=='foot' and z=='cubic meter':
        volume_change = volume_raw*0.02832
        return volume_change
    else:
        print('The input is wrong')

#MAIN ROUTINE
if x=='trangle':
    print('please input the base:')
    a=raw_input()
    print('please input the base:')
    b=raw_input()
    print('please input the height:')
    h=raw_input()
    volume_raw=trangle(a,b,h)
    print ('The volume is '+str(unitchange(volume_raw))+' '+str(z))
    

elif x=='cube':
    print('please input the base:')
    a=raw_input()
    print('please input the base:')
    b=raw_input()
    print('please input the height:')
    h=raw_input()
    volume_raw=cube(a,b,h)
    print ('The volume is '+str(unitchange(volume_raw))+' '+str(z))

elif x=='circle':
    print('please input the radius:')
    r=raw_input()
    print('please input the height:')
    h=raw_input()
    volume_raw=circle(r,h)
    print ('The volume is '+str(unitchange(volume_raw))+' '+str(z))

else:
    print('The input is wrong.')
    sys.exit(0)#stop the routiine
