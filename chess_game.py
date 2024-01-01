import os
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from AB import enemy_move
from config_generation import generate_config_file

# Initial position of pieces in international chess with row indices starting at 0
initial_pieces_info = {
    ('a', 0): ('Rook', 'White'), ('b', 0): ('Knight', 'White'), ('c', 0): ('Bishop', 'White'),
    ('d', 0): ('Queen', 'White'), ('e', 0): ('King', 'White'), ('f', 0): ('Bishop', 'White'),
    ('g', 0): ('Knight', 'White'), ('h', 0): ('Rook', 'White'),
    ('a', 1): ('Pawn', 'White'), ('b', 1): ('Pawn', 'White'), ('c', 1): ('Pawn', 'White'),
    ('d', 1): ('Pawn', 'White'), ('e', 1): ('Pawn', 'White'), ('f', 1): ('Pawn', 'White'),
    ('g', 1): ('Pawn', 'White'), ('h', 1): ('Pawn', 'White'),

    ('a', 7): ('Rook', 'Black'), ('b', 7): ('Knight', 'Black'), ('c', 7): ('Bishop', 'Black'),
    ('d', 7): ('Queen', 'Black'), ('e', 7): ('King', 'Black'), ('f', 7): ('Bishop', 'Black'),
    ('g', 7): ('Knight', 'Black'), ('h', 7): ('Rook', 'Black'),
    ('a', 6): ('Pawn', 'Black'), ('b', 6): ('Pawn', 'Black'), ('c', 6): ('Pawn', 'Black'),
    ('d', 6): ('Pawn', 'Black'), ('e', 6): ('Pawn', 'Black'), ('f', 6): ('Pawn', 'Black'),
    ('g', 6): ('Pawn', 'Black'), ('h', 6): ('Pawn', 'Black'),
}


def print_white_piece(chess_dict):
    for key, value in chess_dict.items():
        if 'White' in value:
            position_str = f"{key[0]}{key[1]}"
            print(f"({position_str}, {value[0]}), ", end='')


fig, ax = plt.subplots()
pieces_info = initial_pieces_info.copy()

# Function to draw the chessboard
def draw_chessboard(fig, ax):    
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal', adjustable='box')
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                ax.add_patch(plt.Rectangle((i, j), 1, 1, fill=True, color='lightgray'))

# Function to place chess pieces on the board with images
def place_chess_pieces(ax, pieces):
    for position, piece_info in pieces.items():
        col, row = ord(position[0]) - ord('a'), position[1]
        piece_type, piece_color = piece_info[0][0].lower(), piece_info[1].lower()

        # Append a unique string for certain pieces
        if piece_type == 'p':
            piece_type += 'awn'
        elif piece_type == 'k':
            piece_type += 'night' if piece_info[0] == 'Knight' else 'ing'
        elif piece_type == 'n':
            piece_type += 'ight'

        piece_image_path = os.path.join(os.getcwd(), 'images', f'{piece_type}_{piece_color}.png').replace(os.sep, '/')
        imagebox = OffsetImage(plt.imread(piece_image_path), zoom=0.5)
        ab = AnnotationBbox(imagebox, (col + 0.5, row + 0.5), frameon=False, pad=0)
        ax.add_artist(ab)

# Draw the chessboard and place pieces with images
draw_chessboard(fig, ax)
place_chess_pieces(ax, initial_pieces_info)

# Add row indices on the left 
for i in range(7, -1, -1):
    ax.text(-0.5, 8.5 - abs(8-i), str(i), ha='center', va='center', fontsize=8)

# Add column indices on the top
for i in range(8):
    ax.text(i + 0.5, 8.5, chr(ord('a') + i), ha='center', va='center', fontsize=8)

# Show the chessboard
plt.axis('off')
# plt.ion()
# plt.pause(0.1)  # Allow time for the plot to be displayed
plt.show(block=False)

def convert_to_tuple(position):
    # Assuming position is a string like 'a1'
    alphabet, number = position[0], int(position[1])
    return alphabet, number

def convert_to_str(position):
    # Assuming position is a tuple like ('a', 1)
    alphabet, number = position[0], position[1]
    return alphabet + str(number)

# Function to move a chess piece
def move_white_chess_piece(pieces):
    print("Current White Pieces (position, piece):")
    print_white_piece(pieces)
    print("")
    
    piece_to_move = convert_to_tuple(input("Enter the position of the piece you want to move (e.g., a1): ").lower())
    if piece_to_move not in pieces or pieces[piece_to_move][1]=='Black':
        print("Invalid position. Try again.")
        return pieces

    new_position = convert_to_tuple(input("Enter the new position for the piece (e.g., b2): ").lower())
    if new_position in pieces and pieces[new_position][1]=='White':
        print("A white piece already exists at the new position. Try again.")
        return pieces

    # Move the piece to the new position
    pieces[new_position] = pieces.pop(piece_to_move)

    return pieces

def move_black_chess_piece(pieces, move):
    print("Current Black Pieces (position, piece):")
    print_white_piece(pieces)
    print("")
    
    piece_to_move = move[0]
    if piece_to_move not in pieces or pieces[piece_to_move][1]=='White':
        print("Invalid position. Try again.")
        return pieces

    new_position = move[1]
    if new_position in pieces and pieces[new_position][1]=='Black':
        print("A Black piece already exists at the new position. Try again.")
        return pieces

    # Move the piece to the new position
    pieces[new_position] = pieces.pop(piece_to_move)

    return pieces


# Interactive input loop for moving chess pieces
while True:
    print("###################################")
    pieces_info = move_white_chess_piece(pieces_info)
    generate_config_file(pieces_info)
  
    # Clear the current plot
    ax.clear()
    draw_chessboard(fig, ax)
    
    # Redraw the chessboard and place pieces with images
    place_chess_pieces(ax, pieces_info)
    
    # Add row and column indices
    for i in range(7, -1, -1):
        ax.text(-0.5, 8.5 - abs(8-i), str(i), ha='center', va='center', fontsize=8) 

    # Add column indices on the top
    for i in range(8):
        ax.text(i + 0.5, 8.5, chr(ord('a') + i), ha='center', va='center', fontsize=8)

    # Show the updated chessboard
    plt.axis('off')
    plt.draw()
    plt.pause(0.1)  # Allow time for the updated plot to be displayed

    print("###################################")
    # Enemy's turn:
    move = (enemy_move('.\config.txt'))
    print(f"Enemy move from {convert_to_str(move[0])} to {convert_to_str(move[1])}")

    pieces_info = move_black_chess_piece(pieces_info, move)
    generate_config_file(pieces_info)
  
    # Clear the current plot
    ax.clear()
    draw_chessboard(fig, ax)
    
    # Redraw the chessboard and place pieces with images
    place_chess_pieces(ax, pieces_info)
    
    # Add row and column indices
    for i in range(7, -1, -1):
        ax.text(-0.5, 8.5 - abs(8-i), str(i), ha='center', va='center', fontsize=8) 

    # Add column indices on the top
    for i in range(8):
        ax.text(i + 0.5, 8.5, chr(ord('a') + i), ha='center', va='center', fontsize=8)

    # Show the updated chessboard
    plt.axis('off')
    plt.draw()
    plt.pause(0.1)  # Allow time for the updated plot to be displayed


    
       
