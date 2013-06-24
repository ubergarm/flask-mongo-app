#!/usr/bin/python

from flask import Flask, render_template, url_for
from flask import Response
from flask.ext.pymongo import PyMongo
import json, os, datetime

app = Flask(__name__)

##alternate db config settings
app.config['MONGO_DBNAME'] = 'app_db'
#app.config['MONGO_HOST'] = 'localhost'
#app.config['MONGO_PORT'] = 27017
#app.config['MONGO_USERNAME'] = 'flask'
#app.config['MONGO_PASSWORD'] = 'flask123'
mongo = PyMongo(app, config_prefix='MONGO')

@app.route("/")
def home():
    links = []
    links.append({'title':'Show city data on a js map', 'url':url_for('city_by_zip',zipcode='47586')})
    links.append({'title':'Insert values into db and print collection.',
'url':url_for('db_insert', val=42)})
    #return Response(str(url_for(city_by_zip))
    return render_template('home.html', links=links)

#example javascript interaction with mongodb
@app.route("/city_by_zip/<zipcode>")
def city_by_zip(zipcode):
    #cursor = mongo.db.zips.find({ '_id' : '47586' })
    #cursor = mongo.db.zips.find({ 'state' : 'WY' })
    cursor = mongo.db.zips.find({ '_id' : zipcode })
    #records = [record for record in cursor]
    records = list(cursor)
    return render_template('city_by_zip.html', records=records)

@app.route("/db_insert/<int:val>")
def db_insert(val):
    mongo.db.collection.save({'datetime': datetime.datetime.utcnow(), \
                              'value':val})
    items = list(mongo.db.collection.find())
    result = 'Quick and dirty example of a RESTful db insertion.\r\n'
    result += 'Try adding your favorite integer in the URL.\r\n'
    result += 'Use back button to return to main menu when done.\r\n\r\n'
    result += 'Found {0} items in {1}.collection:\r\n'.format(len(items), mongo.db.name)
    for item in items:
        result += json.dumps(str(item))+'\r\n'
    return Response(result, mimetype='application/json')

#handle 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
