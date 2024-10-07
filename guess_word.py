questions = [
    {'question': 'anfrec',  'answer': 'france'},
    {'question': 'anmilj',  'answer': 'manjil'},
    {'question': 'shta',    'answer': 'stha'},
    {'question': 'alpep',   'answer': 'apple'},
    {'question': 'ogmna',   'answer': 'mango'}
]
score = 0
life = 3

for question in questions:
    while life > 0:
        print(f"You have {life} lives remaining")
        print(question['question'])
        user_answer = input("Enter your answer or type 'quit' to exit: ").strip()

        if user_answer.lower() == "quit":
            print("Exiting the game.")
            break

        if user_answer.lower() == question['answer'].lower():
            print("Correct!\n")
            score += 1
            break  # Move to the next question once the correct answer is given
        else:
            print("Incorrect!\n")
            life -= 1

        if life == 0:
            print(f"Out of lives! The correct answer is: {question['answer']}\n")
            break

    if life == 0:  # End the game if lives reach 0
        break
print(f"Your score is {score}")
print(f"--------- GAME OVER --------")
