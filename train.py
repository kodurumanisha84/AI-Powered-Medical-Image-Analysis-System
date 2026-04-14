from preprocessing import load_data
from model import build_model

train_data, test_data = load_data("data/train", "data/test")

model = build_model()

history = model.fit(train_data, epochs=5, validation_data=test_data)

model.save("models/model.h5")