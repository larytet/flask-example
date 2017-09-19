import flask
import forms


def link():
    url = flask.url_for('static', filename='style.css')
    return flask.render_template('url.html', name="style.css", url=url)

#@app.route('/')
def index():
    return 'Index Page'

def hello(name=None):
    return flask.render_template('hello.html', name=name)

class BaseForm(wtforms.ext.csrf.session.SessionSecureForm):
    SECRET_KEY = 'EPj00jpfj8Gx1SjnyLxwB12qQnQ9DJYe0Ym'
    TIME_LIMIT = timedelta(minutes=20)


def search():
    search_form = forms.SearchForm(flask.request.form)
    request.form()
    return flask.render_template('search.html')

def add_rules(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/link', 'link', link)
    app.add_url_rule('/search', 'search', search, methods=['GET', 'POST'])
    app.add_url_rule('/hello/', 'hello', hello)
    app.add_url_rule('/hello/<string:name>', 'hello', hello)
    
    