import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    if min >= 1 and max <= 1000 and (max - min + 1) >= quantity:
        numbers = set()

        while len(numbers) < quantity:
            number = random.randint(min, max)
            numbers.add(number)

        return sorted(list(numbers))
    else:
        return []

# Test
print(get_numbers_ticket(10, 20, 5)) # [10, 11, 15, 18, 20] (it`s random)