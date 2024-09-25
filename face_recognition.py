import dlib
import cv2
import numpy as np

# Load Dlib's pre-trained face detector and shape predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_rec_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Function to extract face embeddings
def get_face_embedding(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    embeddings = []

    for face in faces:
        shape = predictor(gray, face)
        face_embedding = face_rec_model.compute_face_descriptor(image, shape)
        embeddings.append(np.array(face_embedding))
    
    return embeddings

# Function to recognize faces in real-time from webcam
def recognize_faces():
    cap = cv2.VideoCapture(0)

    # Known face embeddings and corresponding labels
    known_face_embeddings = []  # List of embeddings
    known_face_labels = []      # List of labels

    # Load known faces (You should have a process to populate these)
    # For example, load images and compute embeddings

    while True:
        ret, frame = cap.read()
        embeddings = get_face_embedding(frame)

        for embedding in embeddings:
            distances = [np.linalg.norm(embedding - known) for known in known_face_embeddings]
            min_distance = min(distances)
            threshold = 0.6  # Adjust based on your needs

            if min_distance < threshold:
                index = distances.index(min_distance)
                person_name = known_face_labels[index]
            else:
                person_name = "Unknown"

            # Draw rectangle and label
            cv2.putText(frame, person_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run face recognition
recognize_faces()

