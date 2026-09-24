def main_text():
    return f"""
    ====================================
                QUIZ GAME
    ====================================
    """
def display_question(number, q):
    print(f"Question {number}")
    print(f"{q["question"]}")
    for i,option in enumerate(q["options"], start= 0):
        letter = chr(97 + i)
        print(f"{letter}. {option}")

def get_user_answer(q):
    valid_letters = []
    for i in range (len(q["options"])):
        valid_letters.append(chr(97 + i))
    while True:
        user_answer = input("Select your answer: ").strip().lower()
        if len(user_answer)== 1 and user_answer in valid_letters:
            return user_anser
        print("Invalid input, try again") 

def run_quiz(questions):
    score = 0
    for index, i in enumerate(questions, start = 1):
        display_question(index, i)
        answer = get_user_answer(i)
        ind = ord(answer) - 97
        option_text = i["options"][ind]
        if option_text.strip().lower == i["answer"].strip().lower():
            score+=1
            print("Correct")
        else:
            print("Wrong")
    return score





