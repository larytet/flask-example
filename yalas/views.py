import flask
import wtforms
import werkzeug
import os



class Views:
    
    def __init__(self, app):
        self.app = app

        app.add_url_rule('/', 'index', self.index)
        app.add_url_rule('/link', 'link', self.link)
        app.add_url_rule('/search', 'search', self.search, methods=['GET', 'POST'])
        app.add_url_rule('/hello/', 'hello', self.hello)
        app.add_url_rule('/hello/<string:name>', 'hello', self.hello)
        app.add_url_rule('/upload', 'upload_file', self.upload_file)
    
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
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS
    
    def upload_file(self):
        request = flask.request
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flask.flash('No file part in the request')
                return flask.redirect(request.url)
            attr_file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if attr_file.filename == '':
                flask.flash('No selected file')
                return flask.redirect(request.url)
            if attr_file and self.allowed_file(attr_file.filename):
                filename = werkzeug.utils.secure_filename(attr_file.filename)
                flask.flash('Uploaded {0} to {1}'.format(filename, self.app.config.upload_folder))
                attr_file.save(os.path.join(self.app.config.upload_folder, filename))
                return flask.redirect(flask.url_for('uploaded_file', filename=filename))

        return flask.render_template('upload.html') 
         
    
    