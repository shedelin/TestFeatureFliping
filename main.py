from flask import Flask, flash, redirect, render_template, request, session, abort, make_response, url_for
import json

from document import Database
from document.Feature import Feature
from forms import FeatureForm

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "super secret key"

Md = Database.MongoDatabase()
db = Md.db

@app.route('/')
def home():
	return  render_template('home.html')

@app.route('/managefeature')
def manageFeature():
	features  = db.Features.find()

	return  render_template('manageFeature.html', datas=features)

@app.route('/examplesolo')
def exampleSolo():
	return  render_template('exampleSolo.html')

@app.route('/examplemulti')
def exampleMulti():
	return  render_template('exampleMulti.html')

@app.route('/featureIsOk', methods=['POST'])
def featureIsOk():
	feature_id = request.form['featureId']
	country    = request.form['country']
	
	feature = Feature(feature_id)
	states  = feature.getStates()
	data = ("0", "1")['Activate' == states[country]]
	
	resp = make_response(json.dumps(data))
	resp.status_code = 200
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

@app.route('/featuresAreOk', methods=['POST'])
def featuresAreOk():
	features = request.get_json()['listFeature']
	datas = {}
	for feature in features:
		obj = features[feature]
		featureId = obj['id']
		feature = Feature(featureId)
		states  = feature.getStates()
		country = obj['country']
		state = ("0", "1")['Activate' == states[country]]
		datas[obj['pubId']] = state
	
	resp = make_response(json.dumps(datas))
	resp.status_code = 200
	resp.headers['Access-Control-Allow-Origin'] = '*'
	return resp

@app.route('/addfeature', methods=['GET', 'POST'])
def addfeature():
	form = FeatureForm()
	if form.validate_on_submit():
		feature        = Feature()
		feature._name  = form.name.data
		feature._state_us = form.stateUs.data
		feature._state_en = form.stateEn.data
		feature._state_de = form.stateDe.data
		feature._state_cl = form.stateCl.data
		feature._state_fi = form.stateFi.data
		feature._state_it = form.stateIt.data
		feature._state_jp = form.stateJp.data
		feature._state_es = form.stateEs.data
		feature._state_ru = form.stateRu.data
		feature._state_fr = form.stateFr.data

		#insert val in new feature
		feature.commit()

		flash('New feature successfuly created added.')

		return redirect(url_for('managefeature'))

	return render_template('addEditFeature.html', form=form, type="create")


@app.route('/editfeature/<feature_id>', methods=['GET', 'POST'])
def editfeature(feature_id):
	dbFeature = db.features
	feature   = Feature(feature_id)
	if feature is None:
		flash('feature doesnt exist.')

		return redirect(url_for('home'))

	form = FeatureForm()

	if form.validate_on_submit():
		feature._name  = form.name.data
		feature._state_us = form.stateUs.data
		feature._state_en = form.stateEn.data
		feature._state_de = form.stateDe.data
		feature._state_cl = form.stateCl.data
		feature._state_fi = form.stateFi.data
		feature._state_it = form.stateIt.data
		feature._state_jp = form.stateJp.data
		feature._state_es = form.stateEs.data
		feature._state_ru = form.stateRu.data
		feature._state_fr = form.stateFr.data

		feature.commit()

		flash('feature successfuly edited.')

		return redirect(url_for('managefeature'))

	# pas reussis a faire marcher
	#form.populate_obj(feature)
	if request.method == 'GET':
		form.name.data = feature._name
		form.stateUs.data = feature._state_us
		form.stateEn.data = feature._state_en
		form.stateDe.data = feature._state_de
		form.stateCl.data = feature._state_cl
		form.stateFi.data = feature._state_fi
		form.stateIt.data = feature._state_it
		form.stateJp.data = feature._state_jp
		form.stateEs.data = feature._state_es
		form.stateRu.data = feature._state_ru
		form.stateFr.data = feature._state_fr

	return render_template('addEditFeature.html', form=form, type="edit", id=feature._id)

if __name__ == "__main__":
	app.run()