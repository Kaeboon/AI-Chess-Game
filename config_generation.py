import os

def generate_config_file(pieces_info): 

    # Extract rows, cols, and pieces information
    rows = 8
    cols = 8  # Assuming an 8x8 chessboard  

    # Generate enemy_pieces and own_pieces based on initial_pieces_info
    enemy_pieces_count = {'King': 0, 'Queen': 0, 'Bishop': 0, 'Rook': 0, 'Knight': 0, 'Ferz': 0, 'Princess': 0, 'Empress': 0, 'Pawn': 0}
    own_pieces_count = {'King': 0, 'Queen': 0, 'Bishop': 0, 'Rook': 0, 'Knight': 0, 'Ferz': 0, 'Princess': 0, 'Empress': 0, 'Pawn': 0}  

    for piece, color in pieces_info.values():
        if color == 'Black':
            enemy_pieces_count[piece] += 1
        elif color == 'White':
            own_pieces_count[piece] += 1    


    # Extract enemy_positions and own_positions
    enemy_positions = [f'[{piece},{pos[0]}{pos[1]}]' for pos, (piece, color) in pieces_info.items() if color == 'Black']
    own_positions = [f'[{piece},{pos[0]}{pos[1]}]' for pos, (piece, color) in pieces_info.items() if color == 'White']  

    # Save configuration to config.txt
    with open('config.txt', 'w') as file:
        file.write(f'Rows:{rows}\n')
        file.write(f'Cols:{cols}\n')
        file.write(f'Number of Enemy King, Queen, Bishop, Rook, Knight, Ferz, Princess, Empress, Pawn (space between):{" ".join(map(str, enemy_pieces_count.values()))}\n')
        file.write('Position of Enemy Pieces:\n')
        file.write('\n'.join(enemy_positions) + '\n')   

        file.write(f'Number of Own King, Queen, Bishop, Rook, Knight, Ferz, Princess, Empress, Pawn (space between):{" ".join(map(str, own_pieces_count.values()))}\n')
        file.write('Starting Position of Pieces [Piece, Pos]:\n')
        file.write('\n'.join(own_positions) + '\n') 

    print("Configuration saved to config.txt")  
