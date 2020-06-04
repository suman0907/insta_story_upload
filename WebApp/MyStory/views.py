from . import test
from flask import jsonify, request, render_template, redirect
from WebApp import *
import requests
import json
from .models import *
from werkzeug.utils import secure_filename
import os
from WebApp.Files import *
from PIL import Image



@test.route('/tes', methods=['GET'])
def tes():
    return jsonify({"msg":"Welcome to your story"})



@test.route('/upload_file', methods=['GET'])
def upload_file():
   return render_template("upload_image.html")




ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF","MP4"]
MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024 * 1024
IMAGE_UPLOADS= "WebApp/Files/saved_images"



def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.split(".")[-1]


    if ext.upper() not in ALLOWED_IMAGE_EXTENSIONS:
        return True
    else:
        return False




def allowed_image_filesize(filesize):

    if int(filesize) <= MAX_IMAGE_FILESIZE:
        return True
    else:
        return False




@test.route('/upload_image',methods=['GET','POST'])
def upload_image():

    requestObject = request.form
    f = request.files['file']
    try:

        story_info = Story_Info()
        res = {}

        res['grapher_name'] = requestObject.get("grapher_name")
        res['description'] = requestObject.get("description")
        res['type'] = requestObject.get("type")
        res['longitude'] = requestObject.get("longitude")
        res['lattitude'] = requestObject.get("lattitude")
        res['duration'] = requestObject.get("duration")
        res['name'] = f.filename

        #res['file']=f
        #filesize= request.headers.get('content-length')

        if f.filename == "":
            print("No filename")
            return jsonify({"message": " Empty upload not allowed"})

        if allowed_image(f.filename):
            filename = secure_filename(f.filename)
            print("Image saved")
            return jsonify({"message": " File extension not supported "})


        if res['type']=='image':
            img = Image.open(f)
            image_height = img.height
            image_width = img.width
            if image_height != 1200 or image_width != 600:
                newsize = (1200, 600)
                im1 = img.resize(newsize)




        #f.save(os.path.join(IMAGE_UPLOADS, f.filename))


        story_info.import_data(res)
        db.session.add(story_info)
        db.session.commit()



        return jsonify({"message": " Your Story is Successfully Added "})
    except Exception as e:
        print (str(e))
        db.session.rollback()
        return jsonify({"message": "error", "error_info": str(e)})




@test.route('/get_recent_stories',methods=['GET'])
def get_recent_stories():
    try:

        stories=Story_Info.query.order_by(Story_Info.timestamp.desc())



        req= {
            "grapher_name": "",
            "lattitude": "",
            "longitude":"",
            "timestamp":"",
            "duration":""
        }
        result = []

        for prods in stories:

            if prods is None:
                return jsonify({"message": "Not found"})

            prod_details = {}
            for key in req:
                prod_details[key] = getattr(prods, key)

            result.append(prod_details)


        return jsonify({"message": "success","reponse": result})



    except Exception as e:
        print(str(e))
        db.session.rollback()
        return jsonify({"message": "error", "error_info": str(e)})
