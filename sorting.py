import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    numbers = numbers[:]
    for pozice_ukladani in range(len(numbers)):
        min_idx = pozice_ukladani
        for pozice_prohazene in range(pozice_ukladani + 1, len(numbers)):
            if numbers[pozice_prohazene] < numbers[min_idx]:
                min_idx = pozice_prohazene
        numbers[pozice_ukladani], numbers[min_idx] = numbers[min_idx], numbers[pozice_ukladani]
    return numbers



numbers = [5, 1, 4, 2, 8]
print("puvodni seznam:", numbers)
print("novy seznam:", selection_sort(numbers))