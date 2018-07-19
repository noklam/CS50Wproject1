import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO Books (Isbn, Title, Author, Year) VALUES (:isbn, :title, :author, :year)",
                    {"isbn": isbn, "title": title, "author": author, "year": year})
        print(f"{isbn},{title},{author},{year}")
    db.commit()

if __name__ == "__main__":
    main()
