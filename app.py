from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Bilal Uddin khan</h1>"

app.run(debug= True)

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Hello World!</h1>"

# app.run(debug=True)
# Footer