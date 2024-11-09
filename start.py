from flask import Flask , render_template, request

app = Flask(__name__)
app.secret_key="hello"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signIn", methods=["POST"])
def signInfun():
    use = request.form.get("UBID")
    password = request.form.get("password")

    
    return render_template("TA.html")


@app.route("/studentAdd", methods=["POST"])
def addStudentFromStudent():
    # create student and add them to the que;
    return render_template("listDisplay.html")

@app.route("/removeSelf" , methods=["POST"])
def removeStudent():
    return render_template("listDisplay.html")

@app.route("/submit" , methods=["POST"])
def tARemoveAndAdd():
    action = request.form.get("action")
    print(action)
    if(action == 'add'):
        print('add')
    else:
        print('removed')
    
    return render_template("TA.html")


if __name__ == "__main__":
    app.run(debug=True)