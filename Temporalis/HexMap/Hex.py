from HexDirection import AXIAL_DIRECTIONS as DIRECTIONS

class Hex:
    def __init__(self, q, r):
        self.q = q
        self.r = r

    @property
    def s(self):
        """Interpolated s-coordinate of Hex"""
        return - self.q - self.r

    def hexDirection(self, direction):
        """Return hex direction, given 0 based direction, clockwise from SE"""
        axial = DIRECTIONS[direction]
        return Hex(*axial) # *expands tuples into discrete args

    def hexNeighbor(self, direction):
        """Return actual hex neighbor, given axial direction"""
        d = self.hexDirection(direction)
        return Hex(self.q + d.q, self.r + d.r)