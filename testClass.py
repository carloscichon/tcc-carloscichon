import cv2
import numpy as np
from keras.models import model_from_json

emotion_dict = {0: "angry", 1: "contempt", 2: "disgust", 3: "fear", 4: "happy", 5: "neutral", 6: "sad", 7: "surprise"}


json_file = open('affect_model_200.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
emotion_model = model_from_json(loaded_model_json)

emotion_model.load_weights("affect_model_200.h5")
print("Loaded model from disk")

img = cv2.imread("/home/carlos/UFPR/tcc/tcc-carloscichon/angry.jpg")
face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces available on camera
num_faces = face_detector.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
for (x, y, w, h) in num_faces:
    cv2.rectangle(img, (x, y-50), (x+w, y+h+10), (0, 255, 0), 4)
    roi_gray_frame = gray_frame[y:y + h, x:x + w]
    cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (224, 224)), -1), 0)
    # predict the emotions
    emotion_prediction = emotion_model.predict(cropped_img)
    maxindex = int(np.argmax(emotion_prediction))
    print("Max :", maxindex)
    print(emotion_prediction)
    cv2.putText(img, emotion_dict[maxindex], (x+5, y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imwrite("example.png", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break