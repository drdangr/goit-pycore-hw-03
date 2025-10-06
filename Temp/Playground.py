import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
        #Trim leading/trailing whitespace
        phone_number = phone_number.strip()

        # Remove all non-digit characters except leading +
        cleaned = re.sub(r"[^0-9+]", "", phone_number)

        
        print("Нормалізований номер телефону", cleaned)

        # Ensure it starts with +38
        if cleaned.startswith("00"):
                cleaned = "+" + cleaned[2:]

        #Ensure it starts with +380
        if cleaned.startswith("+380"):
                return cleaned

        #Ensure it starts with 380
        if cleaned.startswith("380"):
                return "+" + cleaned

        #Ensure it starts with 0
        if cleaned.startswith("0"):
                return "+38" + cleaned

        #If it starts with anything else, add +38 at the beginning
        if not cleaned.startswith("+"):
                return "+38" + cleaned

        return cleaned


sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
