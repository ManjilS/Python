# print("Welcome to the quiz game !!!")

# user_choice=input("Do you want to play ? ")
# if(user_choice.lower()=="yes"):
#     print("Let's play the game")
# else:
#     exit()


print("Welcome to the quiz game !!!")

user_choice=input("Do you want to play ? ")
if(user_choice.lower()=="yes"):
    print("Let's play the game")
    # Few lines of code before the cursor
    questions = [
        {'question': 'Question for Rs 1000\nWhat is the capital of France?', 'options': ['Paris', 'Berlin', 'Madrid', 'London'], 'answer': '1'},
        {'question': 'Question for Rs 2000\nWhat is the largest planet in our solar system?', 'options': ['Jupiter', 'Saturn', 'Uranus', 'Neptune'], 'answer': '1'},
        {'question': 'Question for Rs 4000\nWho wrote the novel "Pride and Prejudice"?', 'options': ['Jane Austen', 'Charles Dickens', 'George Eliot', 'William Shakespeare'], 'answer': '1'},
        {'question': 'Question for Rs 10000\nWhat is the chemical symbol for gold?', 'options': ['Au', 'Ag', 'Pt', 'Hg'], 'answer': '1'},
        {'question': 'Question for Rs 50000\nWhich country is known as the "Land of the Rising Sun"?', 'options': ['Japan', 'China', 'Korea', 'Vietnam'], 'answer': '1'}
    ]
    amount=[1000,2000,4000,10000,50000]
    score = 0
    i=0
    for question in questions:
        
             print(question['question'])
             print(question['options'])
             user_answer = input("Enter your answer(1,2,3,4) or Quit: ")
             if(user_answer.lower()=="quit"):
                print("Your won Rs ",score,"\n")
                quit()
             if user_answer == question['answer']:
                print("Correct!\n")
                score=amount[i]
                i+=1
             else:
                print("You won Rs",score)
                quit()
            

    print("Your won Rs ",score,"\n")
else:
    exit()