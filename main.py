
'''
## Sources

1. [Flask-Ask](https://flask-ask.readthedocs.io/en/latest/getting_started.html)
2. [Instructables](https://www.instructables.com/Control-Raspberry-Pi-GPIO-With-Amazon-Echo-and-Pyt/)

'''

from flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('HelloIntent')
def hello(firstname):
    text = render_template('hello', firstname=firstname)
    return statement(text).simple_card('Hello', text)

if __name__ == '__main__':
    app.run(debug=True)