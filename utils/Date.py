
# 'dd-mm-yyyy'
def custom_date_formatter(date_str):
    # Remove any leading/trailing spaces
    date_str = date_str.strip()

    # Check if the input is in 'yyyy-mm-dd' format
    if len(date_str) == 10 and date_str[4] == '-' and date_str[7] == '-':
        year, month, day = date_str.split('-')
        return f"{day}-{month}-{year}"

    # Check if the input is in 'mm-dd-yyyy' format
    elif len(date_str) == 10 and date_str[2] == '-' and date_str[5] == '-':
        month, day, year = date_str.split('-')
        return f"{day}-{month}-{year}"

    # If the format is not recognized, return an error message
    else:
        return " Please enter a valid date in 'yyyy-mm-dd' or 'mm-dd-yyyy' format."

# Example usage
user_date = input("Enter the date (in 'yyyy-mm-dd' or 'mm-dd-yyyy' format): ")

# Call the custom date formatter function
formatted_date = custom_date_formatter(user_date)

print("Formatted date: ", formatted_date)