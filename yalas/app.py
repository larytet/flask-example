import flask
import views

import forms

app = flask.Flask(__name__, instance_relative_config=True)

app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    resp = flask.make_response(flask.render_template('error.html', error_code=404), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

views.add_rules(app)
search_form = forms.SearchForm()
