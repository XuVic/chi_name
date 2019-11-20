import unittest
from lib.google_sheet_api import create_credentials
from lib.google_sheet_api.api_gateway import ApiGateway
import pdb

class GoogleSheetTest(unittest.TestCase):
    def setUp(self):
        self.gateway = ApiGateway(create_credentials())

    def test_get_names(self):
        sheet_id = "1hkRdSGobwgv_Z22UunsvRnJHRNUMMthOw-wgTSstY0s"
        res = self.gateway.get_values(sheet_id, 'LastName', 1)
        pdb.set_trace()


if __name__ == "__main__":
    unittest.main()