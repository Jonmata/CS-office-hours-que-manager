from flask import Flask , render_template
app = Flask(__name__)
app.secret_key="hello"

@app.route("/")
def index():
    name = "Kevin"
    return render_template("index.html",name=name)


if __name__ == "__main__":
    app.run(debug=True)