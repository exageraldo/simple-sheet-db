import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/spreadsheets'
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'google-credentials.json',
    scope
)
client = gspread.authorize(creds)
db_sheet = client.create('Simple Sheet DB')
db_sheet.share(
    'you.email@here.com',
    perm_type='user',
    role='writer'
)
worksheet = db_sheet.get_worksheet(0)