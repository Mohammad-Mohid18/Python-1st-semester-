# Tic-Tac-Toe game in Python (simplified)

# Initialize the board with hardcoded values
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

current_player = "X"

while True:
    # Print the board
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
    
    # Get the player's move
    try:
        row = int(input(f"Player {current_player}, enter row (0-2): ")) - 1
        col = int(input(f"Player {current_player}, enter column (0-2): ")) - 1
    except ValueError:
        print("Invalid input. Please enter integers between 0 and 2.")
        continue
    
    if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
        print("Invalid move. The cell is either out of bounds or already occupied.")
        continue
    
    # Make the move
    board[row][col] = current_player
    
    # Check for a winner
    winner = False
    for row in board:
        if row.count(current_player) == 3:
            winner = True
            break
    
    for col in range(3):
        if all(board[row][col] == current_player for row in range(3)):
            winner = True
            break
    
    if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
        winner = True
    if board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player:
        winner = True
    
    if winner:
        # Print final board and announce winner
        for row in board:
            print(" | ".join(row))
            print("-" * 5)
        print(f"Player {current_player} wins!")
        break
    
    # Check for a draw
    if all(cell != " " for row in board for cell in row):
        # Print final board and announce draw
        for row in board:
            print(" | ".join(row))
            print("-" * 5)
        print("It's a draw!")
        break
    
    # Switch players
    current_player = "O" if current_player == "X" else "X"