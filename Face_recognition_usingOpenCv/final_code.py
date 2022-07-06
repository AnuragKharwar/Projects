import cv2
import numpy as np
import cv2 as cv

from os import listdir
from os.path import isfile, join

data_path = 'C:/Users/Anura/PycharmProjects/pythonProject5/faces/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

Training_data, Labels = [], []

for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    Training_data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels, dtype=np.int32)

model = cv.face.LBPHFaceRecognizer_create()


model.train(np.asarray(Training_data), np.asarray(Labels))

print("Model Training complete!!! ")

face_classifier = cv.CascadeClassifier(
    'C:/Users/Anura/PycharmProjects/pythonProject5/FaceDetection-HaarCascade-master/FaceDetection-HaarCascade-master/haarcascade_frontalface_default.xml')


def face_detector(img, size=0.5):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return img, []

    for(x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
        roi = img[y:y+h, x:x+w]
        roi = cv.resize(roi, (200, 200))

    return img, roi


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/400))
          #  display_string = str(confidence)+'% confidence it is user'
        # cv.putText(image, display_string, (100, 120), cv.FONT_HERSHEY_SIMPLEX, 1, (250, 120, 240), 2)

        if confidence > 85:
            cv.putText(image, "unlocked", (250, 450),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 225, 0), 2)
            display_string = str(confidence) + '% confidence it is user'
            cv.putText(image, display_string, (100, 120),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (250, 120, 240), 2)
            cv.imshow('face_cropper', image)
            print("USER Face detected....")
        else:
            cv.putText(image, "locked ", (250, 450),
                       cv.FONT_ITALIC, 1, (0, 0, 255))
            display_string = str(confidence) + '% confidence it is NOT user'
            cv.putText(image, display_string, (100, 120),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (250, 120, 240), 2)
            cv.imshow('face_cropper', image)

    except:
        cv.putText(image, "No face found", (250, 450),
                   cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
        cv.imshow('face_cropper', image)
        print("No face found!!!!!!!")
        pass

    if cv.waitKey(1) == 13:
        break
      cap.release()
cv.destroyAllWindows()

