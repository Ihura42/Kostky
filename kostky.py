import random
import time

def roll_dice(num_dice):
    result = []
    for i in range(num_dice):
        result.append(random.randint(1, 6))
    return result

def calculate_score(dice):
    score = 0
    counts = []
    for i in range(1,7):
        counts.append(dice.count(i))

    # 1
    score += counts[0] * 100

    # 5
    score += counts[4] * 50

    # 3x stejné číslo nebo 3x jedniček
    for i in range(6):
        if counts[i] >= 3:
            if i + 1 == 1:
                score += 1000
            else:
                score += (i + 1) * 100

    # 4x stejné číslo nebo 4x jedniček
    for i in range(6):
        if counts[i] == 4:
            if i + 1 == 1:
                score += 2000
            else:
                score += (i + 1) * 200

    # 5x stejné číslo nebo 5x jedniček
    for i in range(6):
        if counts[i] == 5:
            if i + 1 == 1:
                score += 4000
            else:
                score += (i + 1) * 400

    # 6x stejné číslo nebo 6x jedniček
    for i in range(6):
        if counts[i] == 6:
            if i + 1 == 1:
                score += 8000
            else:
                score += (i + 1) * 800

    # 3 dvojice
    if counts.count(2) == 3 and counts.count(1) == 0:
        score += 1000

    # postupka
    if counts == [1, 1, 1, 1, 1, 1]:
        score += 1500
    
    return score

def main():
    total_score = 0
    body = int(input("Enter the amount of points to end the game: "))
    
    dice_numbers = roll_dice(6)
    print(f"Dice rolled: {dice_numbers}")
    time.sleep(1)

    score = calculate_score(dice_numbers)
    total_score += score

    print(f"Added score: {score}")
    time.sleep(1)
    print(f"Your total score is: {total_score}")
    time.sleep(1)

    if total_score >= body:
        print("Congratulations! You have reached the specified score.")
    else:
        print("You haven't reached the specified score. Better luck next time.")

main()