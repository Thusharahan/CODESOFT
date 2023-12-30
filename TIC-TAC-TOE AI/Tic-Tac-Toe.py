

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        # Check rows
        if all(cell == player for cell in board[i]):
            return True

        # Check columns
        if all(board[j][i] == player for j in range(3)):
            return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_empty_positions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, maximizing_player):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_positions(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, False)
            board[i][j] = ' '
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_positions(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, True)
            board[i][j] = ' '
            min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board, player):
    best_move = None
    best_eval = float('-inf') if player == 'O' else float('inf')

    for i, j in get_empty_positions(board):
        board[i][j] = player
        eval = minimax(board, 0, player == 'O')
        board[i][j] = ' '

        if (player == 'O' and eval > best_eval) or (player == 'X' and eval < best_eval):
            best_eval = eval
            best_move = (i, j)

    return best_move

def ai_place_coin(board, ai_player):
    ai_move = get_best_move(board, ai_player)
    board[ai_move[0]][ai_move[1]] = ai_player
    print_board(board)

def ai_drag_coin(board, ai_player):
    best_move = None
    best_eval = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ai_player:
                possible_moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                possible_moves = [(x, y) for x, y in possible_moves if 0 <= x < 3 and 0 <= y < 3 and board[x][y] == ' ']

                for move in possible_moves:
                    board[move[0]][move[1]] = ai_player
                    eval = minimax(board, 0, False)
                    board[move[0]][move[1]] = ' '

                    if eval > best_eval:
                        best_eval = eval
                        best_move = (i, j, move)

    if best_move:
        i, j, (new_i, new_j) = best_move
        board[new_i][new_j] = ai_player
        board[i][j] = ' '
        print_board(board)

def human_place_coin(board, human_player):
    while True:
        try:
            i = int(input("Enter the row index to place your 'X' coin: "))
            j = int(input("Enter the column index to place your 'X' coin: "))

            if board[i][j] == ' ':
                board[i][j] = human_player
                print_board(board)
                break
            else:
                print("That position is already occupied. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def human_drag_coin(board, human_player):
    while True:
        try:
            i = int(input("Enter the row index of the coin to move: "))
            j = int(input("Enter the column index of the coin to move: "))

            if board[i][j] == human_player:
                break
            else:
                print("You can only move your own coin. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

    while True:
        try:
            new_i = int(input("Enter the new row index: "))
            new_j = int(input("Enter the new column index: "))

            if (new_i, new_j) == (i, j):
                print("New position cannot be the same as the current position. Try again.")
            elif (new_i, new_j) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] and board[new_i][new_j] == ' ':
                board[new_i][new_j] = human_player
                board[i][j] = ' '
                print_board(board)
                break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X'
    ai_player = 'O'

    print_board(board)

    # Human places the 1st coin
    human_place_coin(board, human_player)
    if check_winner(board, human_player):
        print("Congratulations! You win!")
        return
    elif is_board_full(board):
        print("The game is drawn!")
        return

    # AI places the 1st coin
    ai_place_coin(board, ai_player)
    if check_winner(board, ai_player):
        print("Sorry, you lose. The AI wins!")
        return
    elif is_board_full(board):
        print("The game is drawn!")
        return

    # Human places the 2nd coin
    human_place_coin(board, human_player)
    if check_winner(board, human_player):
        print("Congratulations! You win!")
        return
    elif is_board_full(board):
        print("The game is drawn!")
        return

    # AI places the 2nd coin
    ai_place_coin(board, ai_player)
    if check_winner(board, ai_player):
        print("Sorry, you lose. The AI wins!")
        return
    elif is_board_full(board):
        print("The game is drawn!")
        return

    # Human places the 3rd coin
    human_place_coin(board, human_player)
    if check_winner(board, human_player):
        print("Congratulations! You win!")
        return
    elif is_board_full(board):
        print("The game is drawn!")
        return

    # AI places the 3rd coin
    ai_place_coin(board, ai_player)
    if check_winner(board, ai_player):
        print("Sorry, you lose. The AI wins!")
        return
    elif is_board_full(board):
        print("The game is drawn!")
        return

    # Human drags coins
    for _ in range(3):
        human_drag_coin(board, human_player)
        if check_winner(board, human_player):
            print("Congratulations! You win!")
            return
        elif is_board_full(board):
            print("The game is drawn!")
            return

        # AI drags coins
        ai_drag_coin(board, ai_player)
        if check_winner(board, ai_player):
            print("Sorry, you lose. The AI wins!")
            return
        elif is_board_full(board):
            print("The game is drawn!")
            return

if __name__ == "__main__":
    play_game()
