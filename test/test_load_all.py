from app import create_app
from app.models import *
from lib.google_sheet_api import api_gateway, create_credentials

if __name__ == "__main__":
    app = create_app(env="development")
    dbsession = app.dbsession()
    g_sheet_api = api_gateway.ApiGateway(create_credentials())
    sheet_id = "1hkRdSGobwgv_Z22UunsvRnJHRNUMMthOw-wgTSstY0s"