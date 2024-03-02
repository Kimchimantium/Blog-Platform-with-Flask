import smtplib
from send_email import Smtp
from flask import Flask, render_template, url_for, request
import requests, json, os
from random import choice



result = requests.get(url='https://api.npoint.io/c73f6bdc0b52d620d550').json()
if not os.path.isfile("articles.json"):
    with open("articles.json", "w") as file:
        json.dump(result, file, indent=4)

app = Flask(__name__)

def jinja_attributes():
    articles = result['articles']
    rand_post = choice(articles)
    img_path = url_for('static', filename='/assets/img/contact-bg.jpg')
    css_url = url_for('static', filename="css/styles.css")
    js_url = url_for('static', filename="js/scripts.js")
    return articles, rand_post, img_path, css_url, js_url

@app.route("/")
def home():
    articles, rand_post, img_path, css_url, js_url = jinja_attributes()
    return render_template('index.html',
                           css_url=css_url,
                           js_url=js_url,
                           img_path=img_path,
                           articles=articles,
                           rand_post=rand_post)


@app.route("/about")
def about():
    articles, rand_post, img_path, css_url, js_url = jinja_attributes()
    return render_template("about.html",
                           css_url=css_url,
                           js_url=js_url,
                           img_path=img_path,
                           rand_post=rand_post)

@app.route("/contact")
def contact():
    articles, rand_post, img_path, css_url, js_url = jinja_attributes()
    return render_template("contact.html",
                           img_path=img_path,
                           css_url=css_url,
                           js_url=js_url,
                           articles=articles,
                           rand_post=rand_post)


@app.route('/credits', methods=["GET", "POST"])
def receive_data():
    user_credentials = []
    if request.method == "POST":
        name_credits = request.form.get("name")
        password_credits = request.form.get("password")
        email_credits = request.form.get("email")
        ph_credits = request.form.get("phone")
        message_credits = request.form.get("message")
    user_credentials.append({
        "Names": name_credits,
        "Passwords": password_credits,
        "Emails": email_credits,
        "Phone Numbers": ph_credits,
        "Messages": message_credits
    })
    se = Smtp(user_credentials)
    se.send_email()
    articles, rand_post, img_path, css_url, js_url = jinja_attributes()
    return render_template("user-credentials.html",
                           img_path=img_path,
                           css_url=css_url,
                           js_url=js_url,
                           articles=articles,
                           rand_post=rand_post,
                           user_credentials=user_credentials)

@app.route("/post/<string:title>")
def post(title):
    articles, rand_post, img_path, css_url, js_url = jinja_attributes()
    for index, article in enumerate(articles):
        if title == article['title']:
            article_for_page = article
            current_index = index
    article_num = len(articles)
    return render_template("post.html",
                           css_url=css_url,
                           js_url=js_url,
                           articles=articles,
                           article_num=article_num,
                           article_for_page=article_for_page,
                           current_index=current_index,
                           rand_post=rand_post)


if __name__ == '__main__':
    app.run(debug=True, port=6060)

