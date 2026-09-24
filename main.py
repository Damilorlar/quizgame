import random
from utils import run_quiz, main_text

questions=[
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Saturn", "Jupiter", "Mars"],
        "answer": "Jupiter"
    },
    {
        "question": "How many continents are there?",
        "options": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "O2", "CO2", "NaCl"],
        "answer": "H2O"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is 9 x 3?",
        "options": ["21", "27", "24", "18"],
        "answer": "27"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Seoul", "Beijing", "Tokyo", "Bangkok"],
        "answer": "Tokyo"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What is 2 + 3?",
        "options": ["3", "4", "5", "6"],
        "answer": "5"
    },
    {
        "question": "What is 1 + 5?",
        "options": ["3", "4", "5", "6"],
        "answer": "6"
    },
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Rome", "Berlin"],
        "answer": "Paris"
    }


]
print(main_text())
picked =random.sample(questions, 5)
final_score = run_quiz(picked)
print(f"Your final score is {final_score} out of {len(questions)}")