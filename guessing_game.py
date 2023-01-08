
import random
from dice import Dice

def print_randomDice():
    rand1 =  random.randint(0,5)
    rand2 = random.randint(0,5)
    print(Dice.dice[rand1],Dice.dice[rand2])
    return (rand1 + 1) + (rand2 +  1)


def deposit():    
    while True:
        cash = input("How much money would you like to deposit? $")
        if cash.isdigit():
            cash = int(cash)
            if cash > 0 :
                break
            else:
                print("invalid aount")
        else:
            print("Please enter a number!")

    return cash

def winning_losing(guess,money,bet,times,number):
    if (guess == 'higher' and number > 7) or (guess == 'lower' and number < 7) or (guess == 'equal' and number == 7):
        money = money + (bet * times)
        print(f"Correct!! The number was {number} , total balance is {money} ")
    else:
        money =money-(bet * times)
        print(f"Sorry! You guessed wrong! The number was {number}, total balance is {money}")

    return money
    

def get_guess():
    while True:
        guess  = input("Guess 'higher','lower' than or 'equal' to 7!\t")
        if type(guess) == str:
            guess = guess.lower()
            if guess == 'higher' or guess == 'lower' or guess =='equal':
                break
            else:
                print("invalid guess!")
        else:
            print("Please enter higher,lower or equal!")

    return guess

def get_bet():
    while True:
        bet = input("Place your bet!\t$")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print("invalid bet")
        else:
            print("Please enter number!")
    return bet

def get_multiplier():
    while True:
        times = input("State your multiplier!")
        if times.isdigit():
            times = int(times)
            if times > 0:
                break
            else:
                print("invalid multiplier!")
        else:
            print("Please enter number!")

    return times

def gameStart():
    print("*" * 60)
    money = deposit()
    while True:
        print("*" * 60)
        guess = get_guess()
        print("*" * 60)
        bet = get_bet()
        print("*" * 60)
        times = get_multiplier()
        print("*" * 60)
        number = print_randomDice()
        
        money = winning_losing(guess,money,bet,times,number)
        if money <= 0 :
            print("You have lost all of your money!")
            break
        print("*" * 60)
        loop = input("Would you like to play again? Y/N\t")
        if type(loop) == str:
            loop = loop.lower()
            if loop == 'n':
                break
            elif loop == 'y':
                continue
            else:
                break  
        
gameStart()
