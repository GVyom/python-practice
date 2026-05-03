print('''                ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
''')
player = {}
game = True

while game == True:
    Name = input("Hi, Please put your name here: ").lower()
    Bid = int(input("Please let us know your bid amount: "))
    if Name in player:
        if Bid > player[Name]:
            player[Name] = Bid
            print("Your Bid is updated successfully")
        else:
            print("Same or lower bids are not allowed under auction policies, please re-enter your bid or pass to next candidate")
    else:
        player[Name] = Bid
    
    if len(player) < 2:
        print("At least 2 bids are needed for auction to be valid")
        continue
    else:
        game_continue = input("Continue Bidding?(Yes/No): ").lower()
    if game_continue == "no":
        game = False
    
highest_bid = 0
winner = ""
for win in player:
    if player[win] > highest_bid:
        highest_bid = player[win]
        winner = win
    
print(f"The winner for this bid is {winner} with bid amount {highest_bid}")

#if player:  # safety check (avoid crash if empty)
#    winner = max(player, key=player.get)
 #   highest_bid = player[winner]
  #  print(f"\n🏆 Winner is {winner} with a bid of {highest_bid}")
#else:
 #   print("No bids were placed.")