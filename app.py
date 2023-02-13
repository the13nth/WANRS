from flask import Flask, render_template, request
import random

app = Flask(__name__)

intro_message = "Y'all have dates? Wow, look at you! Well, before you fall head over heels, let me introduce you to a little game called We're Not Really Strangers. Now, I can't take credit for this brilliant idea, but if you enjoy it, I highly recommend you head over to werenotreallystrangers.com and purchase the official game. But for now, let's get ready to strip down our emotional walls and get to know each other on a whole new level."

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
    "What is your fondest childhood memory?",
    "Do you believe in any sort of higher power or divine being? Why or why not?",
    "Have you ever had a spiritual experience or felt a connection to something greater than yourself? Can you describe it?",
    "How has your spirituality, or lack thereof, influenced your life and decision-making?",
    "Are there any spiritual practices or rituals that you engage in regularly? Why do you find them meaningful?",
    "How do you find purpose and meaning in life?",
    "Do you believe that there is a purpose or plan for your life, or do you think that everything is random chance? Why?",
    "Have you ever had a crisis of faith or a moment where you doubted your spiritual beliefs? How did you navigate that experience?",
    "Do you believe that there is life after death? Why or why not?",
    "Have you ever explored spirituality or religious beliefs that are different from your own? What did you learn from that experience?",
    "Are there any spiritual or philosophical texts or teachings that have had a significant impact on your life? What did you learn from them?",
    "Do you believe that there is such a thing as destiny or fate? Why or why not?",
    "How do you reconcile difficult or painful experiences with your spiritual beliefs, or lack thereof?",
    "Are there any moral or ethical values that you hold as a result of your spiritual beliefs or lack thereof? What are they?",
    "Have you ever had an encounter with death that made you question your spiritual beliefs, or lack thereof?",
    "Do you believe that spirituality can exist outside of organized religion? Why or why not?",
]
    random.shuffle(questions)
    current_question = 0
    return render_template('game.html', questions=questions, current_question=current_question)

if __name__ == "__main__":
    app.run(debug=True)
