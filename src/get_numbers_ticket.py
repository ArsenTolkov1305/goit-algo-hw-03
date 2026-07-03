import random


def get_numbers_ticket(min: int, max: int, quantity: int):
    if min >= 1 and max <= 1000 and min <= quantity <= (max - min + 1):
        numbers = set()

        while len(numbers) < quantity:
            number = random.randint(min, max)
            numbers.add(number)

        return sorted(list(numbers))
    else:
        return []

# Test
print(get_numbers_ticket(1, 49, 6)) # [15, 21, 26, 35, 44, 49] (it`s random)