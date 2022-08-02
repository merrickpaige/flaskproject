import requests
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, session, render_template, redirect, request, flash

from flask_sqlalchemy import SQLAlchemy
#import sqlalchemy
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import SQLAlchemy
#from forms import RegistrationForm, LoginForm
#import app
#from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine





app = Flask(__name__)
#app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
engine = create_engine("postgres://flcrppqronzaiv:31e2c6fa39f87c156f832683cc9bdac9f11501744139019bc240dfa84b6d1d16@ec2-34-224-229-81.compute-1.amazonaws.com:5432/dch0qq8kl47h7m")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = scoped_session(sessionmaker(bind=engine))

#app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://flcrppqronzaiv:31e2c6fa39f87c156f832683cc9bdac9f11501744139019bc240dfa84b6d1d16@ec2-34-224-229-81.compute-1.amazonaws.com:5432/dch0qq8kl47h7m"

db = SQLAlchemy(app)




# goodreads KEY
#
key = "sMGJFtPjhyHmuaybhB598g"

@app.route("/", methods=["POST", "GET"])
#@login_required
def index():

    return render_template("index.html")


#@app.route("/", methods=["POST", "GET"])
@app.route("/book", methods=["GET","POST"])
def book():

    if request.method == "POST":
        search = request.form.get("search")


         #return render_template("index.html", )
        return render_template("book.html", books=search, search=search)

        if search != "":
            search_result = db.execute("SELECT * FROM books WHERE LOWER(isbn) LIKE :book OR title LIKE :book OR author LIKE :book", {"book": '%'+search+'%'}).fetchall()
            if not search_result:
                message = "No Books ware found. Please search again"
                return render_template("book.html", message=message, search=search)

            for book in search_result:
                isbn = book[1]
               # goodreadsapi(isbn)
                # res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": isbn})
                # print(res)
                # res = res.json()
                # print(res)
               # print(book[1])


            return render_template("book.html", books=search_result, search=search)
            #return render_template("book.html", books=search, search=search)       
            #else:
            #message =  "Please Enter Search Key."
           # return render_template("index.html", message=message)




    else:
        return redirect("/")


    
if __name__ == '__main__':
    app.run(debug=True)
