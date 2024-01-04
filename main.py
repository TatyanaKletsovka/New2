# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2  # Находим середину массива
#
#         if arr[mid] == target:
#             return mid  # Элемент найден, возвращаем его индекс
#         elif arr[mid] < target:
#             left = mid + 1  # Поиск в правой половине
#         else:
#             right = mid - 1  # Поиск в левой половине
#
#     return -1  # Элемент не найден
#
# # Пример использования
# sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target_element = 7
#
# result = binary_search(sorted_array, target_element)
#
# if result != -1:
#     print(f"Элемент {target_element} найден по индексу {result}")
# else:
#     print(f"Элемент {target_element} не найден в массиве")


# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         # Проход по массиву
#         for j in range(0, n - i - 1):
#             # Сравнение и обмен элементов, если нужно
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#
#
# # Пример использования
# my_array = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(my_array)
# print("Отсортированный массив:", my_array)

# def bubble_sort(arr):
#     sorted = False
#     n = len(arr)
#
#     while not sorted:
#         sorted = False
#         i = 0
#         # Проход по массиву
#         for j in range(0, n - i - 1):
#             # Сравнение и обмен элементов, если нужно
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 sorted = True
#         i += 1
#
#
# # Пример использования
# my_array = [64, 34, 25, 12, 22, 11, 90]
# bubble_sort(my_array)
# print("Отсортированный массив:", my_array)

# def selection_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         # Находим минимальный элемент в оставшейся части массива
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#
#         # Меняем найденный минимальный элемент с текущим
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#
#
# # Пример использования
# my_array = [64, 34, 25, 12, 22, 11, 90]
# selection_sort(my_array)
# print("Отсортированный массив:", my_array)


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Перемещение элементов массива, которые больше key, на одну позицию вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставка key в правильное место
        arr[j + 1] = key


# Пример использования
my_array = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_array)
print("Отсортированный массив:", my_array)


# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         i = j = k = 0
#
#         # Слияние двух подмассивов
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         # Обработка оставшихся элементов в подмассивах
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#
# # Пример использования
# my_array = [64, 34, 25, 12, 22, 11, 90]
# merge_sort(my_array)
# print("Отсортированный массив:", my_array)
