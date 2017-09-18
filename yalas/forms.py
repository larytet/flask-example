import flask_wtf
import wtforms

class SearchForm(flask_wtf.Form):
    search_form = wtforms.StringField('Search', validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
