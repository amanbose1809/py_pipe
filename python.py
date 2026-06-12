from flask import Flask
app=Flask(__name__)

@app.route("/",methods=["GET"])
def root():
    return "flask/python app running on port:5500-> 7700"

app.run(port=5500,host="0.0.0.0")
