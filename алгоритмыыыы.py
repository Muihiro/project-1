import random
import string


def get_sort_key(x):

    if x.isdigit():  # Цифры и числа
        return (0, int(x))  # Сортируем по числовому значению
    elif x.isalpha():  # Буквы и слова
        return (1, x.lower())  # Сортируем без учёта регистра
    else:  # Буквосочетания
        return (2, x)

def generate_mixed_array(n=256):
    digits = [str(d) for d in range(10)]  # '0'...'9'
    numbers = [str(random.randint(10, 999)) for _ in range(50)]  # числа 10-999
    letters = random.choices(string.ascii_letters, k=50)  # буквы A-Z a-z
    combos = [
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 4)))
        for _ in range(50)
    ]  # буквосочетания
    words = [
        ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
        for _ in range(56)
    ]  # слова

    all_elements = digits + numbers + letters + combos + words
    random.shuffle(all_elements)
    return all_elements[:n]


def partition_lomuto(arr, low, high):
    pivot = arr[high]
    pivot_key = get_sort_key(pivot)
    i = low - 1

    for j in range(low, high):
        if get_sort_key(arr[j]) <= pivot_key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_lomuto(arr, low, high):
    if low < high:
        pi = partition_lomuto(arr, low, high)
        quicksort_lomuto(arr, low, pi - 1)
        quicksort_lomuto(arr, pi + 1, high)

def partition_hoare(arr, low, high):

    pivot = arr[(low + high) // 2]
    pivot_key = get_sort_key(pivot)
    i = low
    j = high

    while True:
        while get_sort_key(arr[i]) < pivot_key:
            i += 1
        while get_sort_key(arr[j]) > pivot_key:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def quicksort_hoare(arr, low, high):
    if low < high:
        p = partition_hoare(arr, low, high)
        quicksort_hoare(arr, low, p)
        quicksort_hoare(arr, p + 1, high)


def print_sample(arr, title, count=15):
    print(f"\n{title}:")
    print(f" Первые {count}: {arr[:count]}")
    print(f" Последние {count}: {arr[-count:]}")


def main():
    # Генерируем исходный массив
    original = generate_mixed_array(256)
    print_sample(original, "ИСХОДНЫЙ МАССИВ")

    # Копируем для обоих алгоритмов
    arr_lomuto = original.copy()
    arr_hoare = original.copy()

    # Сортировка Ломуто
    print("\n--- Сортировка Ломуто ---")
    quicksort_lomuto(arr_lomuto, 0, len(arr_lomuto) - 1)
    print_sample(arr_lomuto, "РЕЗУЛЬТАТ")


    # Сортировка Хоара
    print("\n--- Сортировка Хоара ---")
    quicksort_hoare(arr_hoare, 0, len(arr_hoare) - 1)
    print_sample(arr_hoare, "РЕЗУЛЬТАТ")



if __name__ == "__main__":
    main()