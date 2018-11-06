import numpy as np

def CollisionHandler(game, obj1, obj2):
    # print("Collision")
    # type1 = type(obj1)
    # type2 = type(obj2)

    # Need to determine the moveable/immoveable object
    

    # Calculate collision vector b = c - a (two origin vectors)
    a = np.asarray(obj1.center)
    c = np.asarray(obj2.center)

    b = np.subtract(c, a) # vector pointing from obj1 to obj2 center

    # Determine if we need to move the box horizontally or vertically
    if(abs(b[1]) > abs(b[0])): # Y is strictly greater than x
        obj2.move(0, b[1])
    else:
        obj2.move(b[0], 0)