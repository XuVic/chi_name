from . import create_credentials
from .values_wrapper import ValuesWrapper
from googleapiclient.discovery import build

class ApiGateway():
    def __init__(self, creds):
        self.service = build('sheets', 'v4', credentials=creds)
        self.sheet = self.service.spreadsheets()

    def get_values(self, sheet_id, page, row):
        range = self.__range(page, row)
        result = self.sheet.values().get(spreadsheetId=sheet_id,
                                range=range).execute()
        values = result.get('values', [])
        return ValuesWrapper(values)


    def __range(self, page, row):
        return "{}!A{}:Z".format(page, row)