import random

def startgame():
    attempts = 0
    rand_num = random.randint(1,10)
    player_name = input("What is your name? ")
    print(f"Hi {player_name}, Welcome to the NUMBER GUESSING GAME")
    wanna_play = input("Do you want to play? ")
    while wanna_play.lower()== 'yes':
        attempts += 1
        guess = int(input("Pick a number between 1 and 10: "))
        if(guess>10 or guess<1):
            print("Out of range.....Try again!!!!")
           
            
            continue
        if guess>rand_num:
            print("Its lower")
        elif guess<rand_num:
            print("Its higher")
        else:
            print("Nice! You got it!")
            print(f"It took you {attempts} attempts")
            play_again = input("Would you like to play again? (Enter Yes/No): ")
            if(play_again.lower()=='yes'):
                attempts = 0
                rand_num=rand_num = random.randint(1,10)
            else:
                print(f"Thank you {player_name} for playing")
                break
            
if __name__=='__main__':
    startgame()
