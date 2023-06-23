'''it works like a normal tuple but its more readable, in a tuple its just about indexing using the numbers.'''
#usecase: example -> to represent rgb values as a tuple
'''why dont we use dictionary??, becuase we need the functionality of the tuple which is immutability'''
from collections import namedtuple

Point = namedtuple('Point','x,y') #here point is the name of the class,this is more like a struct concept

#pt  =Point(x=1,y=-4) #to be more explicit while defining values
pt  =Point(1,-4) 
print(pt)

print(pt.x) #more readable
print(pt.y)
'''we can also use this as a regular tuple'''
print(pt[0])#gives the value of 1st index

'''example two'''
Color = namedtuple('Color','red,green,blue')
black_color = Color(0,0,0)
white_color = Color(255,255,255)
print(black_color.blue)
print(white_color.blue)