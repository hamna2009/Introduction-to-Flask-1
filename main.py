import flask 

app = flask.Flask(__name__)

@app.route("/")
def index(): #index or home
    return flask.render_template('activity.html')

@app.route("/calculate", methods=['POST'])
def calculate():
    units = int(flask.request.form['units'])
    # Add your calculation logic here
    bill = units * 5

    if units <=100:
        message= "You are a energy saver"
    elif units <= 200:
        message= "You are a moderate energy user"
    else:
        message= "You are a high energy user"

    return flask.render_template("activity.html", bill=bill, message=message, units=units)

if __name__ == '__main__':
    app.run(debug=True)