from experta import *

class StudentFacts(Fact):
    pass


class CareerExpertSystem(KnowledgeEngine):

    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("\nSuggested Career Path: Mechanical Engineering")
        print("Subjects: Maths, Physics, Mechanics, Thermodynamics")

    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("\nSuggested Career Path: Computer Engineering")
        print("Subjects: Programming, Data Structures, DBMS, Networks")

    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("\nSuggested Career Path: Biotechnology")
        print("Subjects: Biology, Chemistry, Genetics, Microbiology")

    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("\nSuggested Career Path: Electronics Engineering")
        print("Subjects: Circuits, Electronics, Signals, Communication")

    @Rule(StudentFacts(likes='Programming'),
          StudentFacts(likes='Maths'),
          StudentFacts(likes='AI'))
    def aids(self):
        print("\nSuggested Career Path: AI & DS")
        print("Subjects: Python, Mathematics, Machine Learning, Data Science, AI")


def main():
    engine = CareerExpertSystem()
    engine.reset()

    print("Welcome to the Career Path Expert System!\n")

    print("Available Interests:")
    print("Maths, Physics, Programming, Biology, Chemistry, Circuits, AI\n")

    interests = input("Enter your interests separated by commas: ").split(',')

    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))

    engine.run()


if __name__ == "__main__":
    main()
