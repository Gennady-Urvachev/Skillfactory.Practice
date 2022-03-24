array = [int(x) for x in input("Введите последовательность чисел через пробел: ").split()]


def sorted_array():
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


user_number = int(input('Введите одно число из ранее введенных, кроме максимального или минимального: '))

print(sorted_array())

if user_number <= min(array) or user_number >= max(array):
    print('Введенное число не соответствует требованиям')
elif user_number not in array:
    print('Введенное число не соответствует требованиям')
else:
    user_number_idx = binary_search(array, user_number, 0, len(array))
    print(user_number_idx - 1)






































































































































































