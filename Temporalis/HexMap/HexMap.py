from itertools import product

class HexMap:
    def __init__(self, tiles_across, tiles_down, tile_radius):
        self.tilesAcross = tiles_across
        self.tilesDown = tiles_down
        self.tileRadius = tile_radius

        self.coordinates = list(product(range(tiles_across), range(tiles_down)))
        