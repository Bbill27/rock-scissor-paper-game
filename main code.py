import random as rd

def start():
    global player,chosen

    #rock player
    if player == "rock" and chosen == "paper":
        print(f"player Lose "+ "\n"
              f"Ai choose:{chosen}")
    elif player == "rock" and chosen == "scissor":
        print(f"player Win "+ "\n"
              f"Ai choose:{chosen}")
    elif player == "rock" and chosen == "rock":
        print(f"player Tide "+ "\n"
              f"Ai choose:{chosen}")

    #paper player
    elif player == "paper" and chosen == "scissor":
        print(f"player Lose "+ "\n"
              f"Ai choose:{chosen}")
    elif player == "paper" and chosen == "rock":
        print(f"player Win "+ "\n"
              f"Ai choose:{chosen}")
    elif player == "paper" and chosen == "paper":
        print(f"player Tide "+ "\n"
              f"Ai choose:{chosen}")

    #scissor player
    elif player == "scissor" and chosen == "scissor":
        print(f"player Tide "+ "\n"
              f"Ai choose:{chosen}")
    elif player == "scissor" and chosen == "rock":
        print(f"player Lose "+ "\n"
              f"Ai choose:{chosen}")
    elif player == "scissor" and chosen == "paper":
        print(f"player Win " + "\n"
              f"Ai choose:{chosen}")

    #exit player
    elif player == "exit":
        print("let's play next time!")

    else:
        print("error")


my_list = ["rock", "scissor", "paper"]
chosen = rd.choice(my_list)


while True:
    player = input().lower()
    start()
    if player == "exit":
        break
