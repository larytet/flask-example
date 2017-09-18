import flask_wtf
import wtforms

class SearchForm(flask_wtf.Form):
    search_form = wtforms.TextField('Search', validators=[DataRequired()])
    
    
