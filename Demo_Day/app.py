from flask import Flask, render_template, redirect, jsonify


app = Flask(__name__)



@app.route("/")
def home():

    # Find one record of data from the mongo database

    # Return template and data
    return render_template("dashboard.html")





if __name__ == '__main__':
    app.run(debug=True)