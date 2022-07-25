"""Ey yo"""
def main():
    """ try mai ru ja tum arai """
    money = float(input())
    water = int(input())
    amount1 = int(input())
    amount2 = int(input())
    amount3 = int(input())
    snack1 = money - water
    price = 0
    if snack1 % 3 == 0:
        price += 10 * amount1
    elif snack1 % 3 == 1:
        price += 15 * amount1
    elif snack1 % 3 == 2:
        price += 20 * amount1

    snack2 = snack1 - price
    if snack2 % 3 == 0:
        price += 12 * amount2
    elif snack2 % 3 == 1:
        price += 15 * amount2
    elif snack2 % 3 == 2:
        price += 18 * amount2

    snack3 = snack2 - price
    if snack3 % 3 == 0:
        price += 5 * amount3
    elif snack3 % 3 == 1:
        price += 7 * amount3
    elif snack3 % 3 == 2:
        price += 9 * amount3
    
    money -= price

    if money < 0:
        print("Now you have %d left."%money)
        print("You don't have enough money!")
    else:
        print("Now you have %d left."%snack3)
main()
