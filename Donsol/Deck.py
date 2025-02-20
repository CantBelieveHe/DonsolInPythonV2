import random

class Deck:
  def __init__(self): # this method is run when the object is created
    self.__cards = ['S1','S2','S3','S4','S5','S6','S7','S8','S9','ST','SJ','SQ','SK','H1','H2','H3','H4','H5','H6','H7','H8','H9','HT','HJ','HQ','HK','M1','M2','M3','M4','M5','M6','M7','M8','M9','MT','MJ','MQ','MK','G1','G2','G3','G4','G5','G6','G7','G8','G9','GT','GJ','GQ','GK','DR','DW']


  def ResetDeck(self): # by calling the init method, we reset the deck to its starting point
    self.__init__()
    
    
  def CardsLeft(self): # return the current size (length) of the deck
    return len(self.__cards) 
    

  def ShuffleDeck(self): # we will use a built-in python function to shuffle the deck
    random.shuffle(self.__cards) 
    

  def GetDeck(self): # return the deck rather than accessing the list directly
    return self.__cards
    

  def DrawCard(self):
    if self.CardsLeft() == 0: # if the deck is empty, return none
      return None # we include this to prevent an error if the deck is empty
    return self.__cards.pop(0) # remove and return the top of the deck
    

  def ReturnCard(self, card): # add the card to the bottom of the deck
    self.__cards.append(card) 
    

  def MonsterCheck(self): # we use this when we check if the game is over
    minotaurs = [s for s in self.__cards if s[0] == 'M']
    goblins = [s for s in self.__cards if s[0] == 'G']
    return not (len(minotaurs) == 0 and len(goblins) == 0)
    # if no minotaurs and no goblins is true, return false
    # in other words, return true if there are monsters, false if there are none

