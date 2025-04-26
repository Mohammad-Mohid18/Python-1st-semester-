quiz = {
    '1.  Contitnents in the world?' : '7',
    '2.  Largest Planet?' : 'jupiter',
    '3.  Gas that plants breath':'carbon dioxide',
    '4.  5 + 3' : '8',
    '5.  legs of spiders':'8'
}

options = {
    '1.  Contitnents in the world?' : ['5', '6', '7', '8'],
    '2.  Largest Planet?' : ['jupiter', 'saturn', 'neptune', 'pluto'],
    '3.  Gas that plants breath':['carbon dioxide','oxygen','helium','water'],
    '4.  5 + 3' : ['8', '9', '10', '11'],
    '5.  legs of spiders':['8', '9', '10', '11'],
}

score = 0

for question, answers in quiz.items():
    print (question)
    option_list = options[question]
    for i in range(len(option_list)):
       print(f'{i+1}. {option_list[i]}')

    user_answer = int(input('enter the number of the answer you want to select (1-4):'))
    if user_answer > len(option_list):
        print('Invalid input. Please enter a number between 1 and 4.')
        continue

    if option_list[user_answer - 1].lower() == answers.lower():
        score += 1
        print('correct!')
    else:
        print('wrong!')
        print(f'The correct answer is {answers}')


    print(f'Your score score is',score)