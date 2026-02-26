from flask import *
import pymysql
import os

# initialize the app
app=Flask(__name__)
if not os.path.exists("static/images"):
    os.makedirs("static/images")

app.config["UPLOAD_FOLDER"]="static/images"

# sign up route or endpoint
@app.route("/api/signup",methods=["POST"])
def signup():
    # request inputs from a user
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]

    # connect to mysql databse
    connection=pymysql.connect(host="localhost",user="root",password="",database="mamba_sokogarden_abel")
    # create cursor
    cursor=connection.cursor()

    # sql staetment to indsert the records
    sql="insert into users(username,email,password,phone)values(%s,%s,%s,%s)"

    # prepare the data
    data=(username,email,password,phone)

    # execute/run 
    cursor.execute(sql,data)

    # commit
    connection.commit()

    # return a response

    return jsonify({"message":"Thank You for Joining"})

# signin API
# signin route
@app.route("/api/signin",methods=["POST"])
def signin():
    # request user input
    email=request.form["email"]
    password=request.form["password"]

    # create a connection
    connection=pymysql.connect(host="localhost",user="root",password="",database="mamba_sokogarden_abel")

    # create a cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # sql quelry statement to check the user
    sql="select * from users where email=%s and password=%s"

    # prepare the data
    data=(email,password)
    
    # excecute or run the query
    cursor.execute(sql,data)
    
    # response
    if cursor.rowcount==0:
        return jsonify({"Message":"Login failed"})
    else:
        user=cursor.fetchone()
        user.pop("password",None)
        return jsonify({"Message":"Login Successful","user":user})
    
# add product api
# CREATE A ROUTE
@app.route("/api/add_product",methods=["POST"])
def add_product():
    # request user data
    product_name=request.form["product_name"]
    product_description=request.form["product_description"]
    product_cost=request.form["product_cost"]
    product_photo=request.files["product_photo"]

    # extract photo name
    filename=product_photo.filename

    photo_path=os.path.join(app.config["UPLOAD_FOLDER"],filename)
    product_photo.save(photo_path)

    # create a connection
    connection=pymysql.connect(host="localhost",user="root",password="",database="mamba_sokogarden_abel")

    # create a cursor
    cursor=connection.cursor()

    # sql statement to insert the data
    sql=("insert into products_details(product_name,product_description,product_cost,product_phot" \
    "o)values(%s,%s,%s,%s)")

    # prepare data
    data=(product_name,product_description,product_cost,filename)

    # excecute/run
    cursor.execute(sql,data)

    # commit/save
    connection.commit()

    # run Response
    return jsonify({"message":"Product added successfully"})



 








































app.run(debug=True)