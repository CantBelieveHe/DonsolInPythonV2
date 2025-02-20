from Donsol.Deck import Deck
from Donsol.DisplayTech import DisplayTech

class GameLogic:

  __Health = 21
  __Shield = 0
  __LastAttacked = 0
  __ShieldBroken = False
  __PotionSick = False
  __EscapedLast = False
  __RoomNum = 0
  __RoundNum = 0
  __Hand = []
  

  def __init__(self): 
    self.__Deck = Deck()
    self.__displayTech = DisplayTech()


  def StartGame(self): 
    self.__RoomNum = 0
    self.__RoundNum = 1
    self.__Health = 21
    self.__Shield = 0
    self.__LastAttacked = 0
    self.__ShieldBroken = False
    self.__PotionSick = False
    self.__EscapedLast = False
    
    self.__Deck.ShuffleDeck()
    self.DrawRoom()


  def PrintIntro(self):
    self.__displayTech.StartGame()
  
  
  def GetRoundNum(self):
    return self.__RoundNum

  
  def GetRoomSize(self):
    return len(self.__Hand)

  
  def GetHealth(self):
    return self.__Health

  
  def GetEscapedLast(self):
    return self.__EscapedLast

  
  def ExitGame(self):
    self.__displayTech.QuitGame()

  def ShowHowTo(self):
    self.__displayTech.PrintHowTo()
  
  def ShowCreds(self):
    self.__displayTech.PrintCredits()

  
  def ShowMainMenu(self):
    self.__displayTech.MainMenu()

  
  def ReshuffleStart(self):
    self.__Deck.ResetDeck()
    self.__Hand = []
    self.__displayTech.Reshuffling()
    

  def QuitRound(self): # quit round of game, but not the whole game
    self.__displayTech.QuitRound()
    self.__displayTech.MainMenu()
    self.__Deck.ResetDeck()
    self.__Hand = []
    
  
  def DrawRoom(self): # draw up to 4 cards from the deck
    self.__RoomNum = self.__RoomNum + 1
    if self.__Deck.CardsLeft() > 3:
      for i in range(4):
        self.__Hand.append(self.__Deck.DrawCard())
    else:
      for i in range(self.__Deck.CardsLeft()):
        self.__Hand.append(self.__Deck.DrawCard())


  # i need to revisit the wording around "escaping" and "passing" rooms, later

  def PassRoom(self):
    while len(self.__Hand) > 0:
      self.__Deck.ReturnCard(self.__Hand.pop(0))
    self.DrawRoom()
    self.__RoundNum = self.__RoundNum + 1
    self.__EscapedLast = False
    self.__displayTech.PassRoom()


  def EscapeRoom(self):
    self.__EscapedLast = True
    while len(self.__Hand) > 0:
      self.__Deck.ReturnCard(self.__Hand.pop(0))
    self.DrawRoom()
    self.__RoundNum = self.__RoundNum + 1
    self.__displayTech.SkipRoom()
    

  def CoreLoop(self): # prints the current state of the game and available controls
    self.__displayTech.DrawDivider()
    self.__displayTech.ShowStats(self.__RoundNum,self.__RoomNum,self.__Health,self.__PotionSick,self.__Shield,self.__ShieldBroken,self.__LastAttacked,self.__Deck.CardsLeft())
    self.__displayTech.ShowRoom(self.__Hand)
    self.__displayTech.ShowControls(len(self.__Hand),self.__EscapedLast,self.__RoundNum)
    

  def TranslateValue(self,card): # this code also exists in DisplayTech, maybe we can piggyback off that file's code?
    # this function translates the shorthand to a numerical value
    val = 0
    if card[0] == "D": # both donsols are worth 21
      val = 21
    elif card[1].isnumeric(): # if the card is a number
      val = int(card[1]) # simply cast from string to int
    elif card[1] == 'T': # shorthand for 10
      val = 10
    elif card[0] == "H" or card[0] == "S": # potions and shields max at 11
      val = 11 
    elif card[0] == "M" or card[0] == "G": # monsters increase by values of 2
      if card[1] == "J":
        val = 11
      elif card[1] == "Q":
        val = 13
      elif card[1] == "K":
        val = 15
      elif card[1] == "A":
        val = 17  
    return val  

  
  def CardAction(self,card): # perform the action associated with the given card
    face = card[0]
    val = self.TranslateValue(card)
    self.__displayTech.ShowAction(card,self.__Shield,self.__ShieldBroken,self.__PotionSick,self.__LastAttacked)
    # shield
    if face == "S":
      self.__Shield = val
      self.__LastAttacked = 0
      self.__ShieldBroken = False
      self.__PotionSick = False
    # potion
    elif face == "H":
      if not self.__PotionSick: # as long as we are not potion-sick
        self.__Health = self.__Health + val
        if self.__Health > 21: # player health cannot be greater than 21
          self.__Health = 21
      self.__PotionSick = True # regardless of anything else, 
      # we are potion-sick since we drank a potion
    # enemy
    elif face == "M" or face == "G" or face == "D":
      if self.__Shield == 0:
        self.__Health = self.__Health - val
      else:
        if self.__ShieldBroken:
          if val >= self.__LastAttacked:
            self.__Health = self.__Health - val
            self.__Shield = 0
          elif self.__Shield < val:
            self.__Health = self.__Health - (val - self.__Shield)
        else:
          self.__ShieldBroken = True
          if self.__Shield < val and self.__Shield != 0:
            self.__Health = self.__Health - (val - self.__Shield)
      if self.__Shield > val:
        self.__Shield = val
      self.__ShieldBroken = True
      self.__PotionSick = False
      self.__LastAttacked = val
    # unrecognized card
    else:
      print("unrecognized card")

  
  def cardSelect(self,cardNum): # when the player selects a card in their hand
    self.__RoundNum = self.__RoundNum + 1
    self.CardAction(self.__Hand.pop(cardNum-1)) 
    # arrays are index-0, but humans tend to think in index-1, 
    # so we reduce the player's selection by 1 to make sure we get the right card,
    # and then we call the action method
    if self.__Health <= 0 or not self.__Deck.MonsterCheck():
      self.__displayTech.ShowEnding(self.__Deck.MonsterCheck(),self.__Health)
      # show the type of ending (phyrric victory or loss)
    elif len(self.__Hand) == 0:
      self.__EscapedLast = False
      self.DrawRoom()
