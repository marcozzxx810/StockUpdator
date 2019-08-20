import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

class google_sheet:
    currentworking = None
    worksheet = None 

def Login():
    try :
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

        global client

        client = gspread.authorize(creds)
        return(True)
    except :
        print("Login Failure")
        return(False)

def CreateNewSheet():
    print("New SpreadSheet Name :", end="")
    SheetName = str(input())
    google_sheet.currentworking = client.create( SheetName ) 
    google_sheet.currentworking.share('marcowingwing@gmail.com', perm_type='user', role='writer')

    print("How many number of Stocks:", end="")
    N_stocks = int(input())

    for i in range(N_stocks):
        print("Stock number :", end="")
        StockName = str(input())
        google_sheet.worksheet = google_sheet.currentworking.add_worksheet(title=StockName , rows="100", cols="20")

        google_sheet.worksheet.update_acell('A1', '日期')
        google_sheet.worksheet.update_acell('B1', '股數')
        google_sheet.worksheet.update_acell('C1', '市價')
        google_sheet.worksheet.update_acell('D1', '市值')

def SelectStockNumber():
    print("Please Select StockNumber :", end="")
    StockNumber = str(input())
    google_sheet.worksheet = google_sheet.currentworking.worksheet(StockNumber)

def SelectSheet():
    print("Please Select Sheet :", end="")
    SheetName = str(input())
    google_sheet.currentworking = client.open( SheetName )
    google_sheet.worksheet = google_sheet.currentworking.get_worksheet(0)
    SelectStockNumber()

def UpdateData():
    print("Buying Year : ", end="")
    Year = int(input())
    print("Buying Month : ", end="")
    Month = int(input())
    print("Buying Day : ", end="")
    Day = int(input())
    print("How many stocks : ", end="")
    n_stocks = str(input())
    print("buy value : ", end="")
    value = str(input())
    date = datetime(Year, Month, Day)
    str_date = date.strftime("%d/%m/%Y")
    print(str_date)
    Date_List = google_sheet.worksheet.col_values(1)
    print(Date_List)
    google_sheet.worksheet.update_cell(len(Date_List)+1, 1, str_date)
    google_sheet.worksheet.update_cell(len(Date_List)+1, 2, n_stocks)
    google_sheet.worksheet.update_cell(len(Date_List)+1, 3, value)
