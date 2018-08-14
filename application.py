import os

from flask import Flask, session,  render_template, request, jsonify
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests

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



def api(isbn):
    # isbn = "9781632168146" # for testing
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": os.environ.get('GOODREADKEY'), "isbns": isbn})
    return res.json()
@app.route("/")
def index():

    users = db.execute("SELECT * FROM Users").fetchall()
    return render_template("index.html", users=users)


@app.route("/api/<int:isbn>")
def api_request(isbn):
    return str(api(isbn))
    # isbn = "9781632168146" # for testing
    # res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": os.environ.get('GOODREADKEY'), "isbns": isbn})

    # return str(res.json())

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # User Validation
    user = db.execute("SELECT * FROM users WHERE username= :username and userpassword= :password",
                               {"username": username, "password": password}).fetchone()
    print('login success', user)
    if user:
        print("Login")
        print(f"Welcome {username}, you have login successfully!")

        user_id, user_name,user_password,user_email = user
        session['user_id'] = user_id
        session['user_name'] = user_name
        session['user_email'] = user_email
        
        return render_template("search.html", username=username)
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

    # print(username, password, email)
    if not username or not password or not email:
        return render_template("error.html", message="Some of your field is empty!")

    user = db.execute("SELECT * FROM users WHERE username = :username",
                      {"username": username}).fetchone()

    if user is not None:
        return render_template("error.html", message="This username is registered already.")

    try:
        db.execute("INSERT INTO USERS (UserName, UserPassword, Email) VALUES(:username, :password, :email)",
                   {"username": username, "password": password, "email": email})
        db.commit()  # Save the changes!

        # Registeration is finish.
        return render_template("success.html")

    except:
        print('something is wrong')
        return render_template("error.html", "User registration fails!")


# @app.route("/users")
# def user():

#     users = db.execute("SELECT username FROM Users").fetchall()
#     return render_template("users.html", users=users)

@app.route("/search", methods=["POST"])
def search():
    title = request.form.get("title")
    isbn = request.form.get("isbn")
    author = request.form.get("author")

    if not (title or isbn or author):
        return ("no paramter? at least one please")
    else:
        results = db.execute("SELECT title, isbn, author FROM BOOKS WHERE (:title IS NULL OR title LIKE '%' || :title || '%') AND (:isbn IS NULL OR isbn LIKE '%' || :isbn ||'%') AND (:author IS NULL OR author LIKE '%'||:author||'%')",
        {"author":author, "isbn":isbn, "title":title}).fetchall()
        # raise
    return render_template("books.html", books=results)


# @app.route("/books")
# def books():
#     """Lists all books."""
#     print("books function")
#     books = db.execute("SELECT * FROM books").fetchall()
#     raise
#     print(books)
#     return render_template("books.html", books=books)


@app.route("/books/<isbn>", methods=["GET"])
def book(isbn):
    """Lists details about a single book."""
    if not validate_login():
        return render_template("error.html", message="Please login first.")
    # Make sure book exists.
    book = db.execute("SELECT * FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()
    if book is None:
        return render_template("error.html", message="No such book.")
    book_api = api(isbn)['books'][0]
    
    book = dict(book)
    # raise
    book['reviews_count'], book['average_rating'] = "",""
    
    if book_api.get('reviews_counts'):
            book['reviews_count'] = book_api.get('reviews_count')
    if book_api.get('average_rating'):
       book['average_rating'] = book_api.get('average_rating')

    # raise
    # set session for book, which can be used for review()
    session['book_id'] = book['bookid']
    session['book_title'] = book['title']
  
    return render_template("book.html", book=book)


@app.route("/review", methods=["POST"])
def review():
    rating = request.form.get("rating")
    review_content = request.form.get("review_content")
    user_id = session.get('user_id', 'not set')
    book_id = session.get('book_id', 'not set')

    print(rating, review_content, user_id, book_id)
    print(">>" * 20)
    if not (rating and review_content and user_id and book_id):
        return render_template("error.html", message="Some of your field is empty!")
    
    user_review = db.execute("SELECT * FROM reviews WHERE userkey = :userkey",
                      {"userkey": user_id}).fetchone()
    print("**" * 20)    
    print('user_review:',user_review)
    if user_review is not None:
        return render_template("error.html", message="You have already submitted a review")
    
    try:
        db.execute("INSERT INTO REVIEWS (UserKey, BookKey, Review) VALUES(:userkey, :bookkey, :review_content)",
                   {"userkey": user_id, "bookkey": book_id, "review_content": review_content})
        db.commit()  # Save the changes!

        # Registeration is finish.
        return render_template("success.html")

    except:
        print('something is wrong')
        return render_template("error.html", message="User registration fails!")
    return "PASS"




@app.route('/get/')
def get():
    tmp = session.get('user_id', 'not set')
    return str(tmp)


def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

@app.route("/logout", methods=["POST"])
def logout():
    session['user_id'] = ""
    session['user_name'] = ""
    try:
        return render_template("logout.html", message="You have logout successfully")
    except:
        return render_template("error.html", message="something is wrong, logout failed")    
        

def validate_login():
    """ A boolean variable indicate user is login"""
    return session['user_id'] != ""
       
