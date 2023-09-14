# jode mustafa
# u41333726
#this module import the class fom QuestionClass module and contains the list of all trivia question
#the program then apply all the questions in the list to the Question class 

from questions import question

def trivia_game():
    Questions = [

    question("How many days are in a lunar year?", "354","365","243","379",1 ),
    question("What is the largest planet?", 'mars','jupiter','earth','pluto', 2 ),
    question('What is the largest kind of whale?','orca whale','humpback whale','beluga whale', 'blue whale',4),
    question('Which dinosaur could fly?','triceratops', 'tyrannosaurus rex', 'pternadon','diplodocous',3 ),
    question('Which of these Winnie the Pooh characters is a donkey?','pooh', 'eeyore','piglet','kanga',2 ),
    question('What is the hottest planet?','mars','pluto','earth','venus',4 ),
    question('Which dinosaur had the largest brain compared to body size?','troodon','stegoasaurus','ichthyosaurus','gigantoraptor',1 ),
    question('What is the largest type of penguins?', 'chinstrap penguins','macaroni penguins','emperor penguins','white flippered penguins',3),
    question("Which children's story character is a monkey?",'winnie the poo','curious george', 'horton','goofy', 2),
    question("How long is a year on Mars?",'550','498','126','687',4)
    ]
    return Questions




