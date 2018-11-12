#import the Flask class from the flask module
from flask import Flask, render_template, redirect
from flask_pymongo import flask_pymongo
import scrape_nyt

#create the application object
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/yemen_app"
mongo = PyMongo(app)

# use decoratoes to link the function to a url
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/articles')
def articles():
    return render_template('articles.html') #render a template

@app.route('/about')
def about():
    return render_template('about.html')

# start the server with "run()" method
if __name__ == '__main__':
    app.run(debug=True)