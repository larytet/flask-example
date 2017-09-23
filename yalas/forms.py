import flask_wtf
import wtforms

class SearchForm(wtforms.Form):
    search = wtforms.TextField('Search:', validators=[wtforms.validators.required()])

class LoginForm(wtforms.Form):
    username = wtforms.TextField('Username:', validators=[wtforms.validators.required()])
