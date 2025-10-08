#user input validation for date
from datetime import datetime, date

def get_days_from_today(date_str: str) -> int:
    
    #Приймає дату у форматі 'YYYY-MM-DD' і повертає кількість днів від цієї дати до поточної.
    #Якщо задана дата пізніша за сьогодні, результат буде від'ємним.
    
    try:
        # перетворюємо рядок у об'єкт datetime
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()

        # отримуємо поточну дату
        today = datetime.today().date()

        # розраховуємо різницю в днях
        delta = today - given_date

        # повертаємо кількість днів як ціле число
        return delta.days

    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
        return None


# приклади використання
print(get_days_from_today("2025-10-01"))  # -> 6 (наприклад, якщо сьогодні 2025-10-07)
print(get_days_from_today("2025-10-15"))  # -> -8 (дата у майбутньому)
print(get_days_from_today("2025.10.15"))  # -> повідомлення про помилку


