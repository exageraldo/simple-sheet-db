import gspread
from gspread.exceptions import SpreadsheetNotFound, WorksheetNotFound
from oauth2client.service_account import ServiceAccountCredentials


class SheetDB(object):
    def __init__(self, sheet_name, upsert=False, share=None, config_file='google-credentials.json'):
        self.sheet_name = sheet_name
        self._config = config_file
        self._scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/spreadsheets'
        ]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
            self._config,
            self._scope
        )
        self.client = gspread.authorize(self.creds)
        self.db_sheet = self._get_db(upsert=upsert)
        self._id = self.db_sheet.id 
        self.share_with(share)
    
    def shared_users(self):
        shared_users = [
            {
                'id': user['id'],
                'name': user['name'],
                'email': user['emailAddress'],
                'role': user['role'],
                'type': user['type']
            }
            for user in self.db_sheet.list_permissions()
            if not user['deleted']
        ]
        return shared_users

    def _get_db(self, upsert):
        try:
            return self.client.open(self.sheet_name)
        except SpreadsheetNotFound:
            if upsert:
                return self.client.create(self.sheet_name)
            raise
        except:
            raise
    
    def share_with(self, share):
        if isinstance(share, str):
            share = [share]
        if share:
            for email in share:
                self.db_sheet.share(
                    email,
                    perm_type='user',
                    role='reader'
                )