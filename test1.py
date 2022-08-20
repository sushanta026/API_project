from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/abc', methods=['GET','POST'])
def test():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify((str(result)))

@app.route('/abc1/multiplication', methods=['GET','POST'])
def multiplication1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify((str(result)))

@app.route('/abc1/division1', methods=['GET','POST'])
def div1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a/b
        return jsonify((str(result)))

@app.route('/abc1/exponent1', methods=['GET','POST'])
def expo1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a%b
        return jsonify((str(result)))

@app.route('/abc1/root12', methods=['GET','POST'])
def root1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a**b
        return jsonify((str(result)))
if __name__ == '__main__':
    app.run()