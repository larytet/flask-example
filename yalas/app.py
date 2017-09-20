import flask
import views
import os, errno

def create_folder(name):
    try:
        os.makedirs(name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

app = flask.Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
# https://pythonspot.com/en/flask-web-forms/
# http://flask.pocoo.org/docs/0.12/quickstart/#http-methods
# The secret key shall move out of here to a file which is not in the GIT repository
# and be generated by the setup code
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'  # app.config['SECRET_KEY'] shall work as well 
UPLOAD_FOLDER = './uploads'
app.upload_folder = UPLOAD_FOLDER
create_folder(UPLOAD_FOLDER)


@app.errorhandler(404)
def not_found(error):
    resp = flask.make_response(flask.render_template('error.html', error_code=404), 404)
    resp.headers['X-Something'] = 'A value' # TODO What is it
    return resp


views_object = views.Views(app)

