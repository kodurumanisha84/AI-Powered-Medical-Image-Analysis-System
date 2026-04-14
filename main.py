import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

print("Loading dataset...")

data = []
labels = []

dataset_path = "data"
import os

print("NORMAL:", len(os.listdir("data/NORMAL")))
print("PNEUMONIA:", len(os.listdir("data/PNEUMONIA")))

# Load images
for label in ["NORMAL", "PNEUMONIA"]:
    path = os.path.join(dataset_path, label)
    class_label = 0 if label == "NORMAL" else 1

    for img in os.listdir(path):
        img_path = os.path.join(path, img)

        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # ⚠️ SKIP BROKEN IMAGES
        if image is None:
            print("Skipping corrupted file:", img_path)
            continue

        image = cv2.resize(image, (64, 64))
        data.append(image.flatten())
        labels.append(class_label)

data = np.array(data)
labels = np.array(labels)

print("Dataset loaded!")
print("Total samples:", len(data))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    data, labels, test_size=0.2, random_state=42
)

print("Training model...")

# Train model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

print("Model trained!")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("\nAccuracy:", acc)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

# Show sample prediction
index = 0
sample = X_test[index].reshape(64, 64)

plt.imshow(sample, cmap='gray')
plt.title("Prediction: " + ("PNEUMONIA" if y_pred[index] == 1 else "NORMAL"))
plt.show()