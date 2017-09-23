import flask
import wtforms
import werkzeug
import os
import collections

FlaskRoute = collections.namedtuple('FlaskRoute', ['route', 'name', 'cb', 'methods'], verbose=False)

class Views:
    
    def __init__(self, app):
        self.app = app
        self.add_routes(app)

    
    def add_routes(self, app):

        ROUTES = [
            FlaskRoute('/',                     'index',    self.index,         None),
            FlaskRoute('/link',                 'link',     self.link,          None),
            FlaskRoute('/search',               'search',   self.search,        methods=['GET', 'POST']),
            FlaskRoute('/hello/',               'hello',    self.hello,         None),
            FlaskRoute('/hello/<string:name>',  'hello',    self.hello,         None),
            FlaskRoute('/upload',               'upload',   self.upload_file,   methods=['GET', 'POST']),
        ]

        for flask_route in ROUTES:
            methods = flask_route.methods 
            if methods is None:
                methods = ['GET']
            app.add_url_rule(flask_route.route, flask_route.name, flask_route.cb, methods=methods)
    
    def link(self):
        url = flask.url_for('static', filename='style.css')
        return flask.render_template('url.html', name="style.css", url=url)
    
    def index(self):
        return 'Index Page'
    
    def hello(self, name=None):
        return flask.render_template('hello.html', name=name)
    
    class ReusableForm(wtforms.Form):
        search = wtforms.TextField('Search:', validators=[wtforms.validators.required()])
     
    
    def search(self):
        request = flask.request
        search_form = self.ReusableForm(request.form)
    
        flask.flash("Form errors: {0}".format(search_form.errors))
        if request.method == 'POST':
            print request
            search_query = request.form['search']
            flask.flash("Search query: {0}".format(search_query))
            if search_form.validate():
                # Save the comment here.
                flask.flash('Search ' + search_query)
            else:
                flask.flash('All the form fields are required. ')
     
        return flask.render_template('search.html', form=search_form)
    
    # Security related feature- make sure that html, php&friends are not here
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
    def allowed_file(self, filename):
        result = '.' in filename
        extension = None
        if result:
            extension = filename.rsplit('.', 1)[1].lower()
            result = extension in self.ALLOWED_EXTENSIONS
        return result, extension  
    
    def upload_file(self):
        request = flask.request
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flask.flash('No file part in the request')
                return flask.redirect(request.url)
            attr_file = request.files.get('file', None)
            
            if attr_file is None:
                flask.flash('No file attribute in the POST')
                return flask.redirect(request.url)
            
            # if user does not select file, browser also
            # submit a empty part without filename
            if attr_file.filename == '':
                flask.flash('No selected file')
                return flask.redirect(request.url)

            is_allowed, file_extension = self.allowed_file(attr_file.filename)
            if is_allowed:
                filename = werkzeug.utils.secure_filename(attr_file.filename)
                flask.flash('Uploaded {0} to {1}'.format(filename, self.app.config.upload_folder))
                attr_file.save(os.path.join(self.app.config.upload_folder, filename))
                return flask.redirect(flask.url_for('upload', filename=filename))
            else:
                flask.flash('File type {0} is not supported'.format(file_extension))
                return flask.redirect(request.url)

        return flask.render_template('upload.html') 
         
    
    