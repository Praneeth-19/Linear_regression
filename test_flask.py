from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/addition',methods=["GET"])
def add():
    a=request.args.get('n1')
    b=request.args.get('n2')
    return ([int(a)+int(b)])

if __name__== '__main__':
    app.run(host='0.0.0.0',port=8000)