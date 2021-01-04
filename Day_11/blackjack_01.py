import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calc_score(cards):
  score = sum(cards)
  if sum(cards) == 21 and len(cards) == 2:
    score = 0
  if 11 in cards:
    cards.remove(11)
    cards.append(1)
  return score

def compare(me, house):
  if house == me:
    return "Draw! "

  if house == 21:
    return "Blackjack! House wins! "
  elif me == 21:
    return "Blackjack! You win! "
  elif house > 21:
    return "House is bust!. You win! "
  elif me > 21:
    return "Bust! House wins! "
  elif house > me:
    return "House wins. "
  else:
    return "You win! "

def blackjack():
  my_cards = []
  dealer_cards = []
  game_in_play = True

  for i in range(2):
    my_cards.append(deal_card())
    dealer_cards.append(deal_card())

  while game_in_play:
    my_score = calc_score(my_cards)
    dealer_score = calc_score(dealer_cards)
    print(f"Myhand: {my_cards}, yScore: {my_score}. " )
    print(f"Dealer's hand: {dealer_cards[0]}. ") 

    if my_score == 0 or dealer_score == 0 or my_score > 21:
      game_in_play = False
    else:
      hit = input("Hit? 'y' or 'n': \n")
      if hit == 'y':
        my_cards.append(deal_card())
      else:
        game_in_play = False

  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    calc_score(dealer_cards)
    
  print(f"Your final hand: {my_cards}. Final score: {my_score}. ")
  print(f"House final hand: {dealer_cards}. House final score: {dealer_score}. ")
  game = compare(my_score, dealer_score)

  print(game)

while input("Do you want to play blackjack? 'y' or 'n': \n") == 'y':

  blackjack()
  
