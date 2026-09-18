print('Привет, новый пользователь FitLife MVP!')
user_name = input('Введи, пожалуйста, своё имя: ')
user_age = int(input('Введи, пожалуйста, свой возраст: '))
try:
    user_weight = float(input('Введи, пожалуйста, свой вес: '))
except ValueError:
    print('Вместо знака "," поставте знак "."')
    user_weight = float(input('Введи, пожалуйста, свой вес корректно: '))
try:
    user_height = float(input('Введи, пожалуйста, свой рост: '))
except ValueError:
    print('Вместо знака "," поставте знак "."')
    user_height = float(input('Введи, пожалуйста, свой рост корректно: '))
bmi = round(user_weight / (user_height ** 2), 1)  # Расчёт индекса массы тела
WATER_FOR_KG = 30
ML_IN_L = 1000
water_ml = round(user_weight * WATER_FOR_KG, 1)  # Расчёт нормы воды
water_l = water_ml / ML_IN_L  # Перевод нормы из мл. в л.

print()
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')
