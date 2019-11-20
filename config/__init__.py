class Config(object):
    TEST=False
    SECRET_KEY='asdfsatkwlqj'

from .development import Development
from .test import Test
from .production import Production