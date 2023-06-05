from flask import Flask, render_template, request
from func.get_result import get_result

import pandas as pd
from sqlalchemy import create_engine
import base64
from io import BytesIO
import glob
import os

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():    
    if request.method == 'GET':
        return render_template('blog.html')
  

@app.route('/multiFileUploads', methods = ['POST'])
def multi_upload_file():
    
    #이미지 받기
    upload = request.files.getlist("file")

    #사진이 저장되는 디렉토리                           
    image_path= glob.glob('C:/Users/dkswn/OneDrive/문서/코드스테이츠/CP2/face_rec(v2)2/uploads/*.jpg')
    
    #기존의 사진 삭제 
    for f in image_path:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
            
    # 받은 사진 저장       
    for f in upload:
        f.save('./uploads/' + f.filename)
        
    #저장 이미지 리스트에 담기    
    images = []    
    for path in image_path:
        with open(path, 'rb') as f:
            images.append(f.read())
    
    
    #리스트 이미지를 전달하고 결과값 받음
    result = get_result(images)   
     
    return result

   
if __name__ == "__main__":
    app.run(debug=True)