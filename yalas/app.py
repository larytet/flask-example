import flask
import views


app = flask.Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
# see http://flask.pocoo.org/docs/0.12/quickstart/#http-methods
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# https://pythonspot.com/en/flask-web-forms/
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.errorhandler(404)
def not_found(error):
    resp = flask.make_response(flask.render_template('error.html', error_code=404), 404)
    resp.headers['X-Something'] = 'A value'
    return resp


views.add_rules(app)

