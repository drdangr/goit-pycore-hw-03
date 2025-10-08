import random

def get_numbers_ticket(min_value, max_value, quantity):
    
        
    # Перевірка типів даних
    if not all(isinstance(i, int) for i in [min_value, max_value, quantity]):
        return []

    # Перевірка значень
    if min_value >= max_value:
        return []
    if quantity <= 0:
        return []
    if quantity > (max_value - min_value + 1):
        return []
    if min_value < 1 or max_value < 1:
        return []
    if max_value > 1000:
        return []
   
    numbers = random.sample(range(min_value, max_value + 1), quantity) 
    numbers.sort()

    return numbers


# --- приклади ---
print(get_numbers_ticket(1, 49, 6))      #  → [3, 15, 22, 28, 37, 44] (наприклад)
print(get_numbers_ticket(-10, 10, 5))    #  → []
print(get_numbers_ticket(1000, 1200, 10))#  → []
print(get_numbers_ticket(10, 4, 5))      #  → []
print(get_numbers_ticket(10, 14, 6))     #  → []