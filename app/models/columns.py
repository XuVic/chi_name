import datetime
import hashlib
import sqlalchemy as sa

def generate_uuid():
    time_now = str(datetime.datetime.utcnow())
    time_now_bytes = bytes(time_now, 'ascii')
    digest = hashlib.sha224(time_now_bytes).hexdigest()
    return digest

def uuid():
    return sa.Column('uuid', sa.String(100), primary_key=True, default=generate_uuid)

def timestamp():
    return sa.Column('timestamp', sa.DateTime, server_default=sa.text('NOW()'))