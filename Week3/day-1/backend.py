from flask import Flask

app = Flask(__name__)

@app.route("/",  methods=['GET', 'POST'])
def hello_world():
    return "Forget The syntax"



# @app.route("/delete",methods=['GET','DELETE'])
# def hello_world():
#     return "delete route"



if app.name == 'backend':
    app.run()