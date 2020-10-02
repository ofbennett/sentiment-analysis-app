from marshmallow import Schema, fields, validate
from marshmallow import ValidationError

class ModelInputSchema(Schema):
    text = fields.Str(required=True, allow_none=False, validate=validate.Length(min=1,max=1000))
    pred_type = fields.Str(required=True, allow_none=False, validate=validate.OneOf(['hard','soft']))

def validate_input_data(input_data):
    schema = ModelInputSchema()

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages
    return errors