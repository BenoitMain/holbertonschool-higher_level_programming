#!/usr/bin/python3

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a given template and a list of attendee dictionaries.

    Each invitation is created by replacing placeholders in the template with corresponding values
    from each attendee. If a required value is missing or empty, it is replaced by "N/A".
    The output files are saved as output_1.txt, output_2.txt, etc., one per attendee.

    Parameters:
    - template (str): The invitation text template containing placeholders like {name}, {event_title}, etc.
    - attendees (list): A list of dictionaries. Each dictionary must contain the keys:
      "name", "event_title", "event_date", and "event_location".

    Returns:
    - None

    Error Handling:
    - If the template is not a string, an error message is printed and the function exits.
    - If attendees is not a list of dictionaries, an error message is printed and the function exits.
    - If the template is empty or contains only whitespace, an error message is printed and the function exits.
    - If the attendees list is empty, a message is printed and no files are generated.
    - If any placeholder value is missing or None in a dictionary, it is replaced with "N/A".
    - If a file cannot be written, an error message is printed.

    Example:
    >>> generate_invitations("Hello {name}, you are invited to {event_title}", [{"name": "Alice", "event_title": "PyCon"}])
    Creates a file named output_1.txt with the personalized invitation.
    """
    # Check if the template is a string
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(person, dict) for person in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Check if the template string is empty or contains only whitespace
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if the list of attendees is empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Loop through each attendee in the list, starting index at 1
    for index, person in enumerate(attendees, start=1):
        # Define the list of expected placeholders in the template
        placeholders = ["name", "event_title", "event_date", "event_location"]

        # Start with the original template text
        invitation_text = template

        # Replace each placeholder with the corresponding value from the attendee's data
        for placeholder in placeholders:
            value = person.get(placeholder)  # Get value from dictionary
            if value is None or value == "":  # If value is missing or empty
                value = "N/A"                # Use "N/A" as fallback
            # Replace the placeholder in the text
            invitation_text = invitation_text.replace(
                "{" + placeholder + "}", str(value))

        # Generate the output filename based on the attendee index
        filename = f"output_{index}.txt"

        # Try to write the personalized invitation to a file
        try:
            with open(filename, "w") as f:
                f.write(invitation_text)
        except Exception as e:
            # Handle and display any file writing error
            print(f"Error writing {filename}: {e}")
