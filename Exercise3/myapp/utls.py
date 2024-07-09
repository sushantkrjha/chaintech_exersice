import datetime
import random

def get_current_datetime():
    return datetime.datetime.now()

def get_random_quote():
    quotes = [
        "The best way to predict the future is to invent it.",
        "Life is  what happens to us and  how we react to it.",
        "Your time is limited, so don't waste it living someone else's life.",
        "The only way to do great work is to love what you do.",
    ]
    return random.choice(quotes)
