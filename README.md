## 서버 로직
- 스프링 서버에서 넘어온 사진을 리스트로 받는다.
 <img src = "https://github.com/FaceRecognition0/Flask-server/assets/95980876/71512ca8-250e-44f7-8219-c99a770e45e1.jpg" width="55%" height="55%">

<br><br>
- 받은 사진을 폴더에 저장하고 이미지를 다시 byte형식으로 리스트에 담는다.
<img src = "https://github.com/FaceRecognition0/Flask-server/assets/95980876/a6c897a8-79e6-430a-a327-cac8bb60996b.jpg" width="40%" height="40%"><br>

<br>

- 얼굴 인식 메서드에 이미지를 전달하고 받은 결과값을 클라이언트에 반환한다.
<img src = "https://github.com/FaceRecognition0/Flask-server/assets/95980876/9a9a27db-d03a-49c3-8bcb-e4fa0d9d0898.jpg" width="40%" height="40%"><br>

## 메서드 소개
- **detectAndDisplay()** : resnet_10 모델을 사용하여 사진의 얼굴 영역만 탐지해 자른다.
- **conversion()** : openCV를 활용해 얼굴의 수평을 맞춘다.
- **get_face_embedding_dict()** : face_recognition을 사용해 얼굴의 임베딩 값을 구한다.
