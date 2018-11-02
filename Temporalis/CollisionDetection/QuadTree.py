from pygame.rect import Rect

from GameObject import GameObject

THRESHOLD = 10 # Threshold of game objects to split tree

class QuadTree:
    def __init__(self, x, y, w, h):
        self.objects = set([]) #Unique, un-ordered
        self.children = []
        self.bounds = Rect(x, y, w, h)

    def insert(self, obj):
        """Add object to the tree."""
        # Need to raise an exception when object is out-of-bounds

        if not isinstance(obj, GameObject):
            raise Exception("Can only insert GameObject types into QuadTrees")

        if not ObjectWithinBounds(obj, self.bounds):
            raise Exception("Cannot insert Object out of bounds")
            
        if self.isLeaf:
            # Leaf node, add obj to self
            self.objects.add(obj)

            # If this addition breaks threshold, subdivide
            if len(self.objects) > THRESHOLD:
                SubdivideQuadTree(self)
        else:
            # Parent node, add obj to child tree
            for t in self.children:
                if ObjectWithinBounds(obj, t.bounds):
                    t.insert(obj)
                    return

    def clear(self):
        """Recursively remove all objects from tree."""
        self.objects = set([])
        for t in self.children:
            t.clear()

        self.children = []

    def getCollidableObjects(self, obj):
        """Find all collidable objects in same quad as object."""
        if obj in self.objects:
            returnCopy = self.objects.copy()
            returnCopy.remove(obj) # does this work?
            return returnCopy

        # else find the subtree that has it and return
        for t in self.children:
            subObjects = t.getCollidableObjects(obj)
            if subObjects:
                return subObjects

    @property
    def isLeaf(self):
        return not self.children # List is empty

# Helpers
def SubdivideQuadTree(tree):
    """Divide quad tree into 4 quadrants and extend the tree down"""
    sWidth = tree.bounds.width / 2 # split width
    sHeight = tree.bounds.height / 2 # split height

    # Top Left
    tree1 = QuadTree(tree.x, tree.y, sWidth, sHeight)
    tree1.objects = set(GetContainedObjects(tree, Rect(tree.x, tree.y, sWidth, sHeight)))

    # Top Right
    tree2 = QuadTree(tree.x + sWidth, tree.y, sWidth, sHeight)
    tree2.objects = set(GetContainedObjects(tree, Rect(tree.x + sWidth, tree.y, sWidth, sHeight)))

    # Bottom Left
    tree3 = QuadTree(tree.x, tree.y + sHeight, sWidth, sHeight)
    tree3.objects = set(GetContainedObjects(tree, Rect(tree.x, tree.y + sHeight, sWidth, sHeight)))

    # Bottom Right
    tree4 = QuadTree(tree.x + sWidth, tree.y + sHeight, sWidth, sHeight)
    tree4.objects = set(GetContainedObjects(tree, Rect(tree.x + sWidth, tree.y + sHeight, sWidth, sHeight)))

    tree.objects = set([])
    tree.children = [tree1, tree2, tree3, tree4]

def GetContainedObjects(tree, bounds):
    """Determine Quad membership based on bounds, center tuples"""
    objs = []
    for o in tree.objects:
        if ObjectWithinBounds(o, bounds):
            objs.append(o)
        return objs

def ObjectWithinBounds(obj, bounds):
    """Determine single object membership based on bounds"""
    return obj.centerx >= bounds.left and obj.centerx <= bounds.right and obj.centery >= bounds.top and obj.centery <= bounds.bottom