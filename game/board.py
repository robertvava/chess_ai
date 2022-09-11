from src.constants import *
from src.pieces_png import *

class Board: 
    def __init__(self):
        self.tiles = [[Tile(row, col) for col in range(8)] for row in range(8)]
        self.selected_piece = None
        self.turn = WHITE
        self.king_captured = False
        self.moves_history = []
        self._init()
        self.draw_self()

    def draw_self(self) -> None:
        for row in self.tiles:
            for tile in row:
                tile._drawself()
                if tile.piece:
                    tile.piece._draw()

    def _init(self):
        for row in self.tiles:
            for tile in row:
                if (tile.row + tile.col) % 2 == 0:
                    tile.color = WOOD
        # Generate pawns
        for i in range(8):
            self.tiles[i][1].piece = Piece(i, 1, BLACK, 'Pawn', spring = b_pawn)
            self.tiles[i][6].piece = Piece(i, 6, WHITE, 'Pawn', spring = w_pawn)

        self.tiles[0][0].piece = Piece(0, 0, BLACK, 'Tower', spring = b_tower)
        self.tiles[7][0].piece = Piece(7, 0, BLACK, 'Tower', spring = b_tower)
        self.tiles[0][7].piece = Piece(0, 7, WHITE, 'Tower', spring = w_tower)
        self.tiles[7][7].piece = Piece(7, 7, WHITE, 'Tower', spring = w_tower)

        self.tiles[1][0].piece = Piece(1, 0, BLACK, 'Knight', spring = b_horse)
        self.tiles[6][0].piece = Piece(6, 0, BLACK, 'Knight', spring = b_horse)
        self.tiles[1][7].piece = Piece(1, 7, WHITE, 'Knight', spring = w_horse)
        self.tiles[6][7].piece = Piece(6, 7, WHITE, 'Knight', spring = w_horse)

        self.tiles[2][0].piece = Piece(2, 0, BLACK, 'Bishop', spring = b_bishop)
        self.tiles[5][0].piece = Piece(5, 0, BLACK, 'Bishop', spring = b_bishop)
        self.tiles[2][7].piece = Piece(2, 7, WHITE, 'Bishop', spring = w_bishop)
        self.tiles[5][7].piece = Piece(5, 7, WHITE, 'Bishop', spring = w_bishop)

        self.tiles[3][0].piece = Piece(3, 0, BLACK, 'Queen', spring = b_queen)
        self.tiles[3][7].piece = Piece(3, 7, WHITE, 'Queen', spring = w_queen)

        self.tiles[4][0].piece = Piece(4, 0, BLACK, 'King', spring = b_king, is_king = True)
        self.tiles[4][7].piece = Piece(4, 7, WHITE, 'King', spring = w_king, is_king = True)
        


class Tile:
    def __init__(self, row, col, occupied = False, piece = None, color = DARK_BROWN):
        self.row = row
        self.col = col
        self.surface = TILE_SURFACE
        self.occupied = occupied
        self.piece = piece
        self.color = color
    
    def _fill(self):
        self.surface.fill(self.color)
    
    def _drawself(self):
        self._fill()
        SCREEN.blit(self.surface, convert_to_pixels(self.row, self.col))
        if self.piece:
            self.piece._draw()
    



class Piece:
    def __init__(self, row, col, color, type, spring = None, controller = None, is_king = False):
        self.row = row
        self.col = col
        self.color = color 
        self.spring = spring
        self.controller = controller
        self.is_king = is_king


    def _draw(self):
        SCREEN.blit(self.spring, convert_to_pixels(self.row, self.col))
    
    def move(self, pos):
        self.row = pos[0]
        self.col = pos[1]
    
    def copy(self):
        """
        Creates a deep copy of the current piece
        :return: reference to a new Piece object
        """
        copy = type(self)(self.x, self.y, self.color)
        copy.image = self.image
        copy.firstMove = self.firstMove
        return copy 
        
