from decimal import Decimal
from datetime import datetime, date, timedelta

#     items — словарь, который хранит список продуктов (goods).
#     title — название добавляемого продукта, строка. Может содержать пробелы.
#     amount — количество добавляемого продукта.
#     expiration_date — срок годности добавляемого продукта, строка в формате %Y-%m-%d, например '2023-9-30'. Это необязательный параметр.
#
# Функция добавляет в словарь goods новые данные и не возвращает никакого значения.
#
# str.split(vegetables, '; ')

def add(items, title, amount, expiration_date=None):
    items.setdefault(title,list()) # метод dict.setdefault(key, default).
                                   # Этот метод Python добавит пару ключ-значение в случае, если она ещё не существует.

    # берем количество и дату годности продукта и добавляем в словарь
    date = (datetime.date(datetime.strptime(expiration_date, '%Y-%m-%d')) if expiration_date is not None else None)
    characteristics_dict = {'amount': Decimal(amount), 'expiration_date': date}

    items[title].append(characteristics_dict)
    #return print(items)


def add_by_note(items, note):
    lst_for_goods = str.split(note, ' ') # преобразуем строку в словарь
    str_length = len(lst_for_goods)
    if note[-3] == '-':
        title = ' '.join(lst_for_goods[:str_length - 2])
        amount = lst_for_goods[-2]
        expiration_date = lst_for_goods[-1]
    else:
        title = ' '.join(lst_for_goods[:str_length - 1])
        amount = lst_for_goods[-1]
        expiration_date = None

    add(items, title, amount, expiration_date)

# Функция должна вернуть названия продуктов, которые содержат искомую строку. Найденные названия должны вернуться в виде списка.
def find(items, needle):
    lst_keys_of_items = items.keys()
    needle_lst = []
    for key in lst_keys_of_items:
        if needle.lower() in key.lower():
            needle_lst.append(key)
            return needle_lst

# Функция возвращает общее количество запрошенного продукта — число типа Decimal.
def get_amount(items, needle):
    lst_found_products = find(items, needle)
    dct = {}
    for product in lst_found_products:
        if product in items.keys():
            cnt_amount = 0
            for parameter in items[product]:
                cnt_amount += parameter['amount']
            dct[product] = cnt_amount

    return sum(dct.values())


def get_expired(items, in_advance_days=0):
    today = date(2023, 12, 10)
    term = today + timedelta(days=in_advance_days)
    lst_overdue = []
    for i in items:
        cnt = 0
        for j in items[i]:
            if j['expiration_date'] is not None and (j['expiration_date'] <= term):
                cnt += j['amount']
                lst_overdue.append((i, cnt))

                # print(type (j['expiration_date'] + today))

            # elif j['expiration_date'] is not None and (j['expiration_date'] - today) <= in_advance_days:
            #     tpl_overdue.append((i, j['amount']))
    lst_answer = []
    for item in lst_overdue:
        sm = 0
        for j in item:
           print(j)


    return lst_overdue


def main():
    goods = {
        'Хлеб': [
            {'amount': Decimal('1'), 'expiration_date': None},
            {
                'amount': Decimal('1'),
                'expiration_date': date(2023, 12, 9)
            }
        ],
        'Яйца': [
            {
                'amount': Decimal('2'),
                'expiration_date': date(2023, 12, 12)
            },
        ],
        'Яйца свежие': [
             {
                'amount': Decimal('2'),
                'expiration_date': date(2023, 12, 12)
                },
            {
                'amount': Decimal('3'),
                'expiration_date': date(2023, 12, 11)
            }
        ],
        'Вода': [{'amount': Decimal('100'), 'expiration_date': None}]
    }
    # goods = {}
    # add(goods, 'Пельмени Универсальные', Decimal('2'), '2023-10-28')
    #
    # add(goods, 'Яйца', Decimal('1'), '2023-10-15')
    # add(goods, 'Яйца', Decimal('10'), '2023-9-30')
    # add(goods, 'Вода', Decimal('2.5'))
    # add(goods, 'Пельмени Универсальные', Decimal('5'), '2023-10-28')
    #
    # add_by_note(goods, 'Яйца свежие гусиные 4.55 2023-07-15')
    # add_by_note(goods, 'Яйца свежие гусиные 5 2023-07-15')
    # add_by_note(goods, 'Вода 4.55')

    #print(goods)

    # print(find(goods, 'огурец'))
    # print(get_amount(goods, 'Яйц'))



    # print(get_expired(goods))
    # print(get_expired(goods, 1))
    print(get_expired(goods, 2))



if __name__ == '__main__':
    main()