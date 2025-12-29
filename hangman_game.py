import requests
import os


def main():
    #get word
    response = requests.get('https://random-word-api.herokuapp.com/word?length=5')
    word = response.json()[0]

    #variables
    word_list = list(word)
    no_try = 0
    blank_word =(" _"*len(word))
    clean_blank_word=""

    #loop
    while no_try <= 8:
        check_clear()
        score_image(no_try)
        
        #is game over
        if no_try == 8:
            print("You Lose !!")
            print(f"Word : {word}")
            break
        elif clean_blank_word == word:
            print("Congrats, You Won !!")
            break

        #ask input
        print(blank_word)

        #ask input and check
        letter_entered = ask_input()

        #variable set
        blank_word_list = list(blank_word)
        position = 0
        flag = 0

        #look for the letter
        for letter in word_list:
            position += 1
            if letter == letter_entered:
                blank_word_list[position*2 - 1] = letter
                flag +=1   

        blank_word = "".join(blank_word_list)

        #word to compare
        clean_blank_word = cleaner_blank_word(blank_word_list)

        #count the no_try
        if flag == 0 :
            no_try +=1



#check the os and clear the screen
def check_clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')



def cleaner_blank_word(blank_word_list):
    word = ""
    for letter in blank_word_list:
        if 'a' <= letter <= 'z' :
            word = word + letter
    return word



def ask_input():
    while True:
        letter_entered = input("Enter the letter: ").strip().lower()
        if len(letter_entered) == 1 and 'a' <= letter_entered <= 'z':
            break
        else:
            print("Enter a letter.")
    return letter_entered



#print the hangman and the score
def score_image(no_try):
    #score
    print("_"*20, end="\n")
    score = 80 - (no_try*10)
    print(f"Score:{score:02d}")
    #print the hangman
    #line1
    if no_try >= 2:
        print("_"*7)
    else:
        print("")
    #line2
    if no_try >= 1:
        print("||"+" "*3,end="")
    else:
        print(" "*5,end="")
    if no_try >=2:
        print("|")
    else:
        print("")
    #line3
    if no_try >= 1:
        print("||"+" "*3,end="")
    else:
        print(" "*5,end="")
    if no_try >=3:
        print("o")
    else:
        print("")
    #line4
    if no_try >= 1:
        print("||"+" "*2,end="")
    else:
        print(" "*4,end="")
    if no_try >= 5:
        print(r"/",end="")
    else:
        print(" ",end="")
    if no_try >= 4:
        print(r"|", end="")
    else:
        print(" ",end="")
    if no_try >= 6:
        print("\\")
    else:
        print("")
    #line5
    if no_try >= 1:
        print("||"+" "*2,end="")
    else:
        print(" "*4,end="")
    if no_try >= 7:
        print(r"/", end="")
    else:
        print(" ",end="")
    print(" ",end="")
    if no_try >= 8:
        print("\\")
    else:
        print("")
    #line6,7
    if no_try >=1 :
        print("||")
        print("+======+")
    else:
        print("\n")
    #line8
    if no_try >=8:
        print("Game Over !!")
    else:
        print("")




#run the main function
if __name__ == "__main__" :
    main()
    