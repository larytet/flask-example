import flask_wtf
import wtforms

class SearchForm(flask_wtf.Form):
    # validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()]
    search_form = wtforms.TextField('Search')
    
    
