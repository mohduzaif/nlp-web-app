from flask import Flask, render_template, request, redirect, session
from database import Database

import api

app = Flask(__name__)

database_object = Database()

# route is for login page
@app.route('/')
def index():
    return render_template('login.html')

# route for register page
@app.route('/register')
def register():
    return render_template('register.html')

# route for performing registration process
@app.route('/perform_registration', methods = ['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = database_object.insert_data(name, email, password)

    if response:
        return render_template('login.html', message = "Registration Successful, Now proceed to Login")
    else:
        return render_template('register.html', message = "User Already Exist.")
    
# route for performing login process
@app.route('/perform_login', methods = ['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = database_object.search_user(email, password)
    if response:
        return redirect('/home_page')
    else:
        return render_template('login.html', wrong_msg = "Wrong Credentials, Email/Password")

@app.route('/home_page')
def home_page():
    return render_template('home.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')
    

@app.route('/perform_ner', methods = ['post'])
def perform_ner():
    ner_text = request.form.get('ner_text')
    response = api.name_entity_rec_api(ner_text)

    result = []
    for entity in response.entities():
        current_dict = {}
        simple_type = api.get_entity_type(entity.freebase_types)
        current_dict['Entity'] = entity.id
        current_dict['Type'] = simple_type
        current_dict['Confidence Score'] = entity.confidence_score

        result.append(current_dict)
        # print(f"Entity: {entity.id}")
        # print(f"Type: {simple_type}")
        # print(f"Confidence Score: {entity.confidence_score}")
        # print("-" * 40)
    # print(result)
    return render_template('ner.html', result = result)

@app.route('/sentiment_analysis')
def sentiment_analysis():
    return render_template('sentiment_analysis.html')

@app.route('/perform_sentiment_analysis', methods = ['post'])
def perform_sentiment_analysis():
    user_text = request.form.get('user_text')
    response = api.sentiment_analysis_api(user_text)
    if response:
        return render_template('sentiment_analysis.html', response = response)
    else:
        return render_template('sentiment_analysis.html')
    
@app.route('/language_detection')
def language_detection():
    return render_template('language_detection.html')

@app.route('/detect_language', methods = ['post'])
def detect_language():
    user_text = request.form.get('user_text')
    response = api.language_detection_api(user_text)
    
    result_dict = {}
    result_dict['Language'] = response[0]['language']
    result_dict['Confidence'] = response[0]['confidence']

    if response:
        return render_template('language_detection.html', response = result_dict)
    else:
        return render_template('language_detection.html')


app.run(debug=True)