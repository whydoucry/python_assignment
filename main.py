expenses = []


def add_expense(name, category, amount):
    expense = {
        'name': name,
        'category': category,
        'amount': amount
    }
    expenses.append(expense)
    return expense


def show_expenses():
    if not expenses:
        print('\nРасходов пока нет.')
        return

    print('\n--- Все расходы ---')
    for number, expense in enumerate(expenses, start=1):
        print(f'{number}. {expense["name"]} | {expense["category"]} | {expense["amount"]:.2f} руб.')


def calculate_total():
    return sum(expense['amount'] for expense in expenses)


def show_statistics():
    if not expenses:
        print('\nНет данных для статистики.')
        return

    statistics = {}

    for expense in expenses:
        category = expense['category']
        statistics[category] = statistics.get(category, 0) + expense['amount']

    print('\n--- Статистика расходов ---')
    for category, amount in statistics.items():
        print(f'{category}: {amount:.2f} руб.')

    print(f'Всего потрачено: {calculate_total():.2f} руб.')


def main():
    while True:
        print('\n=== МЕНЕДЖЕР ЛИЧНЫХ РАСХОДОВ ===')
        print('1. Добавить расход')
        print('2. Посмотреть все расходы')
        print('3. Посмотреть общую сумму расходов')
        print('4. Посмотреть статистику')
        print('0. Выход')

        choice = input('\nВыберите действие: ')

        if choice == '1':
            name = input('Название расхода: ').strip()
            category = input('Категория: ').strip()

            try:
                amount = float(input('Сумма (руб.): '))
                if not name or not category or amount <= 0:
                    print('Ошибка: заполните все поля, сумма должна быть больше нуля.')
                    continue

                add_expense(name, category, amount)
                print('Расход успешно добавлен!')

            except ValueError:
                print('Ошибка: сумма должна быть числом.')

        elif choice == '2':
            show_expenses()

        elif choice == '3':
            print(f'\nОбщая сумма расходов: {calculate_total():.2f} руб.')

        elif choice == '4':
            show_statistics()

        elif choice == '0':
            print('До свидания!')
            break

        else:
            print('Неизвестная команда. Попробуйте ещё раз.')


if __name__ == '__main__':
    main()