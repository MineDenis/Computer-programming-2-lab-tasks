import sys
import math

def area(s):
    return (4 * pi) * (s  2)

def volume(s):
    return ( 4 / 3 * pi) * (s  3)

def main(): 
    start_r = float(sys.argv[1]) 
    inc_r = float(sys.argv[2]) 
    end_r = float(sys.argv[3]) 
    h1 = 'Radius (m)' 
    h4 = '-' * len(h1) 
    h2 = 'Area (m^2)' 
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)' 
    h6 = '-' * len(h3) 
    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3)) 
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))
    V = start_r
    I = inc_r
    For i in range(i, end_r) and not (v >= end_r):
        Pog = area(v)
        Dog = volume(v)
        print('{:>10.2f} {:>15.2f} {:>15.2f}'.format(v, pog, dog))
        V = v + i

if name == 'main': 
main()