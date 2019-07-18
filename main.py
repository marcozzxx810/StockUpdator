import module

title = """
 *       _____ _             _    _    _           _       _             
 *      / ____| |           | |  | |  | |         | |     | |            
 *     | (___ | |_ ___   ___| | _| |  | |_ __   __| | __ _| |_ ___  _ __ 
 *      \___ \| __/ _ \ / __| |/ / |  | | '_ \ / _` |/ _` | __/ _ \| '__|
 *      ____) | || (_) | (__|   <| |__| | |_) | (_| | (_| | || (_) | |   
 *     |_____/ \__\___/ \___|_|\_\\____/| .__/ \__,_|\__,_|\__\___/|_|   
 *                                      | |                              
 *                                      |_|                              
 ========================================================================
"""

functionlist = """

A. Initialize the spreadsheet
B. Update the spreadsheet accroding to date and time
C. Modify the spreadsheet
D. Delete the change for the spreadsheet
E. View the profit/loss
F. Change the spreadsheet
G. Create new stock log
H. Exit
                     
 ========================================================================
"""
# Print out the title text 
print(title)

if (module.Login() == True) :
    # Print out the function list text 
    print(functionlist)
    # Check Sheet is selected or not 
    if module.google_sheet.currentworking is None :
        module.SelectSheet()
        while ( True ):
            mode = str(input("Please select the function : "))
            if mode == "A" :
                # Initialize the spreadsheet
                print("FOR DEBUG USE")
            elif mode == "B" :
                # Update the spreadsheet accroding to date and time
                print("FOR DEBUG USE")
            elif mode == "C" :
                # Modify the spreadsheet
                print("FOR DEBUG USE")
            elif mode == "D" :
                # Delete the change for the spreadsheet
                print("FOR DEBUG USE")
            elif mode == "E" :
                # View the profit/loss
                print("FOR DEBUG USE")
            elif mode == "F" :
                # Change the spreadsheet
                print("FOR DEBUG USE")
            elif mode == "G" :
                # Create new stock log
                print("FOR DEBUG USE")
            elif mode == "H" :
                # Exit
                print("FOR DEBUG USE")
                break
            else :
                print("Wrong mode is selected")
                continue
else:
    exit()