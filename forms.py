from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class FeatureForm(FlaskForm):
	"""feature form."""
	name = StringField('Name', [
		DataRequired()])
	stateUs = SelectField('State_us', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	stateEn = SelectField('State_en', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	stateDe = SelectField('State_de', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	stateCl = SelectField('State_cl', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	stateFi = SelectField('State_fi', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	stateIt = SelectField('State_it', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	stateJp = SelectField('State_jp', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	stateEs = SelectField('State_es', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	stateRu = SelectField('State_ru', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	stateFr = SelectField('State_fr', [
		DataRequired()],
		choices=[('Activate', 'activate'), ('Deactivate', 'deactivate')])
	submit = SubmitField('Submit')