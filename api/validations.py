
def empty_order_fields(parcel_location, parcel_destination, parcel_weight, parcel_description, status):
    error = {}
    if not parcel_location:
        error['parcel_location'] = 'parcel location field is missing'
    if not parcel_destination:
        error['parcel_destination'] = 'parcel destination field is missing'
    if not parcel_weight:
        error['parcel_weight'] = 'parcel weight can not be empty'
    if not parcel_description:
        error['parcel_description'] = 'parcel description field is missing'
    if not status:
        error['status'] = 'parcel status field is missing'
    return error


def invalid_input_types(parcel_location, parcel_destination, parcel_weight, parcel_description, status):
    error = {}
    if not isinstance(parcel_location, str):
        error['parcel_location'] = 'should be a string'
    if not isinstance(parcel_destination, str):
        error['parcel_destination'] = 'should be a string'
    if not isinstance(parcel_weight, int):
        error['parcel_weight'] = 'should be an integar'
    if not isinstance(parcel_description, str):
        error['parcel_location'] = 'should be a string'
    if not isinstance(status, str):
        error['status'] = 'status should be a string'
    return error


def empty_strings_add_weight(parcel_location, parcel_destination,parcel_weight, parcel_description, status):
    error = {}
    if parcel_location == " ":
        error['parcel_location'] = 'parcel location can not be parced empty string'
    if parcel_destination == " ":
        error['parcel_destination'] = 'parcel destination can not be parced empty string'
    if parcel_description == " ":
        error['parcel_description'] = 'parcel description can not be parced empty string'
    if status == " ":
        error['status'] = 'parcel status can not be parcel empty string'
    if parcel_weight < 0:
        error['parcel_weight'] = 'weight cant be less than 0'
    return error
