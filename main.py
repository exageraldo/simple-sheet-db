import gspread
from gspread.exceptions import SpreadsheetNotFound
from oauth2client.service_account import ServiceAccountCredentials


def connect_to(table, share_with=None, filename='google-credentials.json'):
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file',
        'https://www.googleapis.com/auth/spreadsheets'
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        filename,
        scope
    )
    client = gspread.authorize(creds)

    try:
        db_sheet = client.open(table)
    except SpreadsheetNotFound:
        db_sheet = client.create(table)

    if share_with:
        db_sheet.share(
            share_with,
            perm_type='user',
            role='reader'
        )
    ws_table = db_sheet.sheet1
    return ws_table
