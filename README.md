# **Strategic Grid Game**

## **Overview**
The Strategic Grid Game is a two-player grid-based game with AI capabilities, developed using Python and Pygame. It allows players to compete against each other or play against AI opponents, offering an engaging and strategic gameplay experience. The AI utilizes the Minimax algorithm to make optimal moves, adding a layer of challenge and intelligence to the game. The project also demonstrates the implementation of a Hash Table data structure with unit testing.

## **Features**
- **Multiple Game Modes:** 
  - Human vs Human
  - Human vs AI
  - AI vs AI
- **AI Decision-Making:** 
  - The game uses the Minimax algorithm to simulate and evaluate potential moves, allowing AI players to make strategic decisions.
- **Overflow Mechanics:** 
  - The game includes a recursive overflow mechanic that dynamically adjusts the grid, adding complexity to the gameplay.
- **Interactive GUI:** 
  - Built with Pygame, the GUI features smooth animations, interactive elements, and color-coded pieces for each player.
- **Save/Load Functionality:** 
  - Game states can be saved and loaded using Python’s pickle module, allowing players to resume their games.

## **Technologies Used**
- **Programming Language:** Python
- **Graphics Library:** Pygame
- **Algorithms:** Minimax Algorithm for AI decision-making
- **Data Structures:** Queue for overflow management and Hash Table with separate chaining
- **Persistence:** Python’s pickle module for saving/loading game states
- **Unit Testing:** Python’s unittest module for testing Hash Table functionality

## **Getting Started**

### **Prerequisites**
- Python 3.x
- Pygame library
- Clone or download the repository from GitHub
