question = 'Что лучше Питон или С#?'
riddle_1_answer = 'питон'
request = int(input(question))


count = 0



if riddle_1_answer == request:
    count += 1
    print('Да вы правы!')
else:
    print('Нет, вы не правы!')


