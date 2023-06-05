'''
find face and crop and embedding

실행 시간 : 0.5425937175750732
''' 
import cv2
import numpy as np
import sys 
from func.detect_face import detectAndDisplay
from func.make_horizon import conversion
from func.embedded import get_face_embedding_dict

def img_embedding(images):        
                      
    img_dict = {} # {0:[array], 1:[array], 2:[array], 3:[array], 4:[array]} value = 임베딩값
    '''위 img_dict 딕셔너리를 위해 주소가 아닌 "0", "1", "2"... numbering 으로 바꿈'''
    for numbering, image in enumerate(images):
                    
            image_nparray = np.fromstring(image, dtype=np.uint8)
            image = cv2.imdecode(image_nparray, cv2.IMREAD_COLOR)

            #사진의 얼굴 영역만 crop한다.
            crop_img = detectAndDisplay(image)    

            '''crop을 실패했을 때 원본 이미지로 임베딩 값 구하기'''
            if len(crop_img) == 0: # crop_img = 위 리턴값을 []로 했기 때문에 리스트 내용은 0
                image = conversion(image) # image 얼굴의 수평을 맞춘다.
                original_embedded = get_face_embedding_dict(image) # 숫자이름, 이미지 주소, 원본 이미지
            
                if original_embedded is not None : # 임베딩 값을 구했으면 딕셔너리에 삽입                         
                    img_dict[numbering] = original_embedded # key = 숫자이름, value = 임베딩값          
            
            else : 
                '''#crop이 성공했을 때 임베딩 값 구하기'''    
                crop_img = conversion(crop_img) # crop_img 얼굴의 수평을 맞춘다.                          
                crop_embedded = get_face_embedding_dict(crop_img) # 숫자이름, 이미지 주소, 원본 이미지
             
                if crop_embedded is not None: # 임베딩 값이 구했으면 딕셔너리에 삽입                   
                    img_dict[numbering] = crop_embedded # key = 숫자이름, value = 임베딩값 


    '''만약 프로필 사진을 한 장 이하로 인식을 했다면'''    
    if len(img_dict) <= 1:
        sys.exit('인식할 수 있는 프로필 사진이 없습니다')

    return img_dict # 딕셔너리 리턴 / key: 숫자이름, value: 임베딩값