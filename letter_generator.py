def generate_letter(name, date):
    # Define the template with placeholders for 'name' and 'date'
    template = """
    Dear {name},

    This is to remind you that your next appointment is scheduled for {date}.
    Please let us know if you need to reschedule at least 24 hours in advance.

    Sincerely,
    [Your Company]
    """
    # Replace placeholders with actual values
    return template.format(name=name, date=date)

# Example usage
custom_letter = generate_letter("John Doe", "April 12th, 2024")
print(custom_letter)
