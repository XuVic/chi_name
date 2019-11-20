import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.user import User
from app.models.name import Name
import pdb

Session = sessionmaker()
engine = create_engine('sqlite:///config/db/test.db')


class UserTest(unittest.TestCase):
    def setUp(self):
        self.conn = engine.connect()
        self.trans = self.conn.begin()
        self.dbsession = Session(bind=self.conn)
    
    def test_create(self):
        user = User(messenger_id='12345678910')
        self.dbsession.add(user)
        self.assertIsNone(user.uuid)
        self.dbsession.commit()
        self.assertIsNotNone(user.uuid)

    def test_assoication(self):
        user = User(messenger_id='12345678901')
        name = Name(category='test', traditional='test1')
        user.names = [name]
        self.dbsession.add(user)
        self.dbsession.commit() 
        self.assertIsNotNone(user.uuid)
        self.assertIsNotNone(name.uuid)
        user.names.remove(name)
        self.dbsession.commit()
        self.assertNotIn(name, user.names)
        self.assertIsNotNone(name.uuid)

    def tearDown(self):
        self.dbsession.close()
        self.trans.rollback()
        self.conn.close()

if __name__ == "__main__":
    unittest.main()