from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    print(request.method)
    print(request.form)
    with open("response.txt", "w") as file:
        file.write(f"Name: {request.form["name"]} and Email: {request.form["email"]}")
    return render_template("contact.html")

app.run(debug=True)