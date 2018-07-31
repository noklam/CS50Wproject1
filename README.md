# CS50Wproject1

## Description 

This project try to build a book search and review engine with Flask, PostgresSQL. Flask extension is avoid when possible and logic implemented with native python.

## Behaviors

1. Registration
2. Login
3. Logout
4. Import
5. Search
6. Book Page
7. Review Submission
8. Goodreads Review Data

7/20/2018:

* Add Register button
* Add Register Page

7/23/2018:

* Add Register Logic
* Add Login Logic
* Add Error page logic
* Add success.html
* Check empty form

7/25/2018:

* Add book() details
* Can Search mulitple books, each book have a href tag and lead to details of individual book.
* Call api() inside book() to retrieve data externally from API

7/29/2018:

* Add session["user_id"]
* Add Review function()
  
7/30/2018:

* Add logout button
* Logout button only appears when user is logined 
* Check User is logged in on every route

7/31/2018:

* Return no review when no user review is there
* Return no serach result instead of empty page when no book

Things to do

* Add no result route for search.
* User Review
* Hashing Password
* Add session["user_id"]
* Add Search function
* Book Page
* Review Submission
* API Access: If users make a GET request to your website’s /api/<isbn> route, where <isbn> is an ISBN number, your website should return a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. The resulting JSON should follow the format:

{
    "title": "Memory",
    "author": "Doug Lloyd",
    "year": 2015,
    "isbn": "1632168146",
    "review_count": 28,
    "average_score": 5.0
}
