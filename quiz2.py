# Quiz task :

quiz = {
    'there are how many wonder of the world': {'5,6,7,8' : '7'},
    'the largest continent is': {'asia,europe,africa': 'asia'},
    'the largest mounntain is':{'k2, mount-everest': 'mount-everest'}
}


def add_question(question,options,answer):
    if question in quiz:
        print(f'Question {question} already exists.')
    else:
        quiz[question] = {options: answer}
        print(f'Question {question} added successfully with options: {options} and answer: {answer}')


def remove_question(question):
    if question in quiz:
        del quiz[question]
        print(f'Question {question} removed successfully.')
    else:
        print(f'Question {question} not found.')


for question, options in quiz.items():
    for option_list,answer in options.items():
        print(f'question:{question}')
        print(f'Options: {option_list}')
        user_answer = input('Enter the answer: ')
        if user_answer.lower() == answer.lower():
            print('Correct!')
        else:
            print(f'Wrong! The correct answer is {answer}')