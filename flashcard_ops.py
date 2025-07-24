# view, add, edit, delete flashcards
from file_utils import save_flashcards, load_categories

FILENAME = "flashcards.csv"

def view_flashcards(flashcards):
    # category selection
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
        # print all flashcards
        for flashcard in flashcards:
            print(f"----------------------------------------------")
            print(f"Question: {flashcard['question']}")
            print(f"Answer: {flashcard['answer']}")
            print(f"Category: {flashcard['category']}")

    elif 2 <= choice <= len(categories) + 1:
        category = categories[choice - 2]

        for flashcard in flashcards:
            if flashcard["category"] == category:
                print(f"----------------------------------------------")
                print(f"Question: {flashcard['question']}")
                print(f"Answer: {flashcard['answer']}")

#----------------------------------------------------------------------------------------------------
def add_flashcard(flashcards):
    # ask user for question, answer, etc
    categories = load_categories("flashcards.csv")

    print(f"\nSelect a category:")
    print("1. New category")

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
        new_category = input(f"\nNew category: ")
        new_question = input("New question: ")
        new_answer = input("New answer: ")

        flashcards.append({"question": new_question, "answer": new_answer, "category": new_category})
        save_flashcards(flashcards, FILENAME)

        print(f"\nCreated!")

    elif 2 <= choice <= len(categories) + 1:
        category = categories[choice - 2]

        new_question = input(f"\nNew question: ")
        new_answer = input("New answer: ")

        flashcards.append({"question": new_question, "answer": new_answer, "category": category})
        save_flashcards(flashcards, FILENAME)

        print(f"\nCreated!")
#-----------------------------------------------------------------------------------------
def edit_flashcard(flashcards):
    # change an existing card
    for flashcard in flashcards:
        print(f"--------------------{flashcards.index(flashcard) + 1}--------------------------")
        print(f"Question: {flashcard['question']}")
        print(f"Answer: {flashcard['answer']}")
        print(f"Category: {flashcard['category']}")

    while True:
        try:
            choice = int(input(f"\nSelect an option: "))
        except ValueError:
            print("Invalid option. Please try again.")
        else:
            if 1 <= choice <= len(flashcards):
                break
            else:
                print("Invalid option. Please try again.")

    print(f"1. Question: {flashcards[choice - 1]['question']}")
    print(f"2. Answer: {flashcards[choice - 1]['answer']}")
    print(f"3. Category: {flashcards[choice - 1]['category']}")

    while True:
        try:
            choice_2 = int(input(f"\nSelect an option: "))
        except ValueError:
            continue
        else:
            if 1 <= choice_2 <= 3:
                break

    if choice_2 == 1:
        new_question = input(f"\nWhat is the new question? ")

        flashcards[choice - 1]["question"] = new_question
        save_flashcards(flashcards, FILENAME)

        print(f"\nEdited!")

    elif choice_2 == 2:
        new_answer = input(f"\nWhat is the new answer? ")

        flashcards[choice - 1]["answer"] = new_answer
        save_flashcards(flashcards, FILENAME)

        print(f"\nEdited!")

    elif choice_2 == 3:
        categories = load_categories("flashcards.csv")

        print(f"\n1. New category")

        for category in categories:
            print(f"{categories.index(category) + 2}. {category}")

        while True:
            try:
                choice_3 = int(input("Select an option: "))
            except ValueError:
                print("Invalid option. Please try again.")
            else:
                if 1 <= choice_3 <= len(categories) + 1:
                    break
                else:
                    print("Invalid option. Please try again.")

        if choice_3 == 1:
            # new category to flashcard
            print()
            new_category = input("New category: ")

            flashcards[choice - 1]["category"] = new_category
            save_flashcards(flashcards, FILENAME)

            print(f"\nEdited!")

        else:
            # previous category to flashcard
            flashcards[choice - 1]["category"] = categories[choice_3 - 2]
            save_flashcards(flashcards, FILENAME)

            print(f"\nEdited!")
#-----------------------------------------------------------------------------------------
def delete_flashcard(flashcards):
    # delete existing flashcard
    for flashcard in flashcards:
        print(f"--------------------{flashcards.index(flashcard) + 1}--------------------------")
        print(f"Question: {flashcard['question']}")
        print(f"Answer: {flashcard['answer']}")
        print(f"Category: {flashcard['category']}")

    while True:
        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid option. Please try again.")
        else:
            if 1 <= choice <= len(flashcards):
                flashcards.remove(flashcards[choice - 1])
                save_flashcards(flashcards, FILENAME)

                print(f"\nRemoved!\n")
                break
            else:
                print("Invalid choice. Please try again.")
