from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

def evaluate(model, test_data):
    y_true = test_data.classes
    y_pred = model.predict(test_data)
    y_pred = np.round(y_pred)

    print("Accuracy:", accuracy_score(y_true, y_pred))
    print("Confusion Matrix:", confusion_matrix(y_true, y_pred))