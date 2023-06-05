import cv2
import numpy as np
import mediapipe as mp
import math

#얼굴 이미지를 수평으로 반환하는 함수
def conversion(image):
    '''이미지가 너무 크면 오류남'''
    if image.shape[0] > 1500 or image.shape[1] > 1500: # 너비 높이 1500 이상이면 보간법으로 이미지 축소 
        image = cv2.resize(image, (0, 0), fx=0.4, fy=0.4, interpolation=cv2.INTER_LINEAR)
    
    original_image = image.copy()
    
    # rotate
    rotate_image = rotate_img(original_image)

    return rotate_image



mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
                                static_image_mode=True,
                                max_num_faces=1,
                                refine_landmarks=True,
                                min_detection_confidence=0.5)

'''얼굴 이미지의 수평을 맞춘다.'''
def rotate_img(image):
    result = face_mesh.process(image) #얼굴을 탐지한다.
    height, width = image.shape[:2]
    
    try : #얼굴 탐지가 잘 됐을 경우
        for facial_landmarks in result.multi_face_landmarks:
            x_min = width
            x_max = 0
            y_min = height
            y_max = 0

            for i in range(0, 468): # 랜드마크 (x, y) 0부터 468      
                pt = facial_landmarks.landmark[i]
                x = int(pt.x * width)
                y = int(pt.y * height)
                
                if x < x_min:
                    x_min = x
                if x > x_max:
                    x_max = x
                if y < y_min:
                    y_min = y
                if y > y_max:
                    y_max = y  
                    
            mid_forehead_X = facial_landmarks.landmark[9].x # 중앙 미간 x
            mid_forehead_Y = facial_landmarks.landmark[9].y # 중앙 미간 y
            mid_chin_X = facial_landmarks.landmark[152].x # 중앙 턱 x
            mid_chin_Y = facial_landmarks.landmark[152].y # 중앙 턱 y
            
            '''얼굴 수평 이동'''
            tan_theta = (mid_chin_X - mid_forehead_X)/(mid_chin_Y - mid_forehead_Y)
            theta = np.arctan(tan_theta)
            rotate_angle = theta *180/math.pi
            rot_mat = cv2.getRotationMatrix2D((height//2, width//2), -rotate_angle, 1.0)
            image  = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR, borderValue=(255,255,255))
        
            rotate_image = image.copy()            
        
        return rotate_image #수평을 맞춘 이미지 반환

    #얼굴 탐지를 못하면 기존의 이미지를 반환한다.    
    except: return image