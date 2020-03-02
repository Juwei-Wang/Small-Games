"""
Review of the data type

-data type is set of values and operation and operations on them
- float, int, str, list,color
we work with data types by creating objects of particular type

what's an object
identity location in memory
-data
-type - specifies the object's behaviour
-data type value - what data is store
we access objects through references
a variable holds a reference to an object
turquoise | []
          "reference"

-similarities:
    use in assignment statement
    as elements of an array(list)
    as arguments to function
    as operations for
-differences;
    need import for user defined types
    python literals create built in typos
    'hello' ot 99.90
    vs color(r,g,b)

picture data type(from booksite library)
- 2d array of colors

Creating data types

define an Api for the data type
for a stopwatch
constructor stopwatch()

start timing s.start()

reset to zero s.zero()

class stopwatch

turtle graphics
- turtle tobot for drawing
-very simple API
-create a turtle at (x,y)
-tell turtle to turn left by some angle
- go forward , drawing a line along  the way

"""
from picture import Picture
import stddraw

my_picture = Picture("karel1.jpg")
stddraw.picture(my_picture,0.5,0.5)
stddraw.setFontSize(64)
stddraw.text(0.5,0.2,"I live !")
stddraw.show()