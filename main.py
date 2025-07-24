# main.py
from file_utils import load_flashcards, save_flashcards
from flashcard_ops import add_flashcard, view_flashcards, edit_flashcard, delete_flashcard
from quiz import quiz_user
import sys

FILENAME = "flashcards.csv"

def main():
    flashcards = load_flashcards(FILENAME)

    while True:
        print("\nFlashcards Menu")
        print("1. View flashcards")
        print("2. Add flashcard")
        print("3. Edit flashcard")
        print("4. Delete flashcard")
        print("5. Quiz mode")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            view_flashcards(flashcards)
        elif choice == "2":
            add_flashcard(flashcards)
        elif choice == "3":
            edit_flashcard(flashcards)
        elif choice == "4":
            delete_flashcard(flashcards)
        elif choice == "5":
            quiz_user(flashcards)
        elif choice == "6":
            save_flashcards(flashcards, FILENAME)
            sys.exit(f"\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
