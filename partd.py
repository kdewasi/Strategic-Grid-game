# Function to create a deep copy of the board
def copy_board(board):
    current_board = []
    height = len(board)
    # Copy each row to create a new board
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board

# Function to evaluate the board's score for the given player
def evaluate_board(board, player):
    score = 0
    # Loop through each cell in the board
    for row in board:
        for cell in row:
            # Check if the player has four in a row (assuming cell = 4 * player means a winning state)
            if cell == 4 * player:
                score += 100 * player  # Assign high score for winning
            elif cell == player:
                score += 1  # Add score for player's pieces
            elif cell == -player:
                score -= 1  # Subtract score for opponent's pieces
    return score 

# Class to represent the game tree for AI decision-making
class GameTree:
    
    # Inner class to represent each node in the game tree
    class Node:
        def __init__(self, board, depth, player, tree_height=4):
            self.board = copy_board(board)  # Copy of the board at this node
            self.depth = depth  # Depth of the node in the tree
            self.player = player  # Player to move at this node
            self.children = []  # List of child nodes (possible moves)
            # Generate children if the current depth is less than the tree height
            if depth < tree_height:
                self.generate_children(tree_height)

        # Function to generate child nodes (possible moves)
        def generate_children(self, tree_height):
            height = len(self.board)
            width = len(self.board[0])
            # Iterate over each cell in the board
            for row in range(height):
                for col in range(width):
                    if self.board[row][col] == 0:  # Check if the cell is empty
                        new_board = copy_board(self.board)  # Copy the board
                        new_board[row][col] = self.player  # Place the player's piece
                        # Add the new board configuration as a child node
                        self.children.append(GameTree.Node(new_board, self.depth + 1, -self.player, tree_height))

    # Initialize the game tree with the current board, player, and desired tree height
    def __init__(self, board, player, tree_height=4):
        self.player = player  # Player who will make the move
        self.root = self.Node(board, 0, player, tree_height)  # Root node of the tree

    # Minimax algorithm to evaluate the best possible move
    def minimax(self, node, maximizing_player):
        # Base case: if the node has no children or reaches a terminal depth
        if len(node.children) == 0 or node.depth == 3:
            return evaluate_board(node.board, self.player)

        if maximizing_player:
            max_eval = float('-inf')  # Initialize max evaluation score
            for child in node.children:
                eval = self.minimax(child, False)  # Recursively evaluate child nodes
                max_eval = max(max_eval, eval)  # Choose the maximum score
            return max_eval

        else:
            min_eval = float('inf')  # Initialize min evaluation score
            for child in node.children:
                eval = self.minimax(child, True)  # Recursively evaluate child nodes
                min_eval = min(min_eval, eval)  # Choose the minimum score
            return min_eval

    # Function to get the best move for the current player
    def get_move(self):
        best_move = None
        best_score = float('-inf')  # Initialize the best score
        # Iterate over all possible moves
        for child in self.root.children:
            score = self.minimax(child, False)  # Evaluate the move using minimax
            if score > best_score:  # Check if this move is better
                best_score = score
                max_row_index = 0
                max_col_index = 0
                max_val = float('-inf')
                # Find the position of the move in the board
                for i in range(len(child.board)):
                    for j in range(len(child.board[0])):
                        if child.board[i][j] * self.player > max_val:
                            max_val = child.board[i][j] * self.player
                            max_row_index = i
                            max_col_index = j
                best_move = (max_row_index, max_col_index)  # Save the best move
        return best_move

    # Function to clear the game tree (freeing memory)
    def clear_tree(self):
        self.root = None  # Set the root to None to delete the tree
