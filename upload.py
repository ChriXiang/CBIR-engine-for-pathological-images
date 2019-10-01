# coding:utf-8

from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
from werkzeug.utils import secure_filename
import os
import cv2

from query_api import execution

from datetime import timedelta
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 
app = Flask(__name__)

app.send_file_max_age_default = timedelta(seconds=1)
 
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        if not (f and allowed_file(f.filename)):
            return jsonify({"error": 1001, "msg": "Invalid image format, only png、PNG、jpg、JPG、bmp acceptable."})
 
        user_input = request.form.get("name")
 
        basepath = os.path.dirname(__file__)
 
        upload_path = os.path.join(basepath, 'static/images', secure_filename(f.filename))

        f.save(upload_path)

        ans_list = execution(query_path = upload_path)

        prefix = './database/'
        return render_template('upload_ok.html',qname=f.filename, qpath='./images/'+f.filename ,ans0= prefix + ans_list[0],name0=ans_list[0],ans1= prefix + ans_list[1],name1=ans_list[1],ans2= prefix + ans_list[2],name2=ans_list[2],ans3= prefix + ans_list[3],name3=ans_list[3])
 
    return render_template('upload.html')


 
@app.route('/db', methods=['POST', 'GET'])
def database():
    prefix = './database/'
    cur = 0
    rev_size = 8
    img_list = ['End of database'] * 8
    data = []
    for x in os.listdir('./static/database'):
        if x.endswith('.jpg'):
            data.append(x)

    if request.method == 'POST':
        cur = int(request.form['cur'])
        la = None
        ne = None
        try:
            la = request.form['last']
        except:
            pass
        try:
            ne = request.form['next']
        except:
            pass
        if la is not None:
            cur = cur - 8 if cur - 8 >= 0 else 0
        if ne is not None:
            cur = cur + 8 if cur + 8 <= len(data) - 1 else cur

        for index, each in enumerate(sorted(data)):
            if index >= cur and cur+ 8 > index:
                img_list[index - cur] = each
                #img_list.append(each)

        return render_template('db.html', INDEX = str(cur//8 + 1), CUR = str(cur), 
            ALL = len(data)//8 + 1, img1 = img_list[0], ip1 = prefix + img_list[0], 
            img2 = img_list[1], ip2 = prefix + img_list[1], img3 = img_list[2], ip3 = prefix + img_list[2], 
            img4 = img_list[3], ip4 = prefix + img_list[3], img5 = img_list[4], ip5 = prefix + img_list[4], 
            img6 = img_list[5], ip6 = prefix + img_list[5], img7 = img_list[6], ip7 = prefix + img_list[6], 
            img8 = img_list[7], ip8 = prefix + img_list[7])
    else:
        cur = 0
        for index, each in enumerate(sorted(data)):
            if index >= cur and cur + 8 > index:
                img_list[index - cur] = each
                #img_list.append(each)
        return render_template('db.html', INDEX = str(cur//8 + 1), CUR = str(cur), 
            ALL = len(data)//8 + 1, img1 = img_list[0], ip1 = prefix + img_list[0], 
            img2 = img_list[1], ip2 = prefix + img_list[1], img3 = img_list[2], ip3 = prefix + img_list[2], 
            img4 = img_list[3], ip4 = prefix + img_list[3], img5 = img_list[4], ip5 = prefix + img_list[4], 
            img6 = img_list[5], ip6 = prefix + img_list[5], img7 = img_list[6], ip7 = prefix + img_list[6], 
            img8 = img_list[7], ip8 = prefix + img_list[7])
if __name__ == '__main__':
    # app.debug = True
    app.run()