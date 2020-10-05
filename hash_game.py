def valid_move(X, player):
    """This function will return a two pair tuple with valid index to hash table game

    Args:
        X (list): [the hash table]
        player (int): [the numeral that reprent a player]

    Returns:
        [tuple]: [two valid index to hash table game]
    """
    valid = True
    valid_input = (0, 1, 2)
    
    while valid:
        move = input('Por favor Jogador {}, faça sua jogada (x,y): '.format(player))
        # built in function to cut the input in two pair tuple
        pos = move.split(",")
        move_tuple = [int(num) for num in pos]
        
        if move_tuple[0] in valid_input and move_tuple[1] in valid_input and X[move_tuple[0]][move_tuple[1]] == 0:
            valid = False
        else:
            print("InvalidPlay")
    return move_tuple

def hash_board(X):
    
    tabuleiro =  '''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
'''.format(*X[0], *X[1], *X[2])

    return tabuleiro
    
def winner(X):
    """Returns True if a player won the game else False

    Args:
        X (list): [the hash table]

    Returns:
        [boolean]: True if a player won the game else False
    """
  # Horizontal case.
    for l in range(3):
        if X[l][0] == X[l][1] == X[l][2] != 0:
            return True

  # Vertical case.
    for c in range(3):
        if X[0][c] == X[1][c] == X[2][c] != 0:
            return True

  # Diagonal cases.
    if X[0][0] == X[1][1] == X[2][2] != 0:
        return True

    elif X[2][0] == X[1][1] == X[0][2] != 0:
        return True
    return False


def main():
    X = [[0,0,0],[0,0,0],[0,0,0]]

    # infinite loop
    while True:
        # looping to change player
        for player in (1,2):
            # printing the hash board
            print(hash_board(X))
            move_tuple = valid_move(X, player)

            # Marking the place for the player 1 or 2.
            X[move_tuple[0]][move_tuple[1]] = player
            if winner(X):
                print("Parabéns, o Jogador {} ganhou!!!".format(player))
                print(hash_board(X))
                return
            
            if 0 not in (*X[0], *X[1], *X[2]):
                print("Empate!")
                print(hash_board(X))
                return

main()