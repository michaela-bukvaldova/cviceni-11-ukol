import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    numbers = numbers[:]
    for pozice_ukladani in range(len(numbers)):
        min_idx = pozice_ukladani
        for pozice_prochazene in range(pozice_ukladani + 1, len(numbers)):
            if numbers[pozice_prochazene] < numbers[min_idx]:
                min_idx = pozice_prochazene
        numbers[pozice_ukladani], numbers[min_idx] = numbers[min_idx], numbers[pozice_ukladani]
    return numbers

def bubble_sort(numbers):
    numbers = numbers[:]
    for serazeno_od_konce in range(len(numbers)):
        has_changed = False
        print(serazeno_od_konce)
        for pozice_porovnani in range(len(numbers) - 1 - serazeno_od_konce):
            if numbers[pozice_porovnani] > numbers[pozice_porovnani + 1]:
                has_changed = True
                numbers[pozice_porovnani], numbers[pozice_porovnani + 1] = numbers[pozice_porovnani + 1]
            if not has_changed:
                break
    return numbers




numbers = random_numbers(20)
print("puvodni seznam:", numbers)
print("novy seznam:", bubble_sort(selection_sort(numbers)))