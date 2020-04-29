# imports
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.optimizers import SGD
import argparse
import imutils
import cv2
import os
from flask import Flask, jsonify
from flask_cors import CORS

# app = Flask(__name__)

# flask
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


# load and compile model
model = load_model('model.h5')
model.compile(loss = "binary_crossentropy", 
              optimizer = SGD(lr=0.001, momentum=0.9), 
              metrics=["accuracy"])



def model_predict(file_path, model):
	# image constraints
	img_width, img_height = 128, 128

	# # load and compile model
	# model = load_model('model.h5')
	# model.compile(loss = "binary_crossentropy", 
	#               optimizer = SGD(lr=0.001, momentum=0.9), 
	#               metrics=["accuracy"])

	image = cv2.imread(file_path)
	image = cv2.resize(image, (img_width, img_height))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis = 0)


	# generate prediction
	result = model.predict(image)
	pred = np.argmax(result, axis=1)
	prediction = "UNRECOGNIZABLE"
	if(pred[0] == 0):
	    prediction = "Pneumonia"
	else:
	    prediction = "Normal"


	# return result
	return prediction





#  /API
@app.route('/', methods = ['POST', 'OPTIONS'])  
def success():  
	if request.method == "OPTIONS":
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response
	else:
		f = request.files['file']  
		# f.save(f.filename)
		basepath = os.path.dirname(__file__)
		file_path = os.path.join(
			basepath, 'uploads', secure_filename(f.filename))
		f.save(file_path)

		preds = model_predict(file_path, model)

		print(preds)
			
		return jsonify(success = True, prediction = preds)



if __name__ == '__main__':
    app.run(debug=False,threaded=False)

