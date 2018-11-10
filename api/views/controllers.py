from flask import Blueprint, jsonify, request
from api.models.models import Parcel, parcel_orders
from api.validations import empty_order_fields, invalid_input_types, empty_strings_add_weight
from api.Handlers.error_handlers import InvalidUsage


parcel_blueprint = Blueprint("parcel", __name__)


@parcel_blueprint.route('/api/v1/parcel', methods=['POST'], strict_slashes=False)
def create_parcel():
    if request.content_type != "application/json":
        raise InvalidUsage("Invalid content type", 400)
    data = request.get_json()
    parcel_id = len(parcel_orders) + 1
    parcel_location = data.get('parcel_location')
    parcel_destination = data.get('parcel_destination')
    parcel_weight = data.get('parcel_weight')
    parcel_description = data.get('parcel_description')
    status = data.get('status')

    val = empty_order_fields(parcel_location, parcel_destination, parcel_weight, parcel_description, status)
    if val:
        raise InvalidUsage(val, 400)
    input_type = invalid_input_types(parcel_location, parcel_destination, parcel_weight, parcel_description, status)
    if input_type:
        raise InvalidUsage(input_type, 400)
    empty_strings = empty_strings_add_weight(parcel_location, parcel_destination, parcel_weight, parcel_description, status)
    if empty_strings:
        raise InvalidUsage(empty_strings, 400)

    order = Parcel(parcel_id, parcel_location, parcel_destination, parcel_weight, parcel_description, status)
    parcel_orders.append(order.to_dict())
    return jsonify({"message": "parcel successfully added"}), 201


@parcel_blueprint.route('/api/v1/parcel', methods=['GET'])
def get_all_parcel():
    if not parcel_orders:
        return jsonify({"message": "List is empty first post"})
    return jsonify({"orders": parcel_orders})


@parcel_blueprint.route('/api/v1/parcel/<int:parcel_id>', methods=['GET'])
def get_single_parcel(parcel_id):
    single = []
    for order in parcel_orders:
        if order['parcel_id'] == parcel_id:
            single.append(order)
            return jsonify(single), 200
        return jsonify({"message": "there is no such id"}), 400

