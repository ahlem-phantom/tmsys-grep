import secrets


def extract_field_from_body(field, body):
    return body[field] if field in body else None
