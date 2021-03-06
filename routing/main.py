from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the homepage'

@app.route('/tuna')
def tuna():
    return '<h2>Tuna is good</h2>'

@app.route('/profile/<username>')
def profile(username):
    return "<h2>Hey there %s</h2>"% username

@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h2>Postal Id is: %d</h2>"% post_id

if __name__ == "__main__":
    app.run(debug=True)