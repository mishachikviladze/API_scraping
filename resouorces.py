from flask_restful import Resource
from models import MyhomeFlatsAppartments_model

class MyhomeFlatsAppartments_List(Resource):
    def get(self):
        items = [item.json() for item in MyhomeFlatsAppartments_model.find_all()]#[:3]
        return {'items': items}, 200
        # return {'data':'the data from API'}
