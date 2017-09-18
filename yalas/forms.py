import FlaskForm
import wtforms

class SearchForm(FlaskForm.Form):
    search_form = wtforms.StringField('Search', validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
