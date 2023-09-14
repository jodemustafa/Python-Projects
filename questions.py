# jode mustafa
# u41333726
# #This module contain the question class that will contain the proper format of the question and answers
#to use it accordingly in the triva question program

class question:
    def __init__(self,question,answer1,answer2,answer3,answer4, correct_ans):
        self.trivia_question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct= correct_ans


    def __str__(self):
        return f"{self.trivia_question}\n1. {self.answer1}\n2. {self.answer2}\n3. {self.answer3}\n4. {self.answer4}"
    

    