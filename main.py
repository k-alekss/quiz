import time

questions = {
    'Сколько планет в Солнечной системе?': '8',
    'Столица Франции?': 'Париж'
}

score = 0
for q, a in questions.items():
    start_time = time.time()
    user_answer = input(q + ' ')
    stop_time = time.time()
    if round(stop_time - start_time, 1) > 5:
        print('Вы не уложились в 5 секунд.')
        user_answer = 'wrong'
    print(f'Время ответа: {round(stop_time - start_time, 1)} секунд.')
    if user_answer.lower() == a.lower():
        print('Правильно!')
        score += 1
    else:
        print('Неверно')

print(f'Ваш результат: {score} из {len(questions)}')