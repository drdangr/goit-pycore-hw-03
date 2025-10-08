from datetime import datetime, date, timedelta

user_input = input("Enter year, month, day through '-' aka 2025-01-25: ")
#parse the input
try:
    given_date = datetime.strptime(user_input, "%Y-%m-%d").date()
    print("given date is: ", given_date)
except ValueError:
    print("Invalid date format. Please enter date in YYYY-MM-DD format.")
    exit()

#check today's date
today = date.today()
print("Today's date:", today)
#define function to calculate difference in days
def get_days_from_today(date):
    delta = (date - today).days
    return delta
#calculate difference in days between today and given date
difference = get_days_from_today(given_date)
#tell user the difference
print("Difference in days:", difference)
