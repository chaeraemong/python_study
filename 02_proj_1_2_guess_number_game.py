import random

random_number=random.randint(1,100)

game_count=1

while True:
    my_number=int(input("Enter a number between 1 and 100 : "))

    if my_number>random_number:
        print("Down")

    elif my_number<random_number:
        print("Up")

    elif my_number==random_number:
        print(f"Congradulations. You`ve won by {game_count} tries.")
        break

    game_count=game_count+1
