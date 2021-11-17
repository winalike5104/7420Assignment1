from flask import Flask,jsonify,request,session
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app, resources=r'/*')


@app.route('/registered',methods=['POST','GET'])
def hello_world():
   return jsonify(resultMessage='someone already registered',resultType='warning')

if __name__ == '__main__':
   app.run()

