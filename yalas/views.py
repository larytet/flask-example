import flask


def link():
    url = flask.url_for('static', filename='style.css')
    return flask.render_template('url.html', name="style.css", url=url)

#@app.route('/')
def index():
    return 'Index Page'

def hello(name=None):
    return flask.render_template('hello.html', name=name)


def add_rules(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/link', 'link', link)
    app.add_url_rule('/hello/', 'hello', hello)
    app.add_url_rule('/hello/<string:name>', 'hello', hello)
    
    