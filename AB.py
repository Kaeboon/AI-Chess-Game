import sys
import math

#############################################################################
######## Piece
#############################################################################

#Global variables
depth = 2
INF = math.inf
h_king = 20000
h_queen = 952
h_princess = 604
h_empress = 828
h_rook = 588
h_bishop = 364
h_knight = 240
h_ferz = 144
h_pawn = 42
h_check = 1000
#Those values are the sum of (no of pos a piece can move to) at every position in the 7x7 chessboard.

class Piece(object):
    def __init__(self, piece_name, piece_value, piece_colour, piece_pos):
        self.total_row = 7
        self.total_col = 7
        self.pos = piece_pos
        self.piece_name = piece_name
        self.piece_value = piece_value
        self.piece_colour = piece_colour
    
class King_Piece(Piece):
    def cause_danger_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (not(i==0 and j==0)):
                    if(self.piece_colour == "White"):
                        if(curr_row+i>=0 and curr_col+j>=0 and curr_row+i<self.total_row and curr_col+j<self.total_col and ((curr_row+i, curr_col+j) in black_poses) ):
                            danger_pos.add((curr_row+i, curr_col+j))
                    else:
                        if(curr_row+i>=0 and curr_col+j>=0 and curr_row+i<self.total_row and curr_col+j<self.total_col and ((curr_row+i, curr_col+j) in white_poses) ):
                            danger_pos.add((curr_row+i, curr_col+j))
        return danger_pos

    def can_move_to_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (not(i==0 and j==0)):
                    if(curr_row+i>=0 and curr_col+j>=0 and curr_row+i<self.total_row and curr_col+j<self.total_col and ((curr_row+i, curr_col+j) not in black_poses) and ((curr_row+i, curr_col+j) not in white_poses) ):
                        danger_pos.add((curr_row+i, curr_col+j))
        return danger_pos

class Rook_Piece(Piece):
    def cause_danger_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos =set()
        row = curr_row
        if(self.piece_colour=="White"):

            row = curr_row
            col = curr_col-1
            while(col>=0):
                if(((row, col) in black_poses) ):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in white_poses)):
                    break
                else:
                    col=col-1

            row = curr_row
            col = curr_col+1
            while(col<self.total_col):
                if(((row, col) in black_poses) ):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in white_poses)):
                    break
                else:
                    col=col+1
    
            row = curr_row-1
            col = curr_col
            while(row>=0):
                if(((row, col) in black_poses) ):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in white_poses)):
                    break
                else:
                    row=row-1
                    col=col

            row = curr_row+1
            col = curr_col
            while(row<self.total_row):
                if(((row, col) in black_poses) ):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in white_poses)):
                    break
                else:
                    row=row+1
                    col=col

            return danger_pos
        
        else:

            row = curr_row
            col = curr_col-1
            while(col>=0):
                if(((row, col) in white_poses) ):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in black_poses)):
                    break
                else:
                    col=col-1

            row = curr_row
            col = curr_col+1
            while(col<self.total_col):
                if(((row, col) in white_poses) ):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in black_poses)):
                    break
                else:
                    col=col+1
    
            row = curr_row-1
            col = curr_col
            while(row>=0):
                if(((row, col) in white_poses) ):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in black_poses)):
                    break
                else:
                    row=row-1
                    col=col

            row = curr_row+1
            col = curr_col
            while(row<self.total_row):
                if(((row, col) in white_poses) ):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in black_poses)):
                    break
                else:
                    row=row+1
                    col=col

            return danger_pos

    def can_move_to_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        row = curr_row

        row = curr_row
        col = curr_col-1
        while(col>=0):
            if(((row, col) not in black_poses) and ((row, col) not in white_poses)):
                danger_pos.add((row, col))
            else:
                break
            col=col-1

        row = curr_row
        col = curr_col+1
        while(col<self.total_col):
            if(((row, col) not in black_poses) and ((row, col) not in white_poses) ):
                danger_pos.add((row, col))
            else:
                break
            col=col+1
    
        row = curr_row-1
        col = curr_col
        while(row>=0):
            if(((row, col) not in black_poses) and ((row, col) not in white_poses) ):
                danger_pos.add((row, col))
            else:
                break
            row=row-1
            col=col

        row = curr_row+1
        col = curr_col
        while(row<self.total_row):
            if(((row, col) not in black_poses) and ((row, col) not in white_poses)):
                danger_pos.add((row, col))
            else:
                break
            row=row+1
            col=col

        return danger_pos

class Bishop_Piece(Piece):
    def cause_danger_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()

        if(self.piece_colour=="White"):

            row = curr_row-1
            col = curr_col-1
            while(row>=0 and col>=0):
                if(((row, col) in black_poses)):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in white_poses)):
                    break
                row=row-1
                col=col-1

            row = curr_row-1
            col = curr_col+1
            while(row>=0 and col<self.total_col):
                if(((row, col) in black_poses)):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in white_poses)):
                    break
                row=row-1
                col=col+1
        
            row = curr_row+1
            col = curr_col-1
            while(row<self.total_row and col>=0):
                if(((row, col) in black_poses)):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in white_poses)):
                    break
                row=row+1
                col=col-1

            row = curr_row+1
            col = curr_col+1
            while(row<self.total_row and col<self.total_col):
                if(((row, col) in black_poses)):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in white_poses)):
                    break
                row=row+1
                col=col+1

            return danger_pos

        else:

            row = curr_row-1
            col = curr_col-1
            while(row>=0 and col>=0):
                if(((row, col) in white_poses)):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in black_poses)):
                    break
                row=row-1
                col=col-1

            row = curr_row-1
            col = curr_col+1
            while(row>=0 and col<self.total_col):
                if(((row, col) in white_poses)):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in black_poses)):
                    break
                row=row-1
                col=col+1
        
            row = curr_row+1
            col = curr_col-1
            while(row<self.total_row and col>=0):
                if(((row, col) in white_poses)):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in black_poses)):
                    break
                row=row+1
                col=col-1

            row = curr_row+1
            col = curr_col+1
            while(row<self.total_row and col<self.total_col):
                if(((row, col) in white_poses)):
                    danger_pos.add((row, col))
                    break
                elif(((row, col) in black_poses)):
                    break
                row=row+1
                col=col+1

            return danger_pos          

    def can_move_to_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        row = curr_row-1
        col = curr_col-1
        while(row>=0 and col>=0):
            if(((row, col) not in black_poses) and ((row, col) not in white_poses) ):
                danger_pos.add((row, col))
            else:
                break
            row=row-1
            col=col-1

        row = curr_row-1
        col = curr_col+1
        while(row>=0 and col<self.total_col):
            if(((row, col) not in black_poses) and ((row, col) not in white_poses) ):
                danger_pos.add((row, col))
            else:
                break
            row=row-1
            col=col+1
    
        row = curr_row+1
        col = curr_col-1
        while(row<self.total_row and col>=0):
            if(((row, col) not in black_poses) and ((row, col) not in white_poses) ):
                danger_pos.add((row, col))
            else:
                break
            row=row+1
            col=col-1

        row = curr_row+1
        col = curr_col+1
        while(row<self.total_row and col<self.total_col):
            if(((row, col) not in black_poses) and ((row, col) not in white_poses) ):
                danger_pos.add((row, col))
            else:
                break
            row=row+1
            col=col+1

        return danger_pos

class Queen_Piece(Piece):
    def cause_danger_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        danger_pos.update(Rook_Piece("Rook", self.piece_value, self.piece_colour, self.pos).cause_danger_pos())
        danger_pos.update(Bishop_Piece("Bishop", self.piece_value, self.piece_colour, self.pos).cause_danger_pos())
        return danger_pos

    def can_move_to_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        danger_pos.update(Rook_Piece( "Rook", self.piece_value, self.piece_colour, self.pos).can_move_to_pos())
        danger_pos.update(Bishop_Piece("Bishop", self.piece_value, self.piece_colour, self.pos).can_move_to_pos())
        return danger_pos

class Knight_Piece(Piece):
    def cause_danger_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        parameter = [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]
        for para in parameter:
            row = curr_row+para[0]
            col = curr_col+para[1]
            if(self.piece_colour == "White"):
                if(row>=0 and col>=0 and row<self.total_row and col<self.total_col and ((row, col) in black_poses) ):
                    danger_pos.add((row, col))
            else:
                if(row>=0 and col>=0 and row<self.total_row and col<self.total_col and ((row, col) in white_poses) ):
                    danger_pos.add((row, col))
        return danger_pos

    def can_move_to_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        parameter = [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]
        for para in parameter:
            row = curr_row+para[0]
            col = curr_col+para[1]
            if(row>=0 and col>=0 and row<self.total_row and col<self.total_col and (  ((row, col) not in black_poses) and ((row, col) not in white_poses)  ) ):
                danger_pos.add((row, col))
        return danger_pos

class Ferz_Piece(Piece):
    def cause_danger_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        parameter = [(-1,-1),(1,1),(-1,1),(1,-1)]
        for para in parameter:
            row = curr_row+para[0]
            col = curr_col+para[1]
            if(self.piece_colour == "White"):
                if(row>=0 and col>=0 and row<self.total_row and col<self.total_col and ((row, col) in black_poses) ):
                    danger_pos.add((row, col))
            else:
                if(row>=0 and col>=0 and row<self.total_row and col<self.total_col and ((row, col) in white_poses) ):
                    danger_pos.add((row, col))
        return danger_pos

    def can_move_to_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        parameter = [(-1,-1),(1,1),(-1,1),(1,-1)]
        for para in parameter:
            row = curr_row+para[0]
            col = curr_col+para[1]
            if(row>=0 and col>=0 and row<self.total_row and col<self.total_col and ((row, col) not in black_poses) and ((row, col) not in white_poses)  ):
                danger_pos.add((row, col))
        return danger_pos

class Princess_Piece(Piece):
    def cause_danger_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        danger_pos.update(Bishop_Piece("Bishop", self.piece_value, self.piece_colour, self.pos).cause_danger_pos())
        danger_pos.update(Knight_Piece("Knight", self.piece_value, self.piece_colour, self.pos).cause_danger_pos())
        return danger_pos
    def can_move_to_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        danger_pos.update(Bishop_Piece("Bishop", self.piece_value, self.piece_colour, self.pos).can_move_to_pos())
        danger_pos.update(Knight_Piece("Knight", self.piece_value, self.piece_colour, self.pos).can_move_to_pos())
        return danger_pos

class Empress_Piece(Piece):
    def cause_danger_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        danger_pos.update(Rook_Piece("Rook", self.piece_value, self.piece_colour, self.pos).cause_danger_pos())
        danger_pos.update(Knight_Piece("Knight", self.piece_value, self.piece_colour, self.pos).cause_danger_pos())
        return danger_pos
    def can_move_to_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        danger_pos.update(Rook_Piece("Rook", self.piece_value, self.piece_colour, self.pos).can_move_to_pos())
        danger_pos.update(Knight_Piece("Knight", self.piece_value, self.piece_colour, self.pos).can_move_to_pos())
        return danger_pos

class Pawn_Piece(Piece):

    def cause_danger_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        if(self.piece_colour == "White"):
            i = 1; j = 1
            if (curr_row+i>=0 and curr_col+j>=0 and curr_row+i<self.total_row and curr_col+j<self.total_col and ((curr_row+i, curr_col+j) in black_poses) ):
                danger_pos.add((curr_row+i, curr_col+j))
            i = 1; j = -1
            if (curr_row+i>=0 and curr_col+j>=0 and curr_row+i<self.total_row and curr_col+j<self.total_col and ((curr_row+i, curr_col+j) in black_poses) ):
                danger_pos.add((curr_row+i, curr_col+j))
        else:
            i = -1; j = 1
            if (curr_row+i>=0 and curr_col+j>=0 and curr_row+i<self.total_row and curr_col+j<self.total_col and ((curr_row+i, curr_col+j) in white_poses) ):
                danger_pos.add((curr_row+i, curr_col+j))
            i = -1; j = -1
            if (curr_row+i>=0 and curr_col+j>=0 and curr_row+i<self.total_row and curr_col+j<self.total_col and ((curr_row+i, curr_col+j) in white_poses) ):
                danger_pos.add((curr_row+i, curr_col+j))
        return danger_pos

    def can_move_to_pos(self):
        curr_row = self.pos[0]
        curr_col = self.pos[1]
        danger_pos = set()
        if(self.piece_colour == "White"):
            i = 1; j = 0
        else:
            i = -1; j = 0
        if (curr_row+i>=0 and curr_col+j>=0 and curr_row+i<self.total_row and curr_col+j<self.total_col and ((curr_row+i, curr_col+j) not in black_poses) and ((curr_row+i, curr_col+j) not in white_poses)):
            danger_pos.add((curr_row+i, curr_col+j))
        return danger_pos

#format of move = (from_pos, to_pos, piece)

#Implement your minimax with alpha-beta pruning algorithm here.
def ab(gameboard):
    black_dict = dict() #(row, col): Black Piece
    white_dict = dict() #(row, col): White Piece
    chessboard = gameboard 
    for coor in chessboard:
        p = None
        BW = chessboard[coor][1]
        if BW == "White":
            h_multiplier = 1
        else:
            h_multiplier = -1
        if chessboard[coor][0] == "King":
            p = King_Piece("King", h_king, BW, coor)
            if BW == "White":
                white_king_piece = p
            else:
                black_king_piece = p
        elif chessboard[coor][0] == "Queen":
            p= Queen_Piece("Queen", h_queen*h_multiplier, BW, coor)
        elif chessboard[coor][0] == "Princess":
            p = Princess_Piece("Princess", h_princess*h_multiplier, BW, coor)
        elif chessboard[coor][0] == "Empress":
            p= Empress_Piece("Empress", h_empress*h_multiplier, BW, coor)
        elif chessboard[coor][0] == "Rook":
            p= Rook_Piece("Rook", h_rook*h_multiplier, BW, coor)
        elif chessboard[coor][0] == "Bishop":
            p= Bishop_Piece("Bishop", h_bishop*h_multiplier, BW, coor)
        elif chessboard[coor][0] == "Knight":
            p= Knight_Piece("Knight", h_knight*h_multiplier, BW, coor)
        elif chessboard[coor][0] == "Ferz":
            p= Ferz_Piece("Ferz", h_ferz*h_multiplier, BW, coor)
        elif chessboard[coor][0] == "Pawn":
            p= Pawn_Piece("Pawn", h_pawn*h_multiplier, BW, coor)
        chessboard[coor] = p
        if BW == "White":
            white_dict[coor] = p
        else:
            black_dict[coor] = p
        
    #Starting minimax operation:
    best_val = -INF
    starting_nodes = get_further_moves(black_dict, white_dict,True)
    for move in starting_nodes:
        black_king_piece, white_king_piece, new_black_dict, new_white_dict = move_piece(black_king_piece, white_king_piece, black_dict.copy(), white_dict.copy(), True, move)
        value = minimax(black_king_piece, white_king_piece, new_black_dict.copy(), new_white_dict.copy(), depth-1, False, -INF, INF)
        if value >= best_val:
            best_val =value
            best_move = move
    return outputt(best_move[0], best_move[1])

def minimax(black_king_piece, white_king_piece, black_dict, white_dict, d, is_max_player, alpha, beta):    
    if d == 0:
        v = 0
        for i in white_dict:
            v+=white_dict[i].piece_value
        for i in black_dict:
            v+=black_dict[i].piece_value
        return v
    
    if is_max_player:
        best_val = -INF
        child_node = get_further_moves(black_dict, white_dict, is_max_player)
        for move in child_node:
            black_king_piece, white_king_piece, new_black_dict, new_white_dict = move_piece(black_king_piece, white_king_piece, black_dict.copy(), white_dict.copy(), True, move)
            value = minimax(black_king_piece, white_king_piece, new_black_dict.copy(), new_white_dict.copy(), d-1, False, alpha, beta)
            if(move[1] == black_king_piece.pos):
                value += h_check
            best_val = max(best_val, value)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                break
        return best_val
    
    else:
        best_val = INF
        child_node = get_further_moves(black_dict, white_dict, is_max_player)
        for move in child_node:
            black_king_piece, white_king_piece, new_black_dict, new_white_dict = move_piece(black_king_piece, white_king_piece, black_dict.copy(), white_dict.copy(), False, move)
            value = minimax(black_king_piece, white_king_piece, new_black_dict.copy(), new_white_dict.copy(), d-1, True, alpha, beta)
            if(move[1] in white_king_piece.pos):
                value += h_check
            best_val = min(best_val, value)
            alpha = min(beta, best_val)
            if beta <= alpha:
                break
        return best_val        

def get_further_moves(black_dict, white_dict, is_max):
    children = set()
    moves = list()
    global black_poses
    global white_poses
    black_poses = black_dict
    white_poses = white_dict
    if is_max:
        for coor in white_dict:
            children.clear()
            children.update(white_dict[coor].cause_danger_pos())
            children.update(white_dict[coor].can_move_to_pos())
            for child in children:
                moves.append((coor, child))
        return moves
    else:
        for coor in black_dict:
            children.clear()
            children.update(black_dict[coor].cause_danger_pos())
            children.update(black_dict[coor].can_move_to_pos())
            for child in children:
                moves.append((coor, child))
        return moves

def outputt(pos1_from, pos2_to):
    pos1 = (chr(97+pos1_from[1]), int(pos1_from[0]))
    pos2 = (chr(97+pos2_to[1]), int(pos2_to[0]))
    return (pos1, pos2)

def move_piece(black_king_piece, white_king_piece, black_dict, white_dict, is_max, move):
    new_black_dict = black_dict.copy()
    new_white_dict= white_dict.copy()
    pos1 = move[0]
    pos2 = move[1]
    if is_max:
        piece = new_white_dict[pos1]
        piece.pos = pos2
        if(piece.piece_name == "King"):
            white_king_piece = piece
        new_white_dict[pos2]=piece
        new_white_dict.pop(pos1)
        if pos2 in new_black_dict:
            new_black_dict.pop(pos2)
    else:
        piece = new_black_dict[pos1]
        piece.pos = pos1
        if(piece.piece_name == "King"):
            black_king_piece = piece
        new_black_dict[pos2] = piece
        new_black_dict.pop(pos1)
        if pos2 in new_white_dict:
            new_white_dict.pop(pos2)
    return black_king_piece, white_king_piece, new_black_dict, new_white_dict
        


#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions


#############################################################################
######## Parser function and helper functions
#############################################################################
### DO NOT EDIT/REMOVE THE FUNCTION BELOW###
# Return number of rows, cols, grid containing obstacles and step costs of coordinates, enemy pieces, own piece, and goal positions
def parse(testcase):
    handle = open(testcase, "r")

    get_par = lambda x: x.split(":")[1]
    rows = int(get_par(handle.readline())) # Integer
    cols = int(get_par(handle.readline())) # Integer
    gameboard = {}
    
    enemy_piece_nums = get_par(handle.readline()).split()
    num_enemy_pieces = 0 # Read Enemy Pieces Positions
    for num in enemy_piece_nums:
        num_enemy_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_enemy_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "White")    

    own_piece_nums = get_par(handle.readline()).split()
    num_own_pieces = 0 # Read Own Pieces Positions
    for num in own_piece_nums:
        num_own_pieces += int(num)

    handle.readline()  # Ignore header
    for i in range(num_own_pieces):
        line = handle.readline()[1:-2]
        coords, piece = add_piece(line)
        gameboard[coords] = (piece, "Black")    

    return rows, cols, gameboard

def add_piece( comma_seperated) -> Piece:
    piece, ch_coord = comma_seperated.split(",")
    r, c = from_chess_coord(ch_coord)
    return [(r,c), piece]

def from_chess_coord( ch_coord):
    return (int(ch_coord[1:]), ord(ch_coord[0]) - 97)

# You may call this function if you need to set up the board
def setUpBoard():
    config = sys.argv[1]
    rows, cols, gameboard = parse(config)

### DO NOT EDIT/REMOVE THE FUNCTION HEADER BELOW###
# Chess Pieces: King, Queen, Knight, Bishop, Rook, Princess, Empress, Ferz, Pawn (First letter capitalized)
# Colours: White, Black (First Letter capitalized)
# Positions: Tuple. (column (String format), row (Int)). Example: ('a', 0)

# Parameters:
# gameboard: Dictionary of positions (Key) to the tuple of piece type and its colour (Value). This represents the current pieces left on the board.
# Key: position is a tuple with the x-axis in String format and the y-axis in integer format.
# Value: tuple of piece type and piece colour with both values being in String format. Note that the first letter for both type and colour are capitalized as well.
# gameboard example: {('a', 0) : ('Queen', 'White'), ('d', 10) : ('Knight', 'Black'), ('g', 25) : ('Rook', 'White')}
#
# Return value:
# move: A tuple containing the starting position of the piece being moved to the new ending position for the piece. x-axis in String format and y-axis in integer format.
# move example: (('a', 0), ('b', 3))

def studentAgent(gameboard):
    # You can code in here but you cannot remove this function, change its parameter or change the return type
    move = ab(gameboard)
    return move #Format to be returned (('a', 0), ('b', 3))

#######################
def self_test():
    testcase = sys.argv[1] #Do not remove. This is your input testfile.
    return studentAgent((parse(testcase))[2])

def enemy_move(config_path):
    testcase = config_path
    return studentAgent((parse(testcase))[2])

if __name__ == "__main__":
    print(self_test())