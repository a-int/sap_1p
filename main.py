import random
import argparse

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=int, help="Искомое значение")
    args = parser.parse_args()
    arr = sorted(random.randint(0, 200) for _ in range(100))
    print("Сгенерированный отсортированный массив:")
    print(arr)
    print(f"\nПоиск значения: {args.target}")
    result = binary_search(arr, args.target)
    if result != -1:
        print(f"Найдено на индексе: {result}")
    else:
        print("Значение не найдено.")

