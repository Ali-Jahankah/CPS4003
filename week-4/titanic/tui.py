def welcome(width=30):
    title='Titanic Records System'
    print(f"""
          {'-'*width}
          {title.center(width,' ')}
          {'-'*width}
          """)


def main_menu():
    menu_options = [ 'Load Data', 'Process Data', 'Visualise Data','Exit']
    print("Please choose an option: ")
    for index in range(len(menu_options)):
        print(f"[{index + 1}] - {menu_options[index]}")
    chosen_option =int(input("\nMain option: "))
    if chosen_option in range(1,len(menu_options)+1):
        return chosen_option
    else:
        return False

def data_file_path():
    filePath = input('\n Please enter the file path below:\n')
    isCSV = filePath.endswith('.csv')
    if not isCSV:
        print("\n File must be CSV. 'data/titanic.csv' chosen by default.")
        return 'data/titanic.csv'
    return filePath


def progress(operation, percent):
    status = "STARTED" if percent == int(0) else 'COMPLETED' if percent == 100 else f"IN PROGRESS ({percent}%)"
    before = '\n' if percent == 0 else ''
    after = '\n' if percent == 100 else ''
    print(f"{before}--- {operation.upper()}: {status} ---{after}")


def error(error_msg):
    print(f"Error! {error_msg}")


def process_menu():
    menu_options = ['Extract Passenger Names',
        'Count Survivors',
        'Count Passengers Per Gender',
        'Count Passengers Per Age Group',
        'Return to main menu']
    while True:
        print("\nPlease choose an option for processing the data:\n")
        for index in range(len(menu_options)):
            print(f"[{index+1}] - {menu_options[index]}")
        chosen_option =int(input("\nProcess type: "))
        if chosen_option in range(1,len(menu_options)+1):
            return chosen_option


def display_passenger_names(passenger_names):
    if len(passenger_names) == 0:
        return error('The list is empty and there is no names')
    print(passenger_names)


def display_survivor_count(survivor_count):
    print (f'There are {survivor_count} people survived.')


def display_sex_counts(sex_counts):
   print(f"""
        
        Number of males and femails: {sex_counts}
         
         """)


def display_age_group_counts(age_group_counts):
     print(f"""
        
        Number of age groups: {age_group_counts}
         
         """)


def visual_menu():
    visual_menu_options = ['Passenger Class Horizontal Bar Graph',
        'Return to main menu']
    
    while True:
        print("\nPlease choose an option for visialising the data:\n")
        for index in range(len(visual_menu_options)):
            print(f"[{index+1}] - {visual_menu_options[index]}")
        chosen_option =int(input("\nVisualise option: "))
        if chosen_option in range(1,len(visual_menu_options)+1):
            return int(chosen_option)


def display_visual(visual):
    """
    Display the visual.

    The function should display the visual.

    :param visual: A string containing appropriate ASCII art.
    :return: None
    """
    # TODO: Your code here (remove pass below)
    pass
