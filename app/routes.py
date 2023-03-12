from app import app
import random
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest, RequestEntityTooLarge

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2 megabytes
app.config['UPLOAD_EXTENSIONS'] = ['.jpg']

@app.errorhandler(RequestEntityTooLarge)
def handle_request_entity_too_large_error(error):
    return jsonify({'error': 'Ukuran file melebihi batas 2MB', 'status': 413}), 413

@app.route('/', methods = ['POST'])

def ReturnJSON():
	if(request.method == 'POST'):
		uploaded_file = request.files['file']
		filename = secure_filename(uploaded_file.filename)
		if filename != '':
			file_ext = os.path.splitext(filename)[1]
			if file_ext not in app.config['UPLOAD_EXTENSIONS']:
				errorHandle = {
					"status" : 400,
					"message" : "File upload wajib dalam bentuk JPG"
                }
				return jsonify(errorHandle),400
			
			# Dummy data
			dummyArea           = [98029,118550,124110,99458,104610]
			dummyPerimeter      = [1261.73,1147.57,1248.9,1205.82,1169.27]
			dummyContrast       = [0.0265524,0.0278111,0.0269613,0.0301564,0.0251643]
			dummyCorrelation    = [0.996075,0.995905,0.996118,0.995719,0.996241]
			dummyUkuran         = ['Besar', 'Kecil']
			dummyKebersihan     = ['Bersih', 'Kotor']
			dummyDistribusi     = ['Mall', 'Supermarket', 'Pasar']
			
            # Random data
			randomIndexArea         = random.randrange(len(dummyArea))
			randomIndexPerimeter    = random.randrange(len(dummyPerimeter))
			randomIndexContrast     = random.randrange(len(dummyContrast))
			randomIndexCorrelation  = random.randrange(len(dummyCorrelation))
			randomIndexUkuran       = random.randrange(len(dummyUkuran))
			randomIndexKebersihan   = random.randrange(len(dummyKebersihan))
			randomIndexDistribusi   = random.randrange(len(dummyDistribusi))
			
			data = {
                "status" : 200,
                "data" : {
                    "fitur_ukuran" : {
                            "area" : dummyArea[randomIndexArea],
                            "perimeter" : dummyPerimeter[randomIndexPerimeter]
                    },
                    "fitur_tekstur" : {
                            "contrast" : dummyContrast[randomIndexContrast],
                            "correlation" : dummyCorrelation[randomIndexCorrelation]
                    },
                    "hasil_identifikasi" : {
                            "ukuran" : dummyUkuran[randomIndexUkuran],
                            "kebersihan" : dummyKebersihan[randomIndexKebersihan],
                            "distribusi" : dummyDistribusi[randomIndexDistribusi]
                    },
                }
            }
			return jsonify(data),200
		else :
			errorHandle = {
					"status" : 400,
					"message" : "File upload tidak ditemukan"
                }
			return jsonify(errorHandle),400
