import pandas as pd
import numpy as np
import json
from flask import Flask,request,jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/data_frame",methods=['GET'])
def data_frame():
	df = pd.read_csv("flaskmethod.csv")
	new_dict=df.to_dict("index")
	abc=list(new_dict.values())
	return json.dumps(abc)

@app.route("/add",methods=['POST'])
def add_data():
	data = request.get_json()
	df = pd.read_csv("flaskmethod.csv")
	new_dict=df.to_dict("index")
	list_of_df=list(new_dict.values())
	created_df = {}
	created_df['index'] = (list_of_df[-1]['index']+1)
	combined_data = {**created_df,**data}
	df = df.append(combined_data,ignore_index = True)
	print(df)
	df.to_csv('flaskmethod.csv', index = None, header = True)
	return jsonify({"index ":created_df["index"]})

@app.route("/delete",methods=['DELETE'])
def del_data():
	data = request.get_json()
	df = pd.read_csv(r"flaskmethod.csv")
	# new_dict=df.to_dict("index")
	# list_of_df=list(new_dict.values())
	df = df[df['index'] != data['index']]
	df.to_csv(r'flaskmethod.csv',index = None, header=True)
	return jsonify({"index ":data["index"]})

@app.route("/update", methods=["PUT"])
def update_data():
	data = request.get_json()
	df = pd.read_csv(r"flaskmethod.csv")
	df.loc[df['index'] == data['index'],["Name","Roll_no","class"]] = data["Name"],data["Roll_no"],data["class"]
	df.to_csv(r'flaskmethod.csv',index = None, header=True)
	return jsonify({"index ":data["index"]})

if __name__ == "__main__":
    app.run(debug=True)