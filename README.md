Instructions for Use:
---------------------------
1.Purpose of the Program: This program manages users and their assigned states. 
			You can view, modify, export, add, remove users and their states, or revert to the previous saved version using a simple menu interface.

---------------------------
2.The CSV file structure should be:
---------------------------
|user_id|     | name|     | # of states assigned|   | state(s)|
  |1|      AMAYA CARTAGENA|     | 19|             |Arizona, Florida, Indiana, Kentucky, etc.

---------------------------
3.Running the Program:
---------------------------
-Open "state_routing" .exe file/application

-A menu will appear prompting you with options to choose from.
---------------------------
4.Menu Options:
---------------------------
-(V)iew: Displays a list of all users and their assigned states. You can select specific users or all users to view their state assignments.
-(M)odify: Allows you to modify a user’s state assignments (add or remove states). You can choose a user by their user ID and either add or remove states.
-(E)xport: Exports the selected users' state assignments to a CSV file.
-(A)dd: Adds a new user with their state assignments. You will need to provide the user’s name and states.
-(R)emove: Removes a user by their user ID.
-(X) Revert: Reverts the user data to the last saved version by restoring from a backup.
---------------------------
5.Adding or Removing States:
---------------------------
-When prompted to add or remove states, you can input multiple state abbreviations or full names, separated by commas.

Example:
To add: FL, TX, CA

To remove: Florida, Texas
---------------------------
6.Data Management:
---------------------------
-Each time you save data, a timestamped version of the CSV file is created.

Example: qualified_states_data_20240904_165141.csv
The backup file qualified_states_data_backup.csv is used for the "revert" option, allowing you to restore the previous state of the data.
---------------------------
7.Exiting the Program:
---------------------------
To exit the program, simply type exit at any prompt.
---------------------------
8.Error Handling:
---------------------------
The program will catch and display any errors that occur, pausing before exit to allow you to view the error message.
---------------------------

***IMPORTANT NOTES***

---------------------------

-Make sure the CSV file (qualified_states_data.csv) is in the same folder as the .exe file.
 This ensures the program can read and write to the CSV file as expected.

