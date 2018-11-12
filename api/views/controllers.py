from flask import Blueprint, jsonify, request
from api.models.models import Parcel
from api.validations import empty_order_fields, invalid_input_types, empty_strings_add_weight
from api.Handlers.error_handlers import InvalidUsage

parcel_blueprint = Blueprint("parcel", __name__)


@parcel_blueprint.route('/api/v1/parcel', methods=['POST'], strict_slashes=False)
def create_parcel():
    if request.content_type != "application/json":
        raise InvalidUsage("Invalid content type..--...gkjljlkjlkj.", 400)
    data = request.get_json()
    parcel_id = len(Parcel.parcel_orders) + 1
    parcel_location = data.get('parcel_location')
    parcel_destination = data.get('parcel_destination')
    parcel_weight = data.get('parcel_weight')
    parcel_description = data.get('parcel_description')
    user_id = data.get('user_id')
    status = data.get('status')

    val = empty_order_fields(parcel_location, parcel_destination, parcel_weight, parcel_description, user_id, status)
    if val:
        raise InvalidUsage(val, 400)
    input_type = invalid_input_types(parcel_location, parcel_destination, parcel_weight, parcel_description, user_id, status)
    if input_type:
        raise InvalidUsage(input_type, 400)
    empty_strings = empty_strings_add_weight(parcel_location, parcel_destination, parcel_weight, parcel_description, user_id, status)
    if empty_strings:
        raise InvalidUsage(empty_strings, 400)

    order = Parcel(parcel_id, parcel_location, parcel_destination, parcel_weight, parcel_description, user_id, status)
    Parcel.parcel_orders.append(order.to_dict() )
    return jsonify({"message": "parcel successfully added ", "data": order.to_dict()}), 201


@parcel_blueprint.route('/api/v1/parcel', methods=['GET'], strict_slashes=False)
def get_all_parcel():
    if not Parcel.parcel_orders:
        return jsonify({"message": "List is empty first post"})
    return jsonify({"orders": Parcel.parcel_orders})


@parcel_blueprint.route('/api/v1/parcel/<int:parcel_id>', methods=['GET'], strict_slashes=False)
def get_single_parcel(parcel_id):
    for order in Parcel.parcel_orders:
        if order['parcel_id'] == parcel_id:
            return jsonify({"message": "your request is successfull", "data": order}), 200
    return jsonify({"message": "there is no such id"}), 400


@parcel_blueprint.route('/api/v1/parcel/<int:parcel_id>/cancel', methods=['PUT'], strict_slashes=False)
def cancel_parcel(parcel_id):
    for order in Parcel.parcel_orders:
        if order['parcel_id'] == parcel_id:
            order['status'] = 'cancelled'
            return jsonify(order), 200
    return jsonify({"message": "there is no such id"}), 400


@parcel_blueprint.route('/api/v1/users/<int:user_id>/parcel', methods=['GET'], strict_slashes=False)
def get_parcel_by_user_id(user_id):
    single = []
    for order in Parcel.parcel_orders:
        if order['user_id'] == user_id:
            single.append(order)

    if len(single) > 0:
        return jsonify(single), 200
    return jsonify({"message": "there is no such user"}), 400


@parcel_blueprint.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

