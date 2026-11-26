import calendar

print("Welcome to the super calendar!\n")

while True:
    try:
        year = int(input('Please enter the year: '))
        month = int(input('Please enter the month: '))
        if month < 1 or month > 12:
            print("Invalid month. Please enter a value between 1 and 12.")
            continue
    except ValueError:
        print("Invalid input. Please enter numeric values for year and month.")
        continue

    print(calendar.month(year, month))
    print("Have a good day!")
    break
