import os

from flask import Flask, session,  render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
   
    users = db.execute("SELECT * FROM Users").fetchall()
    return render_template("index.html", users=users)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # User Validation
    login_success = db.execute("SELECT * FROM users WHERE username= :username and userpassword= :password", 
            {"username": username, "password":password}).fetchone()
    print('login success', login_success)
    if login_success:
        print("Login")
        print(f"Welcome {username}, you have login successfully!")
        return render_template("index.html", username=username)
    else:
        return render_template("error.html", message="something is wrong!")

@app.route("/registeration", methods=["GET"])
def registeration():
    return render_template("registeration.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")

    print(username, password, email)

    if not username or not password or not email:
        return render_template("error.html", message="Some of your field is empty!") 

    user = db.execute("SELECT * FROM users WHERE username = :username", 
            {"username": username}).fetchone()

    if user is not None:
        return render_template("error.html", message="This username is registered already.")
     
    try:
        db.execute("INSERT INTO USERS (UserName, UserPassword, Email) VALUES(:username, :password, :email)",
        {"username": username, "password": password, "email": email})
        db.commit() # Save the changes!
            
        # Registeration is finish.  
        return render_template("success.html")
        
    except: 
        print('something is wrong')
        return render_template("error.html","User registration fails!")

@app.route("/users")
def user():
    
    users = db.execute("SELECT username FROM Users").fetchall()
    return render_template("users.html",users = users)