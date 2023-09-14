# jode mustafa
# u41333726
# #this program use list of the questions from TriviaQuestion module and start the game
#the program switch turns between players and ask them for the answer and it checks if the answer is correct or not
#If the player’s answer is correct, that player gets a point.
#at the end the program declers if it is a tie or the player with the highest points as the winner.

import questions
from trivia import trivia_game

t1 = 0
t2 = 1

player1_score=0
player2_score=0

def play_the_game():
    questions= trivia_game()
    num_questions=len(questions)
    num_players=2
    global player1_score
    global player2_score
    global t1
    global t2
    
    for i in range((num_questions)):
        # Prompt player 1 for their answer
        if t1==0:
            print("player 1 's turn")
            print(questions[i])
            answer1 = int(input("Enter your answer (1-4): "))
            if answer1 == questions[i].correct:
                player1_score += 1
                print("that is correct")
            else:
                print("that is incorrect")
        # Prompt player 2 for their answer
        elif t1==1:
            print("Player 2' turn: ")
            print(questions[i])
            answer2 = int(input("Enter your answer (1-4): "))
            if answer2 == questions[i].correct:
                player2_score += 1
                print('that is correct')
            else:
                print("that is incorrect")

        turn = t1
        t1 = t2
        t2 = turn


play_the_game()
print(f"game over player 1 scored {player1_score} points and player2 scored {player2_score} points")
if player1_score> player2_score:
    print("player 1 won")
elif player1_score== player2_score:
    print("it's a tie")
else:
    print("player 2 won")