from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
     return "Hello World!"
if __name__== "__main__":
     app.run()

app = Flask(__name__)

@app.route("/")
def hello():
     return "Hello World !"
if __name__ == "__name__":
    app.run

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World !"

empDB=[
    {
'id':'102',
'name':'Dorry Britz',
'title':'Technical Leader'
        },
{
'id':'102',
'name':'Barbie Gurl',
'title':'Software Engineer'
    }
    ]

@app.route('/emdb/employee/<empId>', methods=['GET'])
def getEmp(empId):
    usr = [ emp for emp in empDB if (emp['id'] == empId)]
    return jsonify({'emp':usr})
