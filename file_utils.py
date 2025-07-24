# load and save flashcards from CSV
import csv

def load_flashcards(filename):
    # read CSV and return a list of dicts
    flashcards = []

    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            flashcards.append(row)

    return flashcards


def save_flashcards(flashcards, filename):
    # save dicts in list to csv
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["question", "answer", "category"])

        writer.writeheader()

        for flashcard in flashcards:
            writer.writerow({"question": flashcard["question"], "answer": flashcard["answer"], "category": flashcard["category"]})

def load_categories(filename):
    # read categories from csv and return a list of such with no repetition

    categories = []
    seen_categories = set()

    with open(filename) as file:
        reader = csv.DictReader(file)
        for flashcard in reader:
            if flashcard["category"] not in seen_categories:
                categories.append(flashcard["category"])
                seen_categories.add(flashcard["category"])

    return categories


