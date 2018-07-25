# CS50Wproject1

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



Thins to do
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
