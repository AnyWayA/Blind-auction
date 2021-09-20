from replit import clear

people_bids = []


def add_new_person(user_name, user_bet):
    new_bet = dict()
    new_bet["Name"] = user_name
    new_bet["Bet"] = int(user_bet)
    people_bids.append(new_bet)


should_continue = True
while should_continue:
    name = input("Write your name: ")
    bet = input("Write your bet: $")

    add_new_person(name, bet)

    next_person = input("Is it someone else? yes/no: ").lower()
    clear()

    if next_person == "no":
        should_continue = False

max_bet = 0
winner_name = ""
for bids in people_bids:
    if bids["Bet"] > max_bet:
        max_bet = bids["Bet"]
        winner_name = bids["Name"]

print(f"The winner is {winner_name} with a bet of {max_bet}!")


