from database.connection import (
  Model,
  UUIDField,
  CharField,
  DateField,
  conn,
)

print (conn.get_tables(), flush=True)

class User(Model):
  id       = UUIDField(index=True)
  email    = CharField(unique=True)
  name     = CharField()
  birthday = DateField()
  country  = CharField()
  password = CharField()

  class Meta:
    database = conn
