"""

"""
class QuizGame:
    score = 0
    question_number = 0

    def __init__(self, questions):
        self.questions = questions

    @classmethod
    def set_question_number(cls):
        cls.question_number += 1 

    def start_game(self):
        question_list = self.questions.items()
        for question in question_list:
            self.set_question_number()
            answer = input(f"{self.question_number},  {question[0]} :")
            if answer == str(question[1]):
                self.score += 1
                print("Correct!")
        return self.score
              
questions = {
    "The Sun rises in the East": True,
    "Surafel's father name is Abebe": False,
    "Girls love to eat": True,
    "I hate Python": False,
    "Surafel is a Django Developer": True,
    "Python lists are immutable": False
}

if __name__ == "__main__":
    print("---------- Quiz started ----------")
    print("- Answer the following question by writing 'True' or 'False'")
    game = QuizGame(questions)
    result = game.start_game()
    print(" Your result is {} out of {} qestions".format(result, len(questions)))
    print("---------- Quiz Ended ----------")