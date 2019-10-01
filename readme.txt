A. update database
	1. put new images into the folder 'database' AND 'static/database', images should be 512x512x3 and end with '.jpg'
	2. execute 'feature_extract.py': python3 feature_extract.py -database database -index feature.h5

B. run the web server
	1. execute the server script: python3 upload.py
	2. navigate to '127.0.0.1:5000/upload'

C. folder description
	1. static: web upload buffer
	2. template: rendering html scripts
	3. old: trivial useless scripts (may be refered as references when dubugging)