from marshmallow import (
  Schema,
  fields,
)

class SingUpSchema(Schema):
  email    = fields.Str(
    required=True
  )
  name     = fields.Str()
  birthday = fields.Date()
  country  = fields.Str()
  password = fields.Str(
    required=True
  )

  class Meta:
    strict = True

class SingInSchema(Schema):
  email    = fields.Str(
    required=True
  )
  password = fields.Str(
    required=True
  )

  class Meta:
    strict = True
