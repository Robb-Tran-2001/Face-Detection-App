# Face-Detection-App
Real-time face detection app.

The Haar Cascade Algorithm: 

Haar Features:
- Rudimentary building blocks (5 in total)
    - Edge features
    - Line features
    - Four-rectangle features
- Each of the haar features are placed over an image, determining
the relationship between the pixels using the blocks.
- Chaining them and overlaying them over and over again gives a template
for a face. Hence, the cascade.
- Grayscale is used because we want brightness. Color is relevant
only if we want race, facial features, etc.

How it is trained:
- Positive images: face
- Negative images: non-face
- This is an example of supervised machine learning
- We want to find the "Winning" Haar features for recognizing a face
- Test EVERY Haar feature (every TYPE, SIZE, LOCATION). Each feature
gives a number, right or wrong by adding up the white/black into
2 different numbers. The difference between the 2 gives the relationship.
If it passes our provided threshold, then it passes for a face. Whichever 
matches the images the closest is the First Winner. The first X winner
features chained together is the face template.

OpenCV has the pretrained classifier, so it is easier to use.
- Create classifier from trained data
- Pass in a picture
- Grayscale it
- Pass it into classifier to get coords of faces
- Draw rectangles over faces
- Render