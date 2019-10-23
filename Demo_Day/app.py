from flask import Flask, render_template, redirect, jsonify


app = Flask(__name__)



@app.route("/")
def home():

    # Find one record of data from the mongo database

    # Return template and data
    return render_template("dashboard.html")


@app.route("/Dashboard2")
def user():

    # Return template and data
    return render_template("dashboard2.html")


@app.route("/Table")
def table():

    # Return template and data
    return render_template("table.html")

@app.route("/Maps")
def maps():

    # Return template and data
    return render_template("maps.html")





if __name__ == '__main__':
    app.run(debug=True)