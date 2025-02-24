A remake of the card game designed by John Eternal.
Inpsired by the adaption created by 100Rabits.
Code written by Carson Elmer without the use of AI.

The game runs in the command line and requires a local install of python. Simply run main.py to begin playing the game.
This project was made to introduce a freind to the basics of game programming, highlighting the core loop of "1. update game state. 2. display game state. 3. take user input."

While performance and security are not very relevant on a project of this size, the game logic is designed to uphold performance and protect object data were the project to be scaled.
The deck of cards is stored as a list of strings written in shorthand. The name and value of the cards is interpreted when they enter the player's hand. 
Objects do not directly access data in other objetcs, they instead access methods to allow the target object to update its own data.
