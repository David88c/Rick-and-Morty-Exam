import csv
import json
from flask import Flask

app = Flask(__name__)# Create an instance of the Flask class


@app.route('/')# Define the route for the root URL
def characters():
    with open('characters.csv', newline='') as csvfile:# Open the CSV file in read mode
        reader = csv.DictReader(csvfile)# Create a DictReader object to read the CSV file
        data = [row for row in reader]# Read each row in the CSV file and store it in a list
        return data# Return the list of rows as the response
    
@app.route('/healthcheck')# Define the route for the /healthcheck URL
def healthcheck():
    return "alive"# Return a simple string indicating the service is alive