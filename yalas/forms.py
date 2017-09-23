import flask_wtf
import wtforms

class SearchForm(flask_wtf.Form):
    search_form = wtforms.TextField('Search', validators=[wtforms.validators.DataRequired()])
    

class LoginForm(flask_wtf.Form):
    login_form = wtforms.TextField('Login', validators=[wtforms.validators.DataRequired()])
    
