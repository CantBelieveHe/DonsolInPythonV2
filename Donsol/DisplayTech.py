from Donsol.Deck import Deck


class DisplayTech:


  def TranslateFace(self,card): 
    face = ""
    if card[0] == "S":
      face = "Shield"
    elif card[0] == "H":
      face = "Potion"
    elif card[0] == "M":
      face = "Zombie"
    elif card[0] == "G":
      face = "Skeleton"
    if card == "DR":
      face = "The Red Necromancer"
    if card == "DW":
      face = "The White Necromancer"
    return face

  
  def TranslateValue(self,card):
    val = 0
    if card[0] == "D": # if the card is a donsol
      val = 21
    if card[1].isnumeric(): # if the card is a number
      val = int(card[1]) # simply cast from string to int
    elif card[1] == 'T': # shorthand for 10
      val = 10
    elif card[0] == "H" or card[0] == "S": # potions and shields max at 11
      val = 11 
    elif card[0] == "M" or card[0] == "G": # monsters increase by values of 2
      if card[1] == "J":
        val = 11
      if card[1] == "Q":
        val = 13
      if card[1] == "K":
        val = 15
      if card[1] == "A":
        val = 17  
    return val  

  
  def MainMenu(self):
    print("------\n1. Start Game\n2. How to Play\n3. Quit Game")
  
  def StartGame(self):
    print("Starting Game...")

  def Reshuffling(self):
    print("Reshuffling Deck...")
  
  def QuitRound(self):
    print("Returning to main menu...")

  def PassRoom(self):
    print("Passing Room...")

  def SkipRoom(self):
    print("Skipping room..")
  
  def QuitGame(self):
    print("Thank you for playing!")

  def DrawDivider(self):
    print("----------------------------------------------------------------")

  
  def PrintCredits(self):
    print("\nDONSOL\n------\nOriginal card game created by John Eternal\nInspired by 100rabits' adaption\nCode by Carson Elmer")

  def PrintHowTo(self):
    print("- In Donsol, you must clear a dungeon full of enemies using the supplies you find along the way.\n- You can reshuffle the deck before taking your first move.\n- You can pass on the last card in a room and return it to the deck.\n- You can skip a full room and return it to the deck, but you cannot do this twice in a row.\n- Potions will refill your health(<3) up to 21.\n- Using potions back to back will cause them to have no effect.\n- Shields(< ]) will absorb damage when you attack enemies.\n- After the first use, your shield is damaged and will break if you attack an enemy greater or equal to the previous enemy.\n- Attacking a lower level enemy weakens your shield down to their level.\n- The game is won when you have defeated all enemies in the deck.")

  
  def ShowRoom(self,hand): # hand is a list of cards
    num = 0
    for i in hand: # for every entry in hand, make i that entry then:
      num += 1
      print("Card #"+str(num)+": "+self.TranslateFace(i)+" lvl: "+str(self.TranslateValue(i)))


  
  def ShowStats(self,roundNum,roomNum,health,potionSick,shield,shieldBroken,lastAttacked,cardsleft):
    # Turn number and room number
    temp = "Turn #: "+str(roundNum)
    temp = temp+" | Room #: "+str(roomNum)
    # health
    if potionSick:
      temp = temp+" | {<3} : "+str(health)
    elif health < 10:
      temp = temp+" | </3 : "+str(health)
    else:
      temp = temp+" | <3 : "+str(health)
    # shield
    if shieldBroken:
      temp = temp+" | </] : "+str(shield)
    else:
      temp = temp+" | < ] : "+str(shield)
    # last attacked and cards left
    temp = temp+" | Last: "+str(lastAttacked)
    print(temp+" | []]] : "+str(cardsleft))


  
  def ShowControls(self,roomSize,escapedLast,turnNumber):
    temp = ""
    if roomSize > 1:
      temp = temp+"Select card #1-"+str(roomSize)
    else:
      temp = temp+"Select card #1"
    # when these controls get simplified, so should this
    if turnNumber == 1:
      temp = temp+" | 'e' to reshuffle"
    elif not escapedLast and roomSize == 4:
      temp = temp+" | 'e' to run"
    if roomSize == 1:
      temp = temp+" | 'e' to pass"
    temp = temp+" | 'q' to quit"
    print(temp)


  
  # our only goal here is to tell the player what is changing, the actual game logic takes place elsewhere
  def ShowAction(self,card,shieldVal,shieldBroken,potionSick,lastAttacked):
    face = card[0]
    val = self.TranslateValue(card)
    att = False
    # shield
    if face == "S":
      print("You picked up a level "+str(val)+" shield!")
    # potion
    elif face == "H":
      print("You drink a level "+str(val)+" potion!")
      if potionSick:
        print("You cant keep the potion down!")
    # Enemies
    elif face == "M" or face == "G" or face == "D":
      if shieldVal == 0:
        print("You attack the undead with your bare hands and take "+str(val)+" damage!")
      else:
        print("You attack the level "+str(val)+" undead with your level "+str(shieldVal)+" shield!")
      if shieldBroken and val >= lastAttacked:
        print("Your shield breaks and you take "+str(val)+" damage!")
      elif shieldVal != 0 and val > shieldVal:
        print("Your shield holds and you take "+str(val-shieldVal)+" damage!")
      if val < shieldVal:
        print("Your shield weakens to level "+str(val)+"!")
      
  
  # fix meeeeeee
  def ShowEnding (self,containsMonsters,health):
    if health <= 0: #dead
      print("Panic sets in, as Death has entered the room and \nyou know, this time, Death is here for you...")
      if containsMonsters:#youLose
         print("There's no peace as life fades away, and you've been bested")
      else:#loserwinner
        print("You realize that nothing will escape this evil dungeon, including yourself.\nYou can take peace knowing you've vanquished the danger in this dungeon of horror")
    else:#truevictory
      print("With the last foe vanquished, you crawl out of the dungeon and see the light of day, You've vanquished this hell")
  
  # if dead
  #   if contains
  #     print you lose
  #   else
  #     print lose but win
  # else  
  #    print you win 
  ##### alternatively,
  # if not contains
  #   if dead
  #     print you lose but win
  #   else
  #     print you win
  # else
  #    print you lose

      
