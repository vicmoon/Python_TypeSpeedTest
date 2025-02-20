from flask import Flask, render_template, url_for
from words import words
import random 

#create the app 
app = Flask(__name__)
# app.config("SECRET_KEY") = "BIgSecret550600"

def random_words():
    return words[:50]

    

#routes 
@app.route("/", methods=["GET", "POST"])
def home():
   return render_template("home.html", words=random_words())
    

#display the text to enter

#check if the user input matches the displayed text 

#measure the time and how many correct words were entered 7



if __name__ == "__main__":
    app.run(debug=True)