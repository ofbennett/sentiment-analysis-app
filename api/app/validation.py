from marshmallow import Schema, fields, validate
from marshmallow import ValidationError

class ModelInputSchema(Schema):
    text = fields.Str(required=True, allow_none=False, validate=validate.Length(min=1,max=1000))

def validate_input(input_data):
    schema = ModelInputSchema()

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages
    return errors