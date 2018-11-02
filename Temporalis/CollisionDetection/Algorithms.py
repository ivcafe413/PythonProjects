import numpy as np

def CollideRectTest(rect1, rect2):
    # Should always be of type pygame Rect
    return rect1.colliderect(rect2)

def SeparatingAxisTest(rect1, rect2):
    pass

def BBSeparatingAxisTest(rect1, rect2):
    axisX = np.array([1, 0])
    axisY = np.array([0, 1])

    rect1a = np.asarray(rect1.topleft)
    rect1b = np.asarray(rect1.topright)

    rect2a = np.asarray(rect2.topleft)
    rect2b = np.asarray(rect2.topright)

    # develop min/max projections
    rect1minX = np.dot(rect1a, axisX)
    rect1maxX = np.dot(rect1b, axisX)
    rect2minX = np.dot(rect2a, axisX)
    rect2maxX = np.dot(rect2b, axisX)

    # check for gap
    isGapX = (rect2minX > rect1maxX or
        rect1minX > rect2maxX)

    if(isGapX):
        # there is a gap along the x axis, return true
        return False

    # else check Y axis
    rect1c = np.asarray(rect1.bottomleft)
    rect2c = np.asarray(rect2.bottomleft)

    rect1minY = np.dot(rect1a, axisY)
    rect1maxY = np.dot(rect1c, axisY)
    rect2minY = np.dot(rect2a, axisY)
    rect2maxY = np.dot(rect2c, axisY)

    isGapY = (rect2minY > rect1maxY or
        rect1minY > rect2maxY)

    if(isGapY):
        return False

    # if both checks fail, then collision
    return True

def GJK(rect1, rect2):
    pass

def MinkowskiPortalRefinement(rect1, rect2):
    pass

def MinkowskiDifference(rect1, rect2):
    pass

def AABBDetection(rect1, rect2):
    return (rect1.x <= rect2.x + rect2.width and
        rect2.x <= rect1.x + rect1.width and
        rect1.y <= rect2.y + rect2.height and
        rect2.y <= rect1.y + rect1.height)