# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse

    
app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('distance')
parser.add_argument('devise')

@app.route('/')
def index():
    return render_template("Accueil.html")


class CalculPrix(Resource):
    def get(self):
        parser.add_argument('task')
        args = parser.parse_args()
        
        prix = float(args['distance']) * 0.25
        
        if args['devise'] == "euro" :
            prixtrain = prix * 1
        elif args['devise'] == "gbp" :
            prixtrain = prix * 0.8827;
        elif args['devise'] == "aud" :
            prixtrain = prix * 1.7592;
        elif args['devise'] == "usd" :
            prixtrain = prix * 1.0916;
        else:
            prixtrain = prix * 1;
                
        return {'prix' : prixtrain}

api.add_resource(CalculPrix, '/CalculPrix')
    
#app.run(debug='true')