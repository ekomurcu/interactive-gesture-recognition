## Apply Face Detection to remove face
### Analyzing which one has faces
face_cascade = cv2.CascadeClassifier('closed_frontal_palm.xml')
face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(face_gray)
detection = face_img.copy()
for (x, y, w, h) in faces:
    cv2.rectangle(detection, (x, y), (x+w, y+h), (255, 0, 0), 2)
for (x, y, w, h) in faces:
    print(x, y, w, h)
display_image(detection)

img_face_removed=face_img.copy()
for (x, y, w, h) in faces:
    for i in range(x, w+x):
        for j in range(y, h+y):
            img_face_removed[j][i]=255

display_image(img_face_removed)