

parcel_orders = []


class Parcel:
    def __init__(self, parcel_id, parcel_location, parcel_destination, parcel_weight, parcel_description, status):
        self.parcel_id = parcel_id
        self.parcel_location = parcel_location
        self.parcel_destination = parcel_destination
        self.parcel_weight = parcel_weight
        self.parcel_description = parcel_description
        self.status = status

    def to_dict(self):
        """A method to Convert the parcel instance to a dictionary"""
        parcel = {
            'parcel_id': self.parcel_id,
            'parcel_location': self.parcel_location,
            'parcel_destination': self.parcel_destination,
            'parcel_weight': self.parcel_weight,
            'parcel_description': self.parcel_description,
            'status': self.status
        }
        return parcel
