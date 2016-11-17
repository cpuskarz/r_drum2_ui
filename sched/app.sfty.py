import json
import urllib
import requests
from flask import Flask, render_template, request
import os

__author__ = 'cpuskarz'

app = Flask(__name__)

APPSERVER = "http://127.0.0.1:5002"

@app.route('/')
def drummer_list():
    u = APPSERVER + "/options"
    page = requests.get(u)
    options = page.json()
    drummer_list = options["options"]
    return render_template('home.html', drummer_list=drummer_list)
    
@app.route("/about")
def about():
    return render_template('about.html', title="About")

'''
@app.route("/results")
def results():
    # Check for submitted vote
    seldrummer = request.args.get('drummer')
    seldrummer = seldrummer.replace(" ", "")
    seldrummer = seldrummer.lower()
    u = urllib.urlopen(APPSERVER + "/"+ seldrummer)
    page = u.read()
    resp = json.loads(page)
    return resp
'''
# following works - dont delete
'''
@app.route("/results", methods=["GET"])
def res():
    pick = request.args.get('drummer')
    pick = pick.replace(" ", "")
    pick = pick.lower()
    u = requests.post(APPSERVER + "/" + pick)
    page = u.content
    resp = json.loads(page)
    return resp
'''

'''
@app.route("/pit", methods=["GET"])
def pit():
    u = requests.post(APPSERVER + "/chetcarello")
    print u.content
    return u.content
'''

# trying to send payload to app server with POST
@app.route("/results", methods=["GET"])
def respick():
    drumman = request.args.get('drummer')
    drumman = drumman.replace(" ", "")
    drumman = drumman.lower()
    u = requests.post(APPSERVER + "/mess", data=drumman)
    page = u.content
    #resp = json.loads(page)
    #return resp
    return page

if __name__ == '__main__':
    #APPSERVER = os.getenv('app_server')
    app.run(debug=True, host='0.0.0.0')
