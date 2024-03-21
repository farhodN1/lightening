from flask import Flask
from flask_cors import CORS
import firebase_admin
from firebase_admin  import credentials, db



app = Flask(__name__)
CORS(app)
cred = credentials.Certificate('python.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pythonbacknd-default-rtdb.firebaseio.com/users'
})

ref = db.reference('users')

print(ref.get())
@app.route('/')
def index():
    return 'Web App with Python Flask!'

@app.route('/community')    
def community():
    return ref.get()


app.run(host='0.0.0.0', port=81)