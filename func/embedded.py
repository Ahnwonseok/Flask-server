import face_recognition
import sys 

'''얼굴 이미지를 임베딩값으로 변환'''
def get_face_embedding_dict(img): # numbering = img번호, url = 사진주소, img = 이미지 자체

    embedding = face_recognition.face_encodings(img)   # 얼굴 영역에서 얼굴 임베딩 벡터를 추출
    
    if len(embedding) > 0:   # crop한 이미지에서 얼굴 영역이 제대로 detect되지 않았을 경우를 대비
        '''crop한 사진에서 임베딩값을 구한경우 통과'''
        return embedding[0] # 임베딩 값 리턴
    else:
        sys.exit('crop 실패')