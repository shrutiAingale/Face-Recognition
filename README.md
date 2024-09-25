# Face-Recognition

Face Recognition Using OpenCV and Webcam

Overview
This project demonstrates a face recognition system using OpenCV and Python. The system captures video input from a webcam and detects faces in real-time using OpenCV's pre-trained face detection models. It also supports building a database by storing images of recognized individuals in organized folders.

Features
Real-time face detection using webcam.
Recognition of multiple faces in a video feed.
Database creation with individual folders for each person.
Each person's folder contains multiple images used for training face recognition.
Easy setup and usage.
Database Creation and Folder Structure
In this project, a simple image-based database is created where:

A main folder named face_database is used to store subfolders.
Each subfolder represents an individual and contains images of that person.
Steps to Create the Database:
Folder Creation:

When a new person is detected or added, a folder is created inside the face_database directory with that person's name.
Collecting Images:

For each person, multiple images are captured from the webcam.
These images are saved in the respective person's folder inside face_database.
The images are later used for training the face recognition model.
Folder Structure Example:
bash
Copy code
face_database/
│
├── person_1/                  # Folder for the first individual
│   ├── image1.jpg             # Images for this individual
│   ├── image2.jpg
│   └── ...
│
├── person_2/                  # Folder for the second individual
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
│
└── person_N/                  # Folder for the N-th individual
    ├── image1.jpg
    ├── image2.jpg
    └── ...
Adding a New Person to the Database
Running the Script:

The user can specify that they want to add a new person by entering a name (either via command line or in the UI).
A folder with that name will be created under face_database, and images will be captured and stored in that folder.
Capturing Images:

Once the webcam is active, the system will automatically capture a certain number of images of the person and save them in their folder.
These images are used to train the face recognition algorithm so that the person can be recognized in future webcam feeds.
Training the Face Recognition Model
After adding several individuals and their images to the database, you can proceed with training the face recognition model by running a training script. This script processes the images in the face_database and updates the model with the new faces.
