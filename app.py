from flask import Flask
from flask_restful import Api
import urllib
from flask_sqlalchemy import SQLAlchemy
from db import db
from waitress import serve


app = Flask(__name__)
params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 11.0};SERVER=RS-SCRAPINGSER;DATABASE=Rent;Trusted_Connection=yes;")
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api = Api(app)
api.app.config['RESTFUL_JSON'] = {'ensure_ascii': False}

from resouorces import MyhomeFlatsAppartments_List
api.add_resource(MyhomeFlatsAppartments_List, '/')


if __name__ == "__main__":
    db.init_app(app)
    # app.run(host='37.46.104.139', port=80, debug=True)  #host='0.0.0.0', port=80,  --host='37.46.104.139', port=80, debug=True
    serve(app, host='37.46.104.139', port=80, threads=3)
