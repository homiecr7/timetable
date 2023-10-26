# Constants
WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
WORK_HOURS = range(9, 17)  # 9 am to 5 pm

# Data structure to store the timetable
timetable = {day: [] for day in WEEK_DAYS}

# Function to display program header
def display_header():
    """
    Display the program header with information about the Weekly Timetable Manager.

    This function prints the program's title, the author's name, and the UniSA email.
    """
    print("Weekly Timetable Manager")
    print("Author: Your Name")
    print("UniSA email: your.email@unisa.edu.au")

# Function to display the main menu
def display_menu():
    print("\nMain Menu:")
    print("1. Create an event")
    print("2. Update an event")
    print("3. Delete an event")
    print("4. Print the timetable")
    print("5. Print events on a specific day")
    print("6. Save timetable to a file")
    print("7. Load timetable from a file")
    print("8. Search Event")
    print("9. Quit")

# Function to validate user input
def get_user_input(prompt, validator):
    """
    Display the main menu for the Weekly Timetable Manager.

    This function prints the available options in the main menu, including creating, updating, and
    deleting events, printing the timetable, printing events on a specific day, saving and loading
    timetable data from a file, searching for events based on keywords, and quitting the program.
    """
    while True:
        user_input = input(prompt)
        if validator(user_input):
            return user_input
        print("Invalid input. Please try again.")

# Function to create a new event
def create_event():
    """
    Create a new event and add it to the weekly timetable.

    This function prompts the user to input the day of the week, title of the event, start time,
    end time, and an optional location for the event. It checks for any overlapping events and
    adds the new event to the timetable if there are no overlaps.
    """
    day = get_user_input("Enter the day of the week (e.g., Monday): ", lambda x: x in WEEK_DAYS)
    title = input("Enter the title of the event: ")
    start_time = int(get_user_input("Enter the start time (hour, e.g., 9): ", lambda x: x.isdigit() and int(x) in WORK_HOURS))
    end_time = int(get_user_input("Enter the end time (hour, e.g., 10): ", lambda x: x.isdigit() and int(x) in WORK_HOURS))
    location = input("Enter the location (optional):")
    
    new_event = {"title": title, "start_time": start_time, "end_time": end_time, "location": location}
    
    # Check for overlap
    overlap = False
    for event in timetable[day]:
        if (new_event["start_time"] < event["end_time"] and new_event["end_time"] > event["start_time"]):
            overlap = True
            print("Error: Overlapping events. Please reschedule.")
    if not overlap:
        timetable[day].append(new_event)
        print("Event created successfully!")

# Function to update an existing event
def update_event():
    """
    Update an existing event based on a keyword search within a specific day.

    This function allows the user to update an event by first specifying the day of the week,
    followed by entering a case-insensitive keyword to search for matching events based on their
    title or location. If matching events are found, the user can select the event to update by
    entering the associated number. The function then prompts the user to provide updated
    information for the selected event, including a new title, end time, and an optional location.
    """

    day = get_user_input("Enter the day of the week (e.g., Monday): ", lambda x: x in WEEK_DAYS)
    keyword = input("Enter a keyword to search for events to update (case-insensitive): ").lower()
    event_found = False
    matching_events = []

    for event in timetable[day]:
        # Convert event title and location to lowercase for case-insensitive search
        title = event['title'].lower()
        location = event['location'].lower()
        if keyword in title or keyword in location:
            matching_events.append(event)

    if matching_events:
        print("Matching Events:")
        for i, event in enumerate(matching_events):
            print(f"{i + 1}. {event['start_time']}-{event['end_time']} => {event['title']} @ {event['location']}")
        
        selected_event_index = int(get_user_input("Enter the number of the event to update: ", lambda x: x.isdigit() and 1 <= int(x) <= len(matching_events))) - 1
        selected_event = matching_events[selected_event_index]

        print("Event found. Please provide updated information:")
        selected_event["title"] = input("Enter the new title: ")
        selected_event["end_time"] = int(get_user_input("Enter the new end time (hour): ", lambda x: x.isdigit() and int(x) in WORK_HOURS))
        selected_event["location"] = input("Enter the new location (optional): ")
        print("Event updated successfully!")
        event_found = True
    
    if not event_found:
        print("No matching events found.")

# Function to delete an event
def delete_event():
    """
    Delete an existing event based on a keyword search within a specific day.

    This function allows the user to delete an event by first specifying the day of the week,
    followed by entering a case-insensitive keyword to search for matching events based on their
    title or location. If matching events are found, the user can select the event to delete by
    entering the associated number. The function then removes the selected event from the timetable.
    """
    day = get_user_input("Enter the day of the week (e.g., Monday): ", lambda x: x in WEEK_DAYS)
    keyword = input("Enter a keyword to search for events to delete (case-insensitive): ").lower()
    event_found = False
    matching_events = []

    for event in timetable[day]:
        # Convert event title and location to lowercase for case-insensitive search
        title = event['title'].lower()
        location = event['location'].lower()
        if keyword in title or keyword in location:
            matching_events.append(event)

    if matching_events:
        print("Matching Events:")
        for i, event in enumerate(matching_events):
            print(f"{i + 1}. {event['start_time']}-{event['end_time']} => {event['title']} @ {event['location']}")

        selected_event_index = int(get_user_input("Enter the number of the event to delete: ", lambda x: x.isdigit() and 1 <= int(x) <= len(matching_events))) - 1
        selected_event = matching_events[selected_event_index]

        timetable[day].remove(selected_event)
        print("Event deleted successfully!")
        event_found = True
    
    if not event_found:
        print("No matching events found.")

# Function to print the weekly timetable (FR11)
def print_timetable():
    choose_start_day()  # Call the choose_start_day function
    print("Weekly Timetable:")
    for day in WEEK_DAYS:
        print(day)
        for event in timetable[day]:
            print(f"{event['start_time']}-{event['end_time']} => {event['title']} @ {event['location']}")

# Function to print events on a specific day
def print_events_on_day():
    """
    Print the weekly timetable, including events for each day of the week.

    This function displays a formatted weekly timetable, showing events for each day. It lists
    the day of the week and, for each event, the start time, end time, title, and location (if provided).
    """
    day = input("Enter the day of the week (e.g., Monday): ")
    choose_start_day()  # Call the choose_start_day function
    print(f"Events on {day}:")
    for event in timetable[day]:
        print(f"{event['start_time']}-{event['end_time']} => {event['title']} @ {event['location']}")

# Function to save the timetable to a file
def save_timetable():
    """
    Save the weekly timetable data to a file.

    This function prompts the user to enter a file name and then saves the timetable data to that file.
    The data is written in a comma-separated format with one line for each event, including the day of
    the week, title, start time, end time, and location (if provided). The function then prints a success
    message upon saving the data.
    """
    file_name = input("Enter the file name to save the timetable data: ")
    with open(file_name, "w") as file:
        for day, events in timetable.items():
            for event in events:
                file.write(f"{day}, {event['title']}, {event['start_time']}, {event['end_time']}, {event['location']}\n")
    print("Timetable data saved to the file.")

# Function to load the timetable from a file
def load_timetable():
    """
    Load timetable data from a file.
    This function allows the user to specify a file from which to load timetable data. The data should be
    formatted with each line representing an event and containing day, title, start time, end time, and location.
    The function attempts to read and parse the file, adding the events to the weekly timetable.
    """
    file_name = input("Enter the file name to load the timetable data: ")
    try:
        with open(file_name, "r") as file:
            for line in file:
                day, title, start_time, end_time, location = line.strip().split(", ")
                new_event = {"title": title, "start_time": int(start_time), "end_time": int(end_time), "location": location}
                timetable[day].append(new_event)
        print("Timetable data loaded from the file.")
    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")

def search_events():
    """
    Load the weekly timetable data from a file.

    This function prompts the user to enter the name of a file containing timetable data. It then attempts
    to read the data from the file, assuming a comma-separated format with one event per line. The data is
    used to update the current timetable with the loaded events. If the file is not found, the function
    prints an error message.
    """
    keyword = input("Enter a keyword to search for (case-insensitive): ").lower()
    matching_events = []

    for day in WEEK_DAYS:
        events = timetable[day]
        for event in events:
            # Convert event title and location to lowercase for case-insensitive search
            title = event['title'].lower()
            location = event['location'].lower()
            if keyword in title or keyword in location:
                matching_events.append(event)

    if matching_events:
        # Sort matching events by start time
        matching_events.sort(key=lambda x: x['start_time'])
        print("Matching Events:")
        for event in matching_events:
            print(f"{event['start_time']}-{event['end_time']} => {event['title']} @ {event['location']}")
    else:
        print("No matching events found.")

def choose_start_day():
    """
    Allow the user to choose the start day of the week.

    This function prompts the user to select the start day of the week, which can be either Monday (1) or Sunday (2).
    Based on the user's choice, the order of days in the weekly timetable is adjusted accordingly.
    If the user provides an invalid choice, the default start day of Monday is used, and a message is displayed.
    """
    global WEEK_DAYS
    choice = input("Choose the start day of the week (1 for Monday, 2 for Sunday): ")
    if choice == '1':
        WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    elif choice == '2':
        WEEK_DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    else:
        print("Invalid choice. Defaulting to Monday as the start day of the week.")

# Main program loop
def main():
    """
    Main program loop for the Weekly Timetable Manager.

    This function serves as the central control point for the Weekly Timetable Manager program.
    It displays the program header, provides a menu for user interaction, and handles various
    user choices, such as creating, updating, and deleting events, printing the timetable, saving
    and loading data from a file, searching for events, and quitting the program.
    """
    display_header()
    quit_program = False
    
    while not quit_program:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_event()
        elif choice == '2':
            update_event()
        elif choice == '3':
            delete_event()
        elif choice == '4':
            print_timetable()
        elif choice == '5':
            print_events_on_day()
        elif choice == '6':
            save_timetable()
        elif choice == '7':
            load_timetable()
        elif choice == '8':
            search_events()
        elif choice == '9':
            print("Goodbye!")
            quit_program = True
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
