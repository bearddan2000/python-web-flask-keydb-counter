from flask import Flask, render_template
from keydb import KeyDB
from keydb import ConnectionPool

app = Flask(__name__)

pool = ConnectionPool(host='keydb')
db = KeyDB(connection_pool=pool)

@app.route("/")
def hello():
    title = 'Python Flask KeyDb MVC Example'
    visits = db.incr('counter')
    return render_template("index.html", title=title, visits=visits)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
