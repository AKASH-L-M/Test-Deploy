
"""
Created on Thu Dec 14 16:12:43 2017

@author: Arjun
"""

#imports
from flask import Flask, render_template

#initialize the flask and SQL Objects
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
