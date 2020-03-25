from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars


app = Flask(__name__)


mongo = PyMongo(app, uri="mongodb://localhost:27017/nasa_app")



@app.route("/")
def home():

    # Find one record of data from the mongo database
    nasa_news = mongo.db.collection.find_all()

    # Return template and data
    return render_template("index.html", nasa_news=nasa_news)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    nasa_news = mongo.db.nasa_news
    nasa_news_data = mission_to_mars.scrape()
    nasa_news.update({}, nasa_news_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
