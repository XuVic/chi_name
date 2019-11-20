import unittest
from app import create_app
from app.models import Name
import pdb

class NameControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app(env='test')
        self.app.testing = True
        self.client = self.app.test_client()
        self.dbsession = self.app.dbsession()

    def test_create(self):
        name_data = dict(category='first_name', traditional='林')
        res = self.client.post('/names', data=name_data)
        self.assertIn('200', res.status)
        names = self.dbsession.query(Name).all()[0]
        self.assertIsNotNone(names.uuid)

    def test_update_from_sheet(self):
        res = self.client.put("/names/1hkRdSGobwgv_Z22UunsvRnJHRNUMMthOw-wgTSstY0s")
        names = self.dbsession.query(Name).all()
        self.assertGreater(len(names), 1)
        self.assertIn('200', res.status)
    
    def test_match_name(self):
        self.client.put("/names/1hkRdSGobwgv_Z22UunsvRnJHRNUMMthOw-wgTSstY0s")
        res = self.client.get("/names?last_name=jashon&first_name=1995")
        # pdb.set_trace()
        self.assertIn('黃', res.data.decode())


    def tearDown(self):
        self.dbsession.query(Name).delete()
        self.dbsession.commit()

if __name__ == "__main__":
    unittest.main()