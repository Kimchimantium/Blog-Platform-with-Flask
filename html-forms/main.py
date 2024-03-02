from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
user_credentials = []
@app.route("/login", methods=["GET", "POST"])
def receive_data(user_credentials=user_credentials):
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user_credentials.append({"username": username})
        user_credentials.append({"password": password})

        print(user_credentials)
    return render_template("login.html",
                           user_credentials=user_credentials)



if __name__ == "__main__":
    app.run(debug=True, port=7000)
