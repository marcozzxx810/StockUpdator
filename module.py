import gspread
from oauth2client.service_account import ServiceAccountCredentials
class google_sheet:
    currentworking = None

def Login():
    try :
        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

        client = gspread.authorize(creds)
        return(True)
    except :
        print("Login Failure")
        return(False)

def SelectSheet():
    print("Please Select Sheet :", end="")
    google_sheet.currentworking = str(input())