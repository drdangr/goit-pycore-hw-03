def get_numbers_ticket(min, max, quantity):
    import random
        
    if min >= max:
        raise ValueError("Minimum must be less than maximum.")
    if quantity > (max - min + 1):
        raise ValueError("Quantity exceeds the range of unique numbers available.")
    if quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")
    if min < 0 or max < 0:
        raise ValueError("Min and Max must be non-negative integers.")
    if not all(isinstance(i, int) for i in [min, max, quantity]):
        raise TypeError("Min, Max, and Quantity must be integers.")
    if max > 1000:
        raise ValueError("Max value should not exceed 1000.")
    if min < 1:
        raise ValueError("Min value should be more 1")
   
    numbers = random.sample(range(min, max + 1), quantity) 
    numbers.sort()
    
    return numbers


print("Your lottery numbers are:", get_numbers_ticket(1, 50, 5))
