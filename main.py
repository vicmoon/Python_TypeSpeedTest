from flask import Flask, render_template, url_for, request, session
from words import words
import time
import os

#create the app 
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")



def get_words():
    return words[:50]


@app.route("/", methods=["GET", "POST"])
def home():
    # Ensure session contains start_time
    if "start_time" not in session:
        session["start_time"] = time.time()  # Store start time in session
        session["word_count"] = 0  # Initialize word count

    feedback = "Start typing! DO NOT add a comma between the words."

    if request.method == "POST":
        elapsed_time = time.time() - session["start_time"]  # Now session["start_time"] exists

        # Only process input if time is up (1 minute)
        if elapsed_time >= 60:
            user_input = request.form["user_text"].strip()
            typed_words = user_input.split()
            correct_words = [word for word in typed_words if word in words]

            session["word_count"] += len(correct_words)  # Update word count
            feedback = f"You typed {session['word_count']} correct words in 1 minute!"

            session.clear()  # Clear session after submission

    return render_template("home.html", words=get_words(), feedback=feedback)



if __name__ == "__main__":
    app.run(debug=True)