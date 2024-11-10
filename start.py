from flask import Flask , render_template, request
from Backend import Queue 

app = Flask(__name__)
app.secret_key="hello"


admin = {"use": "Jessy", "password": "Poker"}

masterList = Queue.LinkedList()

masterList.enqueue("bob","123","CSE116")
masterList.enqueue("jon","1234","CSE115")
masterList.enqueue("kev","432", "CSE116")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signIn", methods=["POST"])
def signInfun():
    use = request.form.get("UBID")
    password = request.form.get("password")
    if admin["use"]== use and admin["password"] == password:
    # create student and add them to the que;
        items = masterList.get_all()
        cse116_students = [item for item in items if item.course == "CSE116"]
        cse115_students = [item for item in items if item.course == "CSE115"]
        return render_template("TA.html", cse116_students=cse116_students, cse115_students=cse115_students)
    else:
        return render_template("studentSignIn.html")


@app.route("/studentAdd", methods=["POST"])
def addStudentFromStudent():
    name = request.form.get("name")
    ubid = request.form.get("UBID")
    course = request.form.get("option")
    print(name+" "+ubid+" "+course)
    masterList.enqueue(name, ubid,course)
    # create student and add them to the que;
    items = masterList.get_all()

    cse116_students = [item for item in items if item.course == "CSE116"]
    cse115_students = [item for item in items if item.course == "CSE115"]
    return render_template("listDisplay.html", cse116_students=cse116_students, cse115_students=cse115_students)

@app.route("/removeSelf" , methods=["POST"])
def removeStudent():
        ubid = request.form.get("UBID")
   
        masterList.dequeue(ubid)
        # create student and add them to the que;
        items = masterList.get_all()
        cse116_students = [item for item in items if item.course == "CSE116"]
        cse115_students = [item for item in items if item.course == "CSE115"]
        return render_template("listDisplay.html", cse116_students=cse116_students, cse115_students=cse115_students)

@app.route("/submit" , methods=["POST"])
def tARemoveAndAdd():
    name = request.form.get("name")
    ubid = request.form.get("UBID")
    course = request.form.get("option")
    action = request.form.get("action")
    print(action)
    if(action == 'add'):
        masterList.enqueue(name, ubid,course)
        # create student and add them to the que;
        items = masterList.get_all()
        cse116_students = [item for item in items if item.course == "CSE116"]
        cse115_students = [item for item in items if item.course == "CSE115"]
    else:
        masterList.dequeue(ubid)
        # create student and add them to the que;
        items = masterList.get_all()
        cse116_students = [item for item in items if item.course == "CSE116"]
        cse115_students = [item for item in items if item.course == "CSE115"]
    
    return render_template("TA.html", cse116_students=cse116_students, cse115_students=cse115_students)


if __name__ == "__main__":
    app.run(debug=True)