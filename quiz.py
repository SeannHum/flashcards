# Quiz logic
import random
from file_utils import load_categories

FILENAME = "flashcards.csv"

def quiz_user(flashcards):
    # pick cards, shuffle, track score
    categories = load_categories(FILENAME)

    print(f"\nSelect a category:")
    print("1. All flashcards")

    for category in categories:
        print(f"{categories.index(category) + 2}. {category}")

    while True:
        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid option. Please try again.")
        else:
            if 1 <= choice <= len(categories) + 1:
                break
            else:
                print("Invalid option. Please try again.")

    if choice == 1:
        while True:
            try:
                questions = int(input(f"\nHow many questions?: "))
            except ValueError:
                print("Invalid number. Please try again.")
            else:
                if questions > 0:
                    break
                else:
                    print("Invalid number. Please try again.")

        done_questions = 0
        correct_questions = 0

        while done_questions < questions:
            random_flashcard = random.choice(flashcards)

            print(f"\nQuestion: {random_flashcard['question']}")
            quiz_answer = input("Answer: ")

            if quiz_answer == random_flashcard["answer"]:
                print(f"\nCorrect!")
                done_questions += 1
                correct_questions += 1
            else:
                print(f"\nWrong! Correct answer: {random_flashcard['answer']}")
                done_questions += 1

        print(f"Score: {correct_questions}/{questions}")

    elif 2 <= choice <= len(categories) + 1:
        category = categories[choice - 2]

        flashcards_category = []

        for flashcard in flashcards:
            if flashcard["category"] == category:
                flashcards_category.append(flashcard)

        if not flashcards_category:
            print(f"No flashcards in {category}!\n")

            quiz_user(flashcards)

        while True:
            try:
                questions = int(input(f"\nHow many questions?: "))
            except ValueError:
                print("Invalid number. Please try again.")
            else:
                if questions > 0:
                    break
                else:
                    print("Invalid number. Please try again.")

        done_questions = 0
        correct_questions = 0

        while done_questions < questions:
            random_flashcard = random.choice(flashcards_category)

            print(f"\nQuestion: {random_flashcard['question']}")
            quiz_answer = input("Answer: ")

            if quiz_answer == random_flashcard["answer"]:
                print(f"\nCorrect!")
                done_questions += 1
                correct_questions += 1
            else:
                print(f"\nWrong! Correct answer: {random_flashcard['answer']}")
                done_questions += 1

        print(f"Score: {correct_questions}/{questions}")
