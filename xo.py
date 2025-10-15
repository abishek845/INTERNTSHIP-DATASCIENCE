board = [' ' for i in range(9)]
player = 'X'
winner = None
game_running = True

print("TIC TAC TOE GAME")
print("Positions:")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9\n")

while game_running:
    print(f"{player}'s turn")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])

    move = int(input("Enter position (1-9): ")) - 1

    if board[move] == ' ':
        board[move] = player
    else:
        print("Position already taken! Try again.")
        continue

    # Check for winner
    if board[0] == board[1] == board[2] != ' ':
        winner = board[0]
    elif board[3] == board[4] == board[5] != ' ':
        winner = board[3]
    elif board[6] == board[7] == board[8] != ' ':
        winner = board[6]
    elif board[0] == board[3] == board[6] != ' ':
        winner = board[0]
    elif board[1] == board[4] == board[7] != ' ':
        winner = board[1]
    elif board[2] == board[5] == board[8] != ' ':
        winner = board[2]
    elif board[0] == board[4] == board[8] != ' ':
        winner = board[0]
    elif board[2] == board[4] == board[6] != ' ':
        winner = board[2]

    # Check for winner or draw
    if winner:
        print(f"\nPlayer {winner} wins!")
        game_running = False
    elif ' ' not in board:
        print("\nIt's a draw!")
        game_running = False
    else:
        if player == 'X': player = 'O'
        else:
            player = 'X'

# Final board display
print("\nFinal Board:")
print(board[0] + " | " + board[1] + " | " + board[2])
print("--+---+--")
print(board[3] + " | " + board[4] + " | " + board[5])
print("--+---+--")
print(board[6] + " | " + board[7] + " | " + board[8])
