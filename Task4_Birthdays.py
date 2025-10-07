#list of users with birthdays
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Test Testov", "birthday": "1990.10.11"}#added a test user
]



#function to find upcoming birthdays within the next 7 days

def get_upcoming_birthdays(users):
    from datetime import datetime, date, timedelta

    today = date.today()
    current_year = today.year
    upcoming_birthdays = []
   

    def adjust_birthday_to_monday(birthday: date) -> date:
        # weekday(): 0=Mon ... 5=Sat, 6=Sun
        weekday = birthday.weekday()

        if weekday == 5:      # saturday
            return birthday + timedelta(days=2)
        elif weekday == 6:    # sunday
            return birthday + timedelta(days=1)
        else:                 # rest days
            return birthday
        
    #utility function to handle leap year birthdays    
    def place_birthday_in_year(birth: date, year: int) -> date:
        try:
            return birth.replace(year=year)
        except ValueError:
            if birth.month == 2 and birth.day == 29:
                return date(year, 2, 28)
            else:
                raise
    
    #work with each user
    for user in users:
        # get date object from birthday string
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Create a birthday date for the current year, handling leap years
        birthday_this_year = place_birthday_in_year(birthday, current_year)
        
        # If the birthday has already occurred this year, use next year
        if birthday_this_year < today:
            birthday_this_year = place_birthday_in_year(birthday, current_year + 1)
        
        # Calculate days until birthday
        days_until_birthday = (birthday_this_year - today).days

        #debug print
        print(f"{user['name']}'s birthday is on {birthday_this_year}, which is in {days_until_birthday} days.")

        if 0 <= days_until_birthday <= 7:
            birthday_this_year = adjust_birthday_to_monday(birthday_this_year)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
           

    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)

if upcoming_birthdays:
    print("Upcoming birthdays:")
    for item in upcoming_birthdays:
        print(f"{item['name']}: {item['congratulation_date']}")
else:
    print("No upcoming birthdays within 7 days.")