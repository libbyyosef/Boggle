# Boggle

**Introduction**

This repository contains a simple implementation of the Boggle game using Python and Tkinter. Boggle is a word game where players attempt to find words in sequences of adjacent letters on a grid.


![Boggle-start](https://github.com/libbyyosef/Boggle/assets/36642026/19c23bfb-6801-4096-9f79-ff6f842f458c)


https://github.com/libbyyosef/Boggle/assets/36642026/b06dce32-6ad7-403f-8933-ad9bc506ac92


![Boggle](https://github.com/libbyyosef/Boggle/assets/36642026/6c6f307c-5978-484d-a516-404b185328d9)


**Project Structure**
The project is organized into several files:

1. **start_window.py:** Contains the StartWindow class responsible for creating the initial window of the game.
2. **game_gui.py:** Contains the GameGui class, which represents the main game window where players can interact with the Boggle board.
3. **boggle_logic.py:** Contains the Boggle class, which manages the game logic, including the Boggle board, scoring, and word validation.
4. **game_ends_window.py:** Contains the GameEnds class, responsible for displaying the end-of-game window with the final score and options to restart or exit the game.
5. **ex12_utils.py:** Utility functions used in the project.
6. boggle_board_randomizer.py: Contains the function for randomizing the Boggle board.
7. **constant.py:** Defines constants used throughout the project.

**Additional Files**
Additional files have been added to enhance the project:

**images/background.png:** Image file used as the background for the StartWindow.
**images/game_over.png:** Image file used as the background for the GameEnds window.


**How to Play**

1. Start the game by launching the application.
2. The initial window will appear. Click the "Start" button to begin the game.
3. The game window will display the Boggle board, and you can click on adjacent letters to form words.
4. Use the "Enter" button to submit a word, "Clear" to clear the current input, and "Undo" to undo the last letter selection.
5.The game has a timer, and when it reaches zero, the game ends.
6. After the game ends, a window will display your final score and give you the option to restart or exit.
