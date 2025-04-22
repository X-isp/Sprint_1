# Напишите функцию, которая принимает строку и проверяет, является ли переданная строка палиндромом.
# Если полученная строка — палиндром, функция должна вернуть True, в ином случае — False.
# Задачу необходимо решить с применением срезов.
# На вход подается строка из букв или цифр, без знаков препинания, содержащая только пробелы,
# при решении регистр не учитывается.
from netaddr.strategy.ipv6 import str_to_int


def is_palindrome_improved(str_input): # Улучшенный вариант
    str_palindrome = str_input.replace(' ','').lower()  # получение строки без пробелов
    palindrome_length = len(str_palindrome)             # определение длины строки
    center_idx = (palindrome_length - 1) // 2          # нахождение среднего символа в строке

    # создание реверсивного индекса, учитывающего четное количество символов в строке или нет + применение тернарного оператора
    idx_shift = (0 if palindrome_length % 2 != 0 else 1)       # нечетная длина строки   => indx_shift = 0
                                                                # четная длина строки     => indx_shift = 1
    return str_palindrome[:center_idx + idx_shift] == str_palindrome[center_idx + 1:][::-1]

    # Варианты вывода return
    # 1. if/else:
    # if str_palindrome[:center_idx + idx_shift] == str_palindrome[center_idx + 1:][::-1]:
    #     return True
    # else:
    #     return False

    # 2. Тернарный оператор:
    # return True if str_palindrome[:center_idx + idx_shift] == str_palindrome[center_idx + 1:][::-1] else False

    # 3. Просто написать выражение и Python вернет вариант выражения через True/False
    # return str_palindrome[:center_idx + idx_shift] == str_palindrome[center_idx + 1:][::-1]


def is_palindrome(str_input): # Вариант работает, однако функцию возможно переписать оптимальнее
    str_palindrome = str_input.replace(' ', '').lower()
    if len(str_palindrome) % 2 != 0:
        num = (len(str_palindrome) - 1) // 2
        str_palindrome = str_palindrome.replace(str_palindrome[num], '')

    middle = (len(str_palindrome) - 1) // 2
    second = str_palindrome[middle + 1:]

    if str_palindrome[:middle + 1] == second[::-1]:
        return True
    else:
        return False

def main():
    print(f'Работа функции: is_palindrome')
    # Должно быть напечатано True:
    print(is_palindrome('А роза упала на лапу Азора'))
    # Должно быть напечатано False:
    print(is_palindrome('Не палиндром'))

    print(f'\nРабота функции: is_palindrome_improved')
    # Должно быть напечатано True:
    print(is_palindrome_improved('А роза упала на лапу Азора'))
    # Должно быть напечатано False:
    print(is_palindrome_improved('Не палиндром'))


if __name__ == '__main__':
    main()