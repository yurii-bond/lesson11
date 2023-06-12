a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_sorted(_list):
    empty_list = []
    for i in _list:
        if i < 5:
            empty_list.append(i)
    return empty_list


b = [x for x in a if x < 5]

x = [x for x in range(1, 10) if x < 5]
print(f'x: {x}')

print(get_sorted(a))
print(b)

message = input('Input: ')
vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U', 'y', 'Y']
formatted_message_list = ['' if ch in vowels else ch for ch in message]
joined_list = ''.join(formatted_message_list)
print('Output: {}'.format(joined_list))
print('Output: {}'.format(''.join(['' if ch in vowels else ch for ch in message])))

