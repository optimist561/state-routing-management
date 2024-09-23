# Dictionary to hold the users and their assigned states from the CSV
qualified_states_data = {
    1: ('AMAYA CARTAGENA', '19', ['Arizona', 'Florida', 'Indiana', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Missouri', 'Nebraska', 'New York', 'North Carolina', 'Ohio', 'South Carolina', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Georgia', 'Alabama']),
    2: ('ARIAHNA JAROSZ', '36', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'District of Columbia', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Nebraska', 'Nevada', 'New Hampshire', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Vermont', 'Virginia', 'Wisconsin']),
    3: ('CONNER CARMACK', '25', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Florida','Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Michigan','Mississippi', 'Missouri', 'New Jersey', 'New York', 'North Carolina','Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee','Texas', 'Virginia', 'Georgia']),
    4: ('ASHLEY KNUCK', '22', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Florida', 'Georgia', 'Hawaii', 'Indiana', 'Louisiana', 'Maryland', 'Michigan', 'Mississippi', 'Missouri', 'New Jersey', 'New York', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'Texas', 'Vermont', 'Virginia']),
    5: ('AUSTIN DODSON', '25', ['Alabama', 'Arizona', 'Arkansas', 'Colorado', 'Florida', 'Georgia', 'Indiana', 'Kentucky', 'Louisiana', 'Michigan', 'Mississippi', 'Missouri', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Washington']),
    6: ('BREAUNNA KEIBLER', '12', ['Alabama', 'Florida', 'Georgia', 'Indiana', 'Maryland', 'Michigan', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia']),
    7: ('EDGARDO VALDES-BIGGS', '18', ['Arizona', 'Arkansas', 'California', 'Florida', 'Indiana', 'Kentucky', 'Michigan', 'Mississippi', 'Missouri', 'New Mexico', 'New York', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia']),
    8: ('FRANCK DORENE', '13', ['Florida', 'Indiana', 'Louisiana', 'Maryland', 'Missouri', 'Nebraska', 'New York', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia']),
    9: ('HECTOR GUTIERREZ', '31', ['Alabama', 'Arizona', 'Arkansas', 'Florida', 'Georgia', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Mississippi', 'Missouri', 'Montana', 'Nevada', 'New Mexico', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'Washington', 'Wisconsin']),
    10: ('JAY HOLT', '11', ['Arkansas', 'Florida', 'Indiana', 'Louisiana', 'Michigan', 'New Mexico', 'Ohio', 'South Carolina', 'Tennessee', 'Texas', 'Virginia']),
    11: ('JEFFREY LANGE', '21', ['Alabama', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Maryland', 'Michigan', 'Missouri', 'North Carolina', 'Ohio', 'South Carolina', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'West Virginia', 'Wisconsin']),
    12: ('JENNIFER KARBOWSKI', '24', ['Alabama', 'Arizona', 'Arkansas', 'Connecticut', 'Florida', 'Georgia', 'Idaho', 'Indiana', 'Kentucky', 'Louisiana', 'Maine', 'Michigan', 'Mississippi', 'Missouri', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'West Virginia', 'Wyoming']),
    13: ('JOHN DANYLAK', '35', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Delaware', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'West Virginia', 'Wisconsin', 'Wyoming']),
    14: ('JOSEPH GIGLIOTTI', '18', ['Arizona', 'Arkansas', 'California', 'Florida', 'Indiana', 'Kentucky', 'Louisiana', 'Michigan', 'Missouri', 'New York', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Georgia']),
    15: ('JOSEPH SANDOR', '39', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Washington']),
    16: ('JUSTIN MORGAN', '23', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Mississippi', 'Missouri', 'New York', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia']),
    17: ('JOSHUA BISHOP', '17', ['Florida', 'Georgia', 'Illinois', 'Indiana', 'Louisiana', 'Maryland', 'Michigan', 'Missouri', 'Nevada', 'New York', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia']),
    18: ('JOVAN RAMOS', '19', ['Alabama', 'Arizona']),
    19: ('KENNETH ZUMBA', '29', ['Alabama', 'Arizona', 'Arkansas', 'Colorado', 'Delaware', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Iowa', 'Kentucky', 'Louisiana', 'Maryland', 'Massachusetts', 'Mississippi', 'Missouri', 'Nevada', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oregon', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Washington', 'West Virginia']),
    20: ('KYLEE JOHNSON', '19', ['Florida', 'Indiana', 'Iowa', 'Louisiana', 'Maryland', 'Michigan', 'New York', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Wisconsin', 'Georgia', 'Alabama', 'California', 'North Carolina']),
    21: ('MARK OZBOURN', '22', ['Alabama', 'Alaska', 'Arizona', 'California', 'Colorado', 'Florida', 'Hawaii', 'Indiana', 'Louisiana', 'Michigan', 'Missouri', 'New Mexico', 'New York', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Virginia', 'West Virginia']),
    22: ('MARK PAKKALA', '25', ['Alabama', 'Arizona', 'Arkansas', 'Colorado', 'Florida', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Michigan', 'Mississippi', 'Missouri', 'New Jersey', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Wisconsin', 'Georgia']),
    23: ('MATTHEW WOLCOTT', '32', ['Alabama', 'Arkansas', 'Colorado', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'North Carolina', 'Ohio', 'Oklahoma', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'West Virginia', 'Wisconsin', 'Wyoming']),
    24: ('MICHAEL SOUTHWICK', '20', ['Arizona', 'Arkansas', 'Colorado', 'Florida', 'Georgia', 'Kansas', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Missouri', 'Nevada', 'North Carolina', 'Ohio', 'South Carolina', 'Tennessee', 'Texas', 'Utah', 'Virginia', 'West Virginia']),
    25: ('NATALIA GEORGE', '24', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Kansas', 'Louisiana', 'Maryland', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'New Jersey', 'New York', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia']),
    26: ('NIKKI AUSTIN', '25', ['Alabama', 'Arkansas', 'California', 'Colorado', 'District of Columbia', 'Florida', 'Georgia', 'Indiana', 'Kentucky', 'Louisiana', 'Mississippi', 'Missouri', 'New Hampshire', 'New Jersey', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Wisconsin', 'Michigan']),
    27: ('NOAH PANGANIBAN', '33', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Florida', 'Georgia', 'Hawaii', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Mississippi', 'Missouri', 'New Jersey', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Vermont', 'Virginia', 'Washington', 'Wisconsin']),
    28: ('PATRICK TOLLER', '18', ['Florida', 'Indiana', 'Kentucky', 'Louisiana', 'Michigan', 'Missouri', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Georgia', 'California', 'Alabama']),
    29: ('ROBERT BOWLING', '23', ['Alabama', 'Arizona', 'Arkansas', 'Florida', 'Georgia', 'Illinois', 'Kentucky', 'Louisiana', 'Michigan', 'Mississippi', 'Missouri', 'New Mexico', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Washington', 'West Virginia']),
    30: ('ROSALVA DIAZ', '25', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Florida', 'Georgia', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Michigan', 'Mississippi', 'Missouri', 'New Jersey', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia']),
    31: ('SANDRA KING', '15', ['Alabama', 'Arizona', 'California', 'Delaware', 'Florida', 'Georgia', 'Indiana', 'Maryland', 'North Carolina', 'Ohio', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia']),
    32: ('SHARMA DRUMMOND', '29', ['Alabama', 'Arizona', 'California', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Washington', 'West Virginia']),
    33: ('SHERRI THOMAS', '31', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Connecticut', 'District of Columbia', 'Florida', 'Georgia', 'Idaho', 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana', 'Michigan', 'Minnesota', 'Missouri', 'Montana', 'Nevada', 'New Jersey', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Wisconsin']),
    34: ('TYLER MORGAN', '27', ['Alabama', 'Arizona', 'Arkansas', 'Colorado', 'Florida', 'Georgia', 'Illinois', 'Indiana', 'Kentucky', 'Louisiana', 'Maryland', 'Massachusetts', 'Michigan', 'Mississippi', 'Missouri', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Washington', 'West Virginia']),
    35: ('TYRESE ROBERTS', '25', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Florida', 'Georgia', 'Indiana', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Mississippi', 'Missouri', 'New Jersey', 'New York', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Utah', 'Virginia']),
    36: ('WANDEE CHANG', '26', ['Alabama', 'Arizona', 'Arkansas', 'California', 'Florida', 'Georgia', 'Idaho', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maryland', 'Michigan', 'Mississippi', 'Missouri', 'New Jersey', 'North Carolina', 'Ohio', 'Oklahoma', 'Pennsylvania', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'Wisconsin']),
    37: ('WILNIE AUGUSTAVE', '22', ['Alabama', 'Arizona', 'California', 'Florida', 'Georgia', 'Illinois','Indiana' ,' Kansas' , ' Louisiana' , 'Michigan' , ' Minnesota' ,'Missouri','New Jersey',' New York ' ,' North Carolina',' Ohio',' Oklahoma' , 'Pennsylvania', 'Tennessee' , 'Texas' ,'Virginia' , 'Washington']),
    38: ('ZACHARY WESTFALL', '12', ['Alabama', 'Arkansas', 'Florida', 'Indiana','Louisiana' ,'Maryland', 'Missouri', 'Ohio' , 'South Carolina', 'Tennessee' , 'Texas' , 'Virginia', ]),
    # More users continue here...


    # Add more users as needed...
}

# Function to export selected users' data to a CSV file
# Dictionary to hold the users and their assigned states from the CSV
import csv
import os
from datetime import datetime
import shutil  # for file backup
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started")

# File paths for storing user data and backup
csv_file = 'qualified_states_data.csv'
backup_file = 'qualified_states_data_backup.csv'

# Function to load data from the CSV file at the start of the program
# Function to load data from the CSV file at the start of the program
def load_data_from_csv():
    qualified_states_data = {}
    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                # Check if the row is empty or contains only empty strings
                if not row or all(not field.strip() for field in row):
                    continue  # Skip empty rows
                
                try:
                    # Validate that the row contains valid data before proceeding
                    user_id = int(row[0].strip()) if row[0].strip().isdigit() else None
                    if user_id is None:
                        continue  # Skip rows with invalid user_id
                    
                    name = row[1].strip() if row[1].strip() else "Unknown"
                    level = row[2].strip() if row[2].strip() else "Unknown Level"  # New level field
                    num_states = int(row[3].strip()) if row[3].strip().isdigit() else 0
                    states = row[4].strip().split(', ') if row[4].strip() else []  # Split the states by comma
                    qualified_states_data[user_id] = (name, level, num_states, states)
                except Exception as e:
                    logging.error(f"Error processing row: {row}. Skipping. Error: {e}")
    except FileNotFoundError:
        logging.warning(f"{csv_file} not found. Starting with an empty dataset.")
    except Exception as e:
        logging.error(f"An error occurred while loading the CSV: {e}")
    
    return qualified_states_data




# Function to save data to the CSV file after changes
def save_data_to_csv():
    global qualified_states_data
    # Create a backup of the current data before saving
    if os.path.exists(csv_file):
        shutil.copy(csv_file, backup_file)  # Create backup file

    try:
        # Save directly to the original CSV file to ensure persistence
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['user_id', 'name', 'level', '# of states assigned', 'state(s)'])
            for user_id, (name, level, num_states, states) in qualified_states_data.items():
                writer.writerow([user_id, name, level, num_states, ', '.join(sorted(states))])
        logging.info(f"Data successfully saved to {csv_file}.")
        
        # Save an additional timestamped backup if needed
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_file_with_timestamp = f'qualified_states_data_{timestamp}.csv'
        shutil.copy(csv_file, csv_file_with_timestamp)
        logging.info(f"Backup created: {csv_file_with_timestamp}")

    except Exception as e:
        logging.error(f"Error saving data: {e}")


# Function to revert to the previous version (undo)
def revert_to_backup():
    global qualified_states_data
    if os.path.exists(backup_file):
        try:
            shutil.copy(backup_file, csv_file)  # Restore the backup to the main CSV file
            logging.info("Reverted to the previous version.")
            
            # Reload the data after reverting
            qualified_states_data = load_data_from_csv()  # Reload the dataset from the reverted file
            logging.info("Data successfully reloaded after revert.")
        except Exception as e:
            logging.error(f"Failed to revert to backup: {e}")
    else:
        logging.warning("No backup file found to revert.")

# Function to view users' state assignments
# Function to view users' state assignments
def view_user_assignments(user_ids):
    for user_id in user_ids:
        if user_id in qualified_states_data:
            name, level, num_states, states = qualified_states_data[user_id]
            logging.info(f"\nUser ID: {user_id}")
            logging.info(f"Name: {name}")
            logging.info(f"Level: {level}")  # Display the level
            logging.info(f"Number of States: {num_states}")
            logging.info("Assigned States:")
            for state in sorted(states):
                logging.info(f"  - {state.strip()}")
        else:
            logging.warning(f"User {user_id} not found.")

# Function to display all users
def display_all_users():
    logging.info("\nAvailable users:")
    for user_id, (name, level, num_states, _) in qualified_states_data.items():
        logging.info(f"{user_id}: {name} - {num_states} states")


# Function to get valid user IDs from input, with the option to export/view all users
def get_user_ids():
    user_input = input("Enter user numbers (e.g., 1,2,3 or type 'all' for all users): ").strip()
    
    if user_input.lower() == 'all':
        return list(qualified_states_data.keys())
    else:
        user_numbers = user_input.split(',')
        return [int(num.strip()) for num in user_numbers if num.strip().isdigit()]

# Function to modify state assignments (add/remove) for a user
def modify_user_state(user_id, action):
    global qualified_states_data
    if user_id in qualified_states_data:
        name, level, _, states = qualified_states_data[user_id]  # Adjusted to unpack 'level' as well
        logging.info(f"\nModifying user {name} (User ID: {user_id})")
        logging.info(f"Current Assigned States ({len(states)} states):")
        for state in sorted(states):
            logging.info(f"  - {state}")

        handle_state_modification(states, action, name)

        # Update the user's data with the new state list
        qualified_states_data[user_id] = (name, level, len(states), states)
        
        # Save the changes to CSV
        save_data_to_csv()
    else:
        logging.warning(f"User {user_id} not found.")



# Function to handle adding/removing states
def handle_state_modification(states, action, name):
    state_input = input(f"Enter the state(s) you want to {action} for {name} (comma separated): ").strip()
    state_list = [convert_abbreviation_to_full(state.strip().title()) for state in state_input.split(",")]

    if action == "add":
        for state in state_list:
            if state not in states:
                states.append(state)
                logging.info(f"State '{state}' added to {name}.")
            else:
                logging.info(f"{name} is already assigned to '{state}'.")
    elif action == "remove":
        for state in state_list:
            if state in states:
                states.remove(state)
                logging.info(f"State '{state}' removed from {name}.")
            else:
                logging.info(f"{name} is not assigned to '{state}'.")

    if not states:
        logging.info(f"{name} has no states left after this modification.")
    
    states.sort()

# Function to add a user (implementation)
# Function to add a user with automatic ID assignment
# Function to add a user with reassigned user ID
def add_user():
    global qualified_states_data
    try:
        name = input("Enter the user's name: ").strip()
        level = input("Enter the user's level: ").strip()
        state_input = input("Enter the states assigned to this user (comma separated): ").strip()
        state_list = [convert_abbreviation_to_full(state.strip().title()) for state in state_input.split(",")]

        # Add new user with temporary max ID (will be reassigned)
        temp_id = len(qualified_states_data) + 1
        qualified_states_data[temp_id] = (name, level, len(state_list), state_list)
        logging.info(f"User {name} added with temporary ID {temp_id}.")
        
        # Reassign IDs to ensure they remain sequential
        reassign_user_ids()

        # Save the changes to CSV
        save_data_to_csv()
        
    except Exception as e:
        logging.error(f"Failed to add user: {e}")




# Function to remove a user (implementation)
def remove_user(user_id):
    global qualified_states_data
    if user_id in qualified_states_data:
        del qualified_states_data[user_id]  # Remove the user from the dictionary
        logging.info(f"User with ID {user_id} removed.")
        
        # Reassign IDs after removal
        reassign_user_ids()
        
        # Save the changes to CSV
        save_data_to_csv()
    else:
        logging.warning(f"User {user_id} not found.")



        
#reassign user id
def reassign_user_ids():
    global qualified_states_data
    # Sort the users by their current user_id (the dictionary keys)
    sorted_users = sorted(qualified_states_data.items(), key=lambda x: x[0])
    
    # Create a new dictionary with reassigned IDs
    new_data = {}
    new_id = 1
    for _, (name, level, num_states, states) in sorted_users:
        new_data[new_id] = (name, level, num_states, states)
        new_id += 1
    
    qualified_states_data = new_data
    logging.info("User IDs have been reassigned sequentially.")






# Helper function to map state abbreviations to full names
state_abbreviations = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'DC': 'District of Columbia', 'FL': 'Florida',
    'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland', 'MA': 'Massachusetts',
    'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri', 'MT': 'Montana',
    'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico',
    'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
    'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota',
    'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'WA': 'Washington',
    'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# Function to convert abbreviation to full state name
def convert_abbreviation_to_full(state_input):
    return state_abbreviations.get(state_input.upper(), state_input.title())

# Function to export selected users' data to a CSV file
def export_users_to_csv(user_ids, filename='exported_users.csv'):
    if not filename.endswith('.csv'):
        filename += '.csv'
    
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["User ID", "User Name", "Level", "Number of States", "Assigned States"])

            for user_id in user_ids:
                if user_id in qualified_states_data:
                    name, level, num_states, states = qualified_states_data[user_id]
                    writer.writerow([user_id, name, level, num_states, ', '.join(states)])
                    logging.info(f"Exported data for {name}.")
        
        logging.info(f"\nData successfully exported to {filename}")
    except Exception as e:
        logging.error(f"Error exporting data: {e}")


# Main program loop
def main():
    global qualified_states_data
    
    # Load the latest data from the CSV file at the start
    qualified_states_data = load_data_from_csv()

    # Reassign IDs on startup to ensure they're sequential
    reassign_user_ids()

    try:
        while True:
            # Reload the CSV data at the start of every loop iteration to ensure fresh data is used
            qualified_states_data = load_data_from_csv()

            # Reassign IDs to ensure no gaps
            reassign_user_ids()

            action = input("\nWould you like to (V)iew, (M)odify, (E)xport, (A)dd, (R)emove, (S)ave, or (X) revert? (Type 'exit' to quit): ").lower().strip()

            if action == "exit":
                break
            elif action == "v":
                display_all_users()
                user_ids = get_user_ids()
                view_user_assignments(user_ids)
            elif action == "m":
                display_all_users()
                user_ids = get_user_ids()
                for user_id in user_ids:
                    modify_action = input(f"Would you like to (A)dd or (R)emove a state for user {user_id}? ").lower().strip()
                    if modify_action in ["a", "r"]:
                        modify_user_state(user_id, "add" if modify_action == "a" else "remove")
                    else:
                        logging.warning("Invalid action. Please choose (A)dd or (R)emove.")
            elif action == "e":
                display_all_users()
                user_ids = get_user_ids()
                filename = input("Enter the filename for the CSV (default is 'exported_users.csv'): ").strip() or 'exported_users.csv'
                export_users_to_csv(user_ids, filename)
            elif action == "a":
                add_user()
            elif action == "r":
                display_all_users()
                user_ids = get_user_ids()
                for user_id in user_ids:
                    remove_user(user_id)
            elif action == "x":
                revert_to_backup()
            elif action == "s":
                # Manual Save Option
                save_data_to_csv()
                logging.info("Data manually saved to CSV.")
            else:
                logging.warning("Invalid action. Please choose (V)iew, (M)odify, (E)xport, (A)dd, (R)emove, (S)ave, or (X) revert.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
