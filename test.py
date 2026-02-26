from flask import *

# initialize the flask app
app=Flask(__name__)

# create route
@app.route("/api/home")
def home():
    return jsonify({"Message":"Welcome to home Api"})

# create the product route
@app.route("/api/product")
def product():
    return jsonify({"Messsage":"Welcome to Product api"})

# create the services route
@app.route("/api/services")
def services():
    return jsonify({"Message":"Welcome to our services API"})

# Route for adding two numbers
@app.route("/api/calc",methods=["POST"])
def calc():
    # request the data
    num1=request.form["num1"]
    num2=request.form["num2"]

    sum=int(num1) + int(num2)
    
    return jsonify({"Answer":sum})

# Route for multiplying two numbers
@app.route("/api/multiply",methods=["POST"])
def multiply():
    # request the data
    num1=request.form["num1"]
    num2=request.form["num2"]

    product=int(num1) * int(num2)
    
    return jsonify({"Answer":product})




 

app.run(debug=True)
