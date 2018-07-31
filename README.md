# CS50Wproject1

## Description 

This project try to build a book search and review engine with Flask, PostgresSQL. Flask extension is avoid when possible and logic implemented with native python.

## Behaviors

1. Registration: Users  able to register for your website, providing (at minimum) a username and password.
2. Login: Users, once registered, should be able to log in to your website with their username and password.
3. Logout: Logged in users should be able to log out of the site.
4. Import: run python import.py should be able to import books.csv into a PostresSQL provided that environment variables are set up correctly. You need to run create.sql in your database to create the schema for tables first. Books.csv, which is a spreadsheet in CSV format of 5000 different books. Each one has an ISBN nubmer, a title, an author, and a publication year. 
5. Search: Once a user has logged in, they should be taken to a page where they can search for a book. Users should be able to type in the ISBN number of a book, the title of a book, or the author of a book. After performing the search, your website should display a list of possible matching results, or some sort of message if there were no matches. If the user typed in only part of a title, ISBN, or author name, your search page should find matches for those as well!
6. Book Page: When users click on a book from the results of the search page, they should be taken to a book page, with details about the book: its title, author, publication year, ISBN number, and any reviews that users have left for the book on your website.
7. Review Submission: On the book page, users should be able to submit a review: consisting of a rating on a scale of 1 to 5, as well as a text component to the review where the user can write their opinion about a book. Users should not be able to submit multiple reviews for the same book.
8. Goodreads Review Data: On your book page, you should also display (if available) the average rating and number of ratings the work has received from Goodreads.
9. API Access: If users make a GET request to your website’s /api/<isbn> route, where <isbn> is an ISBN number, your website should return a JSON response containing the book’s title, author, publication date, ISBN number, review count, and average score. The resulting JSON should follow the format:

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
* Edit Logout, back button css style
* Clean up unuse code

Things to do

* Hashing Password

