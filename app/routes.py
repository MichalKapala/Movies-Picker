from app import app
from flask import render_template, request
from app.forms import LoginForm, FindForm
from app.models import Movies_Database



@app.route('/')
@app.route('/index', )
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route('/find', methods=['GET', 'POST'])
def find():
    form = FindForm()
    movies = ''
    if request.method == 'POST':
        phrase = request.form.get('phrase')
        movies = Movies_Database.query.filter(Movies_Database.name.contains(phrase))

    return render_template('find.html', form=form, movies=movies)

if __name__ == "__main__":
    app.run(debug=True)