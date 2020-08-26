from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/services")
def service():
    return render_template('services.html')


@app.route("/FAQ")
def faq():
    return render_template('faq.html')


@app.route("/pricing")
def price():
    return render_template('pricing.html')


@app.route("/404")
def error():
    return render_template('404.html')


app.run(debug=True)
