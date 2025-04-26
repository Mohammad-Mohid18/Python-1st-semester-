from datetime import datetime

# Define a list of dates in "YYYY-MM-DD" format
date_strings = ["2023-07-11", "2022-02-22", "2024-05-11", "2025-12-31", "2021-01-01"]
print("List of dates:")
print(date_strings)

# Convert the date strings to datetime objects
dates = [datetime.strptime(date, "%Y-%m-%d") for date in date_strings]

# Get the current date
current_date = datetime.now()
print("Current date:", current_date.strftime("%Y-%m-%d"))

# Define a function to check if a date is in the future
def is_date_in_future(date):
    return date > current_date

# Use the filter function to extract dates in the future
dates_in_future = list(filter(is_date_in_future, dates))

# Convert the filtered dates back to strings
filtered_date_strings = [date.strftime("%Y-%m-%d") for date in dates_in_future]
print("\nDates in the future:")
# Print the future dates
print(filtered_date_strings)
