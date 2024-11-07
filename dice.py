import random


# menu to welcome the player
def menu():
    print("""
    Welcome to dice\n
      Would you like to: \n
         1. Review the rule, \n
         2. play a new game \n
         3. review scoring of dice \n
         """)
    try:
        menu_choice = input("")
    except EOFError:
        print("No input received. Please run the program in an interactive environment.")
        return
    if menu_choice == "1":
        print_rules()
    elif menu_choice == "2":
        new_game()
    elif menu_choice == "3":
        print_scroing_values()
        second_meu()
    else:
        print("Invalid choice please choose again")
        second_meu()


#second menu to allow for a alteration of language

def second_meu():
    print("""
  What would you like to do now?
      Would you like to: \n
         1. Review the rule, \n
         2. play a new game \n
         3. review scoring of dice \n
         """)
    menu_choice = input("Please enter your choice: ")
    if menu_choice == "1":
        print_rules()
    elif menu_choice == "2":
        new_game()
    elif menu_choice == "3":
        print_scroing_values()
        second_meu()
    else:
        print("Invalid choice please choose again")
        second_meu()

#explantion of rules
def print_rules():
    print("""
  A player's turn always begins by throwing all six dice. The player then selects and set aside scoring dice, and at least one die must always be set aside. Then the player can throw the remaining dice again and the situation repeats. \n

  Scoring combinations are counted only for the current throw, not the entire turn.\n

  The key element of the game is that if a throw does not produce a single scoring die, then the player's turn is over and all points scored up to that throw are forfeit. It is then the opposing player's turn to throw. \n

  For that reason, it's best to end your turn before the risk that not a single die will score gets too high. Sometimes it's better not to set aside all the scoring dice you you've thrown, so you stand a better chance of scoring higher on the next throw.\n\n
  """)
    second_meu()

#and the scroing system
def print_scroing_values():
    print("""Scoring is as follows:
    - a single 1 is worth 100 points; \n
    - a single 5 is worth 50 points; \n
    - three of a kind is worth 100 points multiplied by the given number, e.g. three 4s are worth 400 points; \n
    - three 1s are worth 1,000 points;\n
    - four or more of a kind is worth double the points of three of a kind, so four 4s are worth 800 points, five 4s are worth 1,600 points etc.\n
    - full straight 1-6 is worth 1500 points.\n
    - partial straight 1-5 is worth 500 points.\n
    - partial straight 2-6 is worth 750 points.\n\n """)


# This die clas allows funtionality to roll a six sided dice and output the value.
class die:
    def __init__(self):
        self.value = 0

    def __repr__(self):
        return f"{self.value}"

    def roll(self):
        self.value = random.randint(1, 6)



#here is where the class objects are created and organised into a list for ease of use.
die1 = die()
die2 = die()
die3 = die()
die4 = die()
die5 = die()
die6 = die()

dice = [die1, die2, die3, die4, die5, die6]


#player class hold the dice values, the player name a method for rolling all 6 dice at one and rerolling specific dice.
class player:
    def __init__(self, name, dice_list, score=4000):
        self.name = name
        self.score = score
        self.dice_list = dice_list

    def deduct_score(self, deduction):
        self.score -= deduction
        return self.score

    def roll_d6(self):
        roll_string: str = ""                  #this funtion rolls all the dice coverts them to string and labels them 1 to 6 producing eg 1: 6, 2: 6, 3: 1, 4: 2, 5: 3, 6: 2
        i = 1
        for die in dice:
            die.roll()
            data = die.value
            str_data = str(data)
            str_i = str(i)
            roll_string += str_i + ": " + str_data + ", "
            i += 1
        return roll_string

    def print_d6(self):                                     #just print the values
        roll_string: str = ""
        i = 1
        for die in dice:
            data = die.value
            str_data = str(data)
            str_i = str(i)
            roll_string += str_i + ": " + str_data + ", "
            i += 1
        return roll_string


    def re_roll(self, index):                         #re rolls dice speficed
        index-=1
        dice[index].roll()
        return dice[index].value


#This is the main game loop it has a lot of moving parts. Take your time reviewing.
def new_game():
    print("Hi so what is your name?\n")
    human_name = input("")
    human_player = player(human_name, dice, 4000)   #creating objects for both human and computer players in the player class
    print("who do you wish to play against?")
    computer_name = input("")
    computer_player = player(computer_name, dice, 4000)
    play = True
    while (play):
        print("""ok here is your roll: 
    you roll a: """)
        print(human_player.roll_d6())     #use of the player class function roll_d6 to give a string of rolled dice
        print("Time to score you dice")
        total_dice_score = possible_to_score(human_player.dice_list)   #this function is below and check to see if any of the dice can score
        print(total_dice_score)
        print("Whould you like to re-roll you any dice? Y/N")  #allowing the player a chance to re roll dice
        lroll = input("")
        roll = lroll.upper()
        if (roll == "Y"):
            dice_choice(human_player)
        #print(dice)
        print("Time to score you dice")
        total_dice_score = possible_to_score(dice)
        print(total_dice_score)
        human_player.deduct_score(total_dice_score)
        print(f"Your score is now {human_player.score}")
        print(f"Ok it's {computer_player.name} go they rolled")
        print(computer_player.roll_d6())
        print("They scored:")
        total_dice_score = possible_to_score(dice)
        print(total_dice_score)
        computer_player.deduct_score(total_dice_score)
        print(f"{computer_player.name} score is now {computer_player.score}")
        input("")
        if human_player.score <= 0 or computer_player.score <= 0:
            if human_player.score <= 0:
                print("You win well done!!")
            else:
                print("You lose to bad.")
            play = False



def possible_to_score(dice):    #dice is a alis for eaither human_player.dice_list or computer_player.dice_list which would look like [1, 2, 3, 4, 5, 6] with random numbers beteen 1 and 6 in each index.
    dice_score = 0
    numbers = count(dice)   #this function count the number of each dice rolled is is a little complex
    #print(dice)             #more functionality checking
    #print(numbers)
    isone = one(numbers)      #each of these are seperate function that check for andy 1s, 5s, any kinds e.g. dice that rolled the same number like four 5s, a full straight or a parital stright
    isfive = five(numbers)
    isthree_of_kind = three_of_kind(numbers)
    isfour_of_kind = four_of_kind(numbers)
    isfive_of_kind = five_of_kind(numbers)
    issix_of_kind = six_of_kind(numbers)
    isfull_straight = full_straight(numbers)
    isone_to_five = one_to_five(numbers)
    istwo_to_six = two_to_six(numbers)
    #print(isone, isfive, isthree_of_kind, isfour_of_kind, isfive_of_kind, issix_of_kind, isfull_straight, isone_to_five, istwo_to_six)      #used this to check the function was working in construction
    if (isone == True):
        dice_score = 10

    if (isfive == True):
        dice_score = 50

    if (isthree_of_kind[0] == True):
        dice_score = 100 * isthree_of_kind[1]    #these function woudl assign score to the dice depeding on valibles

    if (isfour_of_kind[0] == True):
        dice_score = 200 * isfour_of_kind[1]

    if (isfive_of_kind[0]):
        dice_score = 400 * isfive_of_kind[1]

    if (issix_of_kind[0]):
        dice_score = 800 * issix_of_kind[1]

    if (isfull_straight == True):
        temp_dice_score = 1500
        if temp_dice_score > dice_score:
            dice_score = temp_dice_score

    if (isone_to_five == True):
        temp_dice_score = 500
        if temp_dice_score > dice_score:
            dice_score = temp_dice_score
    if (istwo_to_six == True):
        temp_dice_score = 600

        if temp_dice_score > dice_score:
            dice_score = temp_dice_score
    return dice_score

def one(counts):
    if counts[0] >= 1:
        return True
    else:
        return False

def five(counts):
    if counts[4] >= 1:
        return True
    else:
        return False


def three_of_kind(counts):
    if 3 in counts:
        return True, counts.index(3)
    else:
        return False, None


def four_of_kind(counts):
    if 4 in counts:
        return True, counts.index
    else:
        return False, None


def five_of_kind(counts):
    if 5 in counts:
        return True, counts.index
    else:
        return False, None


def six_of_kind(counts):
    if 6 in counts:
        return True, counts.index
    else:
        return False, None


def full_straight(counts):
    if all(value == 1 for value in counts):
        return True
    else:
        return False

def one_to_five(counts):
    if counts[0] <= 1 & counts[1] <= 1 & counts[2] <= 1 & counts[3] <= 1 & counts[4] <= 1:
        return True
    else:
        return False


def two_to_six(counts):
    if counts[1] <= 1 & counts[2] <= 1 & counts[3] <= 1 & counts[4] <= 1 & counts[5] <= 1:
        return True
    else:
        return False

def count(dice):                   #dice is a alis for eaither human_player.dice_list or computer_player.dice_list which would look like [1, 2, 3, 4, 5, 6] with random numbers beteen 1 and 6 in each index.
    value_counts = count_values(dice)
    num_ones = value_counts[1]         #the job of this to take the 1: prefix to all the counts to leave behind only the count itself
    num_twos = value_counts[2]
    num_threes = value_counts[3]
    num_fours = value_counts[4]
    num_fives = value_counts[5]
    num_sixes = value_counts[6]
    numbers_list = [num_ones, num_twos, num_threes, num_fours, num_fives, num_sixes]
    return numbers_list   #this goes back to new game

def count_values(dice_list):
    counts = {i: 0 for i in range(1, 7)}     #this created this {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for die in dice_list:
        counts[die.value] += 1 #assins each of the dice to a value in numerical order eg of output {1: 1, 2: 1, 3: 2, 4: 1, 5: 1, 6: 0}
    return counts

def dice_choice(player):    #alis for human_player
    rolling = True
    print("Please type the dice you want to re-roll after each choice press enter. When you finish type exit and press enter.")
    while (rolling):
        player_input = input("")
        if player_input.isdigit():                     #checks is the input is a number
            number = int(player_input)
            if 1 <= number <= 6:                        #checks if it falls between 1 and 6
                player.re_roll(number)                         #rolls the dice specified
            else:
                print("Invalid entry must be a value between 1 and 6")
        elif player_input == "exit":
            print(f"Your new values are: {player.print_d6()} .")              #outputs the results
            rolling = False
        else:
            print("invalid entry must be a number or exit, please try again.")


menu()

