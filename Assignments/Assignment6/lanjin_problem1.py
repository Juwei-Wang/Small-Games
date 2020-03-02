import stddraw
import stdaudio
from picture import Picture
from juweip3 import GuitarString

a_string = GuitarString(440.00)
c_string = GuitarString(523.25)

p = Picture('cpsc231-guitar.png')
stddraw.picture(p)
stddraw.show(0.0)

escape = False
while not escape:  
    stddraw._checkForEvents()
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == chr(27):
            escape = True
        elif key == 'a':       
            print("a")   
            a_string.pluck()          
        elif key == 'c':      
            print("c")  
            c_string.pluck()                       
    y = a_string.tick()
    y += c_string.tick()
    stdaudio.playSample(y)

# python3 lanjin_problem1.py
