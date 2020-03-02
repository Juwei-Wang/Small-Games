import stddraw
import stdaudio
from picture import Picture
from juweip3 import GuitarString

key1 = ["q","2","w","e","4","r","5","t","y","7","u","8","i","9","0","p","-","[","=","z","x","d","c","f","v","g","b","n",
       "j","m","k",",",".",";","/","'"]

hz = []
for i in range(len(key1)):
    number = 110 * (2 ** (i / 12))
    hz.append(number)

# show a nice background picture
p = Picture("cpsc231-guitar.png")
stddraw.picture(p)
stddraw.show(0.0)

escape = False
while not escape:
    # check for and process events
    stddraw._checkForEvents()
    while stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == chr(27):
            escape = True
        index = 0
        for i in range(len(key1)):
            if key == key1[i]:
                   index = i
        n = GuitarString(hz[index])
        n.pluck()

    y = n.tick()
    y += n.tick()
    # simulate and play strings
    stdaudio.playSample(y)

