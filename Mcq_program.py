# Creating a class for multiple choice exam questions.Each class object has attribute "question" and "answer"

class Mcq:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


# Creating a list of every question

test = [
    "1.How many sides has a triangle?\n (a) 1\n (b) 2\n (c) 3\n\n",
    "2.How many sides has a rectangle?\n (a) 3\n (b) 4\n (c) 5\n\n",
    "3.How many sides has a hexagon?\n (a) 1\n (b) 5\n (c) 6\n\n",
    "4.What is the total internal angle of a Triangle?\n (a) 120\n (b) 180\n (c) 360\n\n",
    "5.A square has the same sides as a rectangle?\n (a) True\n (b) False\n (c) None\n\n",
]

# Creating a list that contains object of the class with attributes to serve as a marking scheme

marking_scheme = [
    Mcq(test[0], "c"),
    Mcq(test[1], "b"),
    Mcq(test[2], "c"),
    Mcq(test[3], "b"),
    Mcq(test[4], "a")
]

#Defining function that marks test with the marking scheme

def mark_script(marking_scheme):
    print("\n\nEND OF SEMESTER EXAMS\nType the letter that corresponds to your answer!!\n\n")
    score = 0

    for obj in marking_scheme:
        answer = input(obj.question)
        if answer == obj.answer:
            score += 1

    print("\nYou got " + str(score) + "/" + str(len(test)) + " correct!")

    if score < 3:
        print("Sorry you need to take the exam again!!")
    else:
        print("Congratulations, you can proceed to the next class")


mark_script(marking_scheme)





