from Donsol.GameLogic import GameLogic

# this file handles input and the menu.

gl = GameLogic()
command = ""
playing = True
menuCase = 0 # 0 = main menu, 1 = in-game, 3 = quit

gl.ShowCreds()
gl.ShowMainMenu()
while playing:
  if menuCase == 0: # on main menu
    command = input()
    if command == "1": # start game
      gl.StartGame()
      gl.PrintIntro()
      menuCase = 1
    elif command == "2": # show how to play
      gl.ShowHowTo()
      gl.ShowMainMenu()
    elif command == "3": # quit game
      playing = False # the while loop will detect this and end the loop
    else: 
      print("bad input")
      gl.ShowMainMenu()
  
  elif menuCase == 1: # in-game
    gl.CoreLoop()
    command = input()
    # the player selects a card in the room
    if command.isnumeric() and int(command) <= gl.GetRoomSize():
      gl.cardSelect(int(command))
      if gl.GetHealth() <= 0: # after a card is played, check if the player is dead
        gl.QuitRound()
        menuCase = 0
    # the player want to quit to the main menu
    elif command.lower() == "q":
      gl.QuitRound()
      menuCase = 0
    # the player wants to either reshuffle, pass the last card in a room, or skip a room.
    elif command.lower() == "e":
      if gl.GetRoomSize() == 1:
        gl.PassRoom()
      elif gl.GetRoundNum() == 1:
        gl.ReshuffleStart()
        gl.StartGame()
      elif not gl.GetEscapedLast():
        gl.EscapeRoom()

    else:
      print("Invalid command")

gl.ExitGame()
