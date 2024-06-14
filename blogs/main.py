from flask import Flask, render_template
import requests
app = Flask(__name__)

@app.route('/')
def home_page():
    response = requests.get("https://api.npoint.io/948a893b298bc81eedf9")
    data = response.json()
    return render_template("index.html", data=data)


@app.route('/blogs/<id>')
def get_post(id):
    response = requests.get("https://api.npoint.io/948a893b298bc81eedf9")
    data = response.json()
    return render_template("blog.html", data=data, id=int(id))


if __name__ == "__main__":
    app.run(debug=True)