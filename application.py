#from flask import Flask
from flask import Flask, render_template, json, request, session, redirect
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/main")
def return_main():
    return render_template('index.html')