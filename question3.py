# jode mustafa
# u41333726

# this program generates a random number and then a response based on  that number to answer a question asked by the user, program keeps running until user says no
import random


value= random.randint(0,20)

def __main__():
    question= input("what is your question ")
    global value
    value= random.randint(0,20)

def printing_function():
    answers= {
        0:"it is certain", 1:"it is decidedly so", 2: "without a doubt", 3:"yes- defnietly" , 4:"you may rely on it",
        5 :"as i see it,yes", 6:"most likely", 7:"outlook good",8:"yes", 9:"signs point to yes", 10:'reply hazy, try again', 11:"ask again latrt", 12: "better not tell you now", 13: "cannot predit now", 14:"concentrate and ask again",
        15: "dont count on it ", 16:"my reply is no", 
        17: "my sources say no", 18:"outlook not so good", 19: "very doubtful"
    }
    answer= (answers[value])
    print(answer)  
    global continue_game
    continue_game= input("would you like to continue game ").lower()


__main__()
printing_function()
while  continue_game != "no":
    __main__()
    printing_function()