from flask import Flask, render_template, request
import random

app = Flask(__name__)

intro_message = "Welcome to the 'We're Not Really Strangers' game! This game is designed to help you get"

@app.route("/")
def home():
    return render_template("home.html", intro_message=intro_message)

@app.route("/start_game")
def start_game():
    questions = [
    "What is something you're passionate about?",
    "If you could have any superpower, what would it be?",
    "What was your favorite subject in school and why?",
    "What is something that you're afraid of?",
    "What is your love language?",
    "If you could live in any time period, when would it be?",
    "What is the most important lesson you've learned in life?",
    "What are your favorite qualities in a friend?",
    "What is your favorite way to spend a lazy day?",
    "What is something you wish people knew about you?",
    "What is the best gift you've ever received and why?",
    "What is your biggest accomplishment?",
    "What is something that you're working to improve in yourself?",
    "What is your happiest memory?",
    "What is the biggest risk you've taken in your life?",
    "What is your definition of success?",
    "What is something you're currently struggling with?",
    "What is your proudest moment?",
    "What is something you're currently excited about?",
    "What is something you've always wanted to do but haven't had the chance?",
    "What did you learn about yourself from our date tonight?",
    "What is something you appreciated about our conversation?",
    "What is something you wish we had talked about more?",
    "What did you enjoy most about our time together?",
    "What is something you learned from me that you didn't know before?",
    "What is something you feel like you want to know more about me?",
    "What is something you would like to do together in the future?",
    "What did you learn from our differences?",
    "What is something you took away from our conversation?",
    "What is something you feel grateful for about our date?",
    "What was your first impression of me?",
    "What is something you're curious about me?",
    "What is something you find attractive in a person?",
    "What is something you find unattractive in a person?",
    "What is something you're looking for in a relationship?",
    "What is something you're not looking for in a relationship?",
    "What is your idea of the perfect date?",
    "What is your idea of a perfect partner?",
    "What is your biggest turn on?",
    "What is your biggest turn off?",
    "What is something that you stand for?",
    "What is something that you would never compromise on?",
    "What is something that you value the most in life?",
    "What is something you believe in that not everyone agrees with?",
    "What is your favorite quote?",
    "What is your favorite book?",
    "What is your favorite movie?",
    "What is your favorite song?",
    "What is your favorite TV show?",
    "What is your favorite food?",
    "What is your dream job?",
    "What is your dream vacation?",
    "What is something you've always wanted to learn?",
    "What is something you've always wanted to try?",
    "What is something you've always wanted to visit?",
    "What is something you've always wanted to do?",
    "What is something you've always wanted to achieve?",
    "What is your ultimate goal in life?",
    "What is something you want to accomplish in the next year?",
    "What is your vision of your future self?",
    "What is your fondest childhood memory?"
]
    random.shuffle(questions)
    current_question = 0
    return render_template('game.html', questions=questions, current_question=current_question)

if __name__ == "__main__":
    app.run(debug=True)
