
def check_fields_existance_in_payload(payload, *fields):
    if all(key in payload for key in fields):
        return True
