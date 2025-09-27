from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format.
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date

def calculate_future_date(days_to_add):
    """
    Calculate and display the future date after adding specified days.
    
    Parameters:
    days_to_add (int): Number of days to add to current date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Date after {days_to_add} days: {formatted_future_date}")
    return future_date

def main():
    """
    Main function to demonstrate datetime operations.
    """
    print("=== Python Datetime Module Explorer ===\n")
    
    # Part 1: Display current date and time
    print("Part 1: Current Date and Time")
    display_current_datetime()
    print()
    
    # Part 2: Calculate future date
    print("Part 2: Calculate Future Date")
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer for the number of days.")
    
    print("\n=== End of Datetime Exploration ===")

if __name__ == "__main__":
    main()