# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the current date and time
def display_current_datetime():
    current_date = datetime.now()  # get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # format it
    print("Current date and time:", formatted_date)
    return current_date

# Part 2: Calculate a future date
def calculate_future_date(current_date):
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Main program
if __name__ == "__main__":
    current_date = display_current_datetime()
    calculate_future_date(current_date)
