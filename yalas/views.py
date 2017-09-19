import flask
import wtforms


def link():
    url = flask.url_for('static', filename='style.css')
    return flask.render_template('url.html', name="style.css", url=url)

#@app.route('/')
def index():
    return 'Index Page'

def hello(name=None):
    return flask.render_template('hello.html', name=name)

class ReusableForm(wtforms.Form):
    search = wtforms.TextField('Search:', validators=[wtforms.validators.required()])
 

def search():
    '''
    search_form = ReusableForm(flask.request.form)

    print "Form errors:", search_form.errors
    if flask.request.method == 'POST':
        search_query = flask.request.form['search']
        print "Search query:", search_query
        if search_form.validate():
            # Save the comment here.
            flask.flash('Search ' + search_query)
        else:
            flask.flash('All the form fields are required. ')
    '''
    return flask.render_template('search.html') #, form=search_form)
 
def add_rules(app):
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/link', 'link', link)
    app.add_url_rule('/search', 'search', search, methods=['GET', 'POST'])
    app.add_url_rule('/hello/', 'hello', hello)
    app.add_url_rule('/hello/<string:name>', 'hello', hello)
    
    