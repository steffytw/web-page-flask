# importing packages
from flask import Flask ,render_template, redirect, url_for, session, request, logging
#import requests
#import json

app = Flask(__name__) #app initialisation
@app.route('/logout', methods=['GET','POST'])
def logout():
	return render_template("index.html")
@app.route('/', methods=['GET','POST']) #landing page intent
def home():
	username="admin@admin.com"
	password="admin"
	if request.method=='POST':
		email =request.form['email']
		password_candidate=request.form['password']
		if username==email and password==password_candidate:
			return render_template("home.html")
		print(email,password)
	return render_template("index.html") #display the html template

if __name__=='__main__':
	app.run(debug=True,host="localhost",port=8000) 
    #use threaded=True instead of debug=True for production
    # use port =80 for using the http port



#sample code for form data recieve
# request.form['name']
# Sample Code for JSON send data to api

#url = 'URL_FOR_API'
#data = {'TimeIndex':time1 ,'Name':name,'PhoneNumber':phone}
#headers = {'content-type': 'application/json'}
#r=requests.post(url, data=json.dumps(data), headers=headers)
#data = r.json()
#print(data)


#Sample code for JSON recieve data from API

#url = 'URL_FOR_API'
#headers = {'content-type': 'application/json'}
#r=requests.get(url, headers=headers)
#data = r.json()
#count = data['Count']