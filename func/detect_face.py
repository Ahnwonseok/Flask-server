import cv2
import numpy as np

model_name='resnet_10/res10_300x300_ssd_iter_140000.caffemodel'
prototxt_name='resnet_10/deploy.prototxt.txt'

def detectAndDisplay(img):
    # 원본 사진을 face_recognition.face_encodings 를 활용해
    # crop과 encoding을 할 수 있지만 시간이 오래걸리기 때문에
    # 크롭하고 인코딩값을 구한다.
    
    (height, width) = img.shape[:2]
    model=cv2.dnn.readNetFromCaffe(prototxt_name,model_name)
    blob=cv2.dnn.blobFromImage(cv2.resize(img,(300,300)),1.0, (300,300),(104.0,177.0,123.0))
    
    model.setInput(blob)
    
    detections=model.forward()

    '''crop 과정'''
    min_confidence=0.9
    result_img = None

    for i in range(0, detections.shape[2]):
        
        confidence = detections[0, 0, i, 2]
        
        if confidence > min_confidence:
              
            box = detections[0, 0, i, 3:7] * np.array([width, height, width, height])
            (startX, startY, endX, endY) = box.astype("int")
            
            if height > endY and width > endX and startX > 0 and startY > 0: #얼굴탐지를 이미지 내에서 해야함
                result_img = img[startY:endY,startX:endX]  
                min_confidence = confidence  #얼굴인식 최소 확률을 현재 확률로 정함            

    '''crop을 했을 경우''' 
    if result_img is not None:
        return result_img
    
    else:    
        '''crop 하지 못하는경우'''
        return []