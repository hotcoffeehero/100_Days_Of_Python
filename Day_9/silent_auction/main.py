from replit import clear
from art import logo
print(logo)

#bid_tally = bids
bids = {}
bidding_done = False

def tally_ho(bid_tally):
  high_bid = 0
  winner = ''
  for bidder in bid_tally:
    bid_val = bid_tally[bidder]
    if bid_val > high_bid:
      high_bid = bid_val
      winner = bidder
  print(f"The winner is ${winner} who bet $${high_bid}.")



while not bidding_done:
  name = input("What is your name?")
  bid = input("What is your bid?")
  bids[name] = bid
  message = input("Any more bidders? Type: 'yes' or 'no'. ")
  if message == 'no':
    bidding_done = True
    tally_ho(bids)
  else:
    clear()