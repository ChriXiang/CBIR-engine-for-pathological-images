# CBIR-engine-for-pathological-images*

* Project due date: 2019 January.
* Database has been cleaned.
* Feature extraction model: VGG16.
* The engine is web based interactable.

## A. update database
	1. put new images into the folder 'static/database', images should be 
		* 512 x 512 x 3 and 
		* end with '.jpg'
	2. execute 'feature_extract.py': 
		- ` python3 feature_extract.py -database database -index feature.h5 `

## B. run the web server
	1. execute the server script: 
		- ` python3 upload.py `
	2. navigate to '127.0.0.1:5000/upload'

## C. folder description
	1. static: web upload buffer
	2. template: rendering html scripts
 
*The project was done during an internship in ICT,CAS.
