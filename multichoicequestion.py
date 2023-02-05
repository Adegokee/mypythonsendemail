questions = {
    'What is the capital of France?': 'Paris',
    'What is the capital of Germany?': 'Berlin',
    'What is the capital of Italy?': 'Rome'
}

# Function to display the questions
def display_questions(questions):
    for i, question in enumerate(questions):
        print(i + 1, question)

# Function to check if answer is correct
def check_answer(questions, question, answer):
    correct_answer = questions[question]
    if answer == correct_answer:
        return True
    else:
        return False

# Main program
display_questions(questions)
question = input("Enter the number of the question you want to answer: ")
question = list(questions.keys())[int(question) - 1]
answer = input("Enter your answer: ")
if check_answer(questions, question, answer):
    print("Correct!")
else:
    print("Incorrect. The correct answer is", questions[question])