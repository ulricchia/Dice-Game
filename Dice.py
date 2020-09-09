#This game simulates the game Lucky sevens. The player rolls 2 dice and if the numbers add up to 7, then the players win 4 dollars and if they dont, then they lose 1 dollar.  This program simulates how much you would make and it shows you how many rolls it took and the value of the pot. It also shows if you win or lose your money or not.
import random  #Import random means that it can randomly choose a bunch of random numbers in a number generator. it it needed for codes like this


def get_random_roll(): #Makes the rolls in the code random 
    return random.choice(range(1, 7)) # The rules of DICE means that you can roll and connect the dots and it has to be in the range of 1-7. So i set the random choice range to 1,7


def main(): #Defines this whole code as the main code 
    while True:
        money = int(input("Enter the amount of money you want to put in pot: ")) #Input money and it will take how much money you have and run the code.
        roll_count = 0
        print("#", roll_count, "Put $"+str(money))  #Makes it so that it will print out how much money there is and what # the roll is
        max_won = money 
        while money != 0: 
            roll_count += 1
            dice1 = get_random_roll() #having this makes it so dice 1 is randomly rolled
            dice2 = get_random_roll() #having this makes it so dice 2 is randomly rolled
            if dice1 + dice2 == 7: #If the 2 dices get a roll of 7, then you get 4 dollars and it prints into the table.
                money += 4 #Adds 4 dollars
                print("#", roll_count, 'Win $'+str(money))
            else: #If you do not roll that, then it will print loss of $, and then you will lose 1 dollar.
                money -= 1 #subtracts 1 dollar
                print("#", roll_count, 'Loss $', str(money)) #Shows the count and how much money there is.
            max_won = max(max_won, money)
        print("You lost your money after", roll_count, "rolls") #Shows how much many rolls it took for player to lose the money.
        print("The maximum amount of money in the pot during the playing is $"+str(max_won)) #This will show you how much money you made at the highest point of the game
        choice = input("Do you want to play again? [Y/N] ") #This code makes it so that if you lose money, you can restart by pressing y or n.
        if choice.lower() != 'y': #If pressed y, then the code will restart again
            break


if __name__ == "__main__":
    main()
