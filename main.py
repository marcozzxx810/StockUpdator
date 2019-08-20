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
B. Select spreadsheet
C. Select stock number
D. Update spreadsheet
E. Delete the change for the spreadsheet
F. View the profit/loss
G. Change the spreadsheet
H. Create new stock log
I. Exit
                     
 ========================================================================
"""
# Print out the title text 
print(title)

if (module.Login() == True) :
    # Print out the function list text 
    print(functionlist)
    # Check Sheet is selected or not 
    while ( True ):
        if module.google_sheet.currentworking is None :
            print ("Current Working Spreadsheet : NONE")
            print("Please Initialize spreadsheet or select spreadsheet")
        else :
            print ("Current Working Spreadsheet : " , end = " ")
            print (module.google_sheet.currentworking)
            print ("Current Working StockNumber : " , end = " ")
            print (module.google_sheet.worksheet)
        mode = str(input("Please select the function : "))

        if mode == "A" :
            # Initialize the spreadsheet
            module.CreateNewSheet()
            print("FOR DEBUG USE")
        elif mode == "B" :
            # Select spreadsheet
            module.SelectSheet()
            print("FOR DEBUG USE")
        elif mode == "C" :
            # Select stock number 
            module.SelectStockNumber()
            print("FOR DEBUG USE")
        elif mode == "D" :
            # Update spreadsheet
            module.UpdateData()
            print("FOR DEBUG USE")
        elif mode == "E" :
            # Delete the change for the spreadsheet
            print("FOR DEBUG USE")
        elif mode == "F" :
            # View the profit/loss
            print("FOR DEBUG USE")
        elif mode == "G" :
            # Change the spreadsheet
            print("FOR DEBUG USE")
        elif mode == "H" :
            # Create new stock log
            print("FOR DEBUG USE")
        elif mode == "I" :
            # Exit
            print("FOR DEBUG USE")
            break
        else :
            print("Wrong mode is selected")
            continue
