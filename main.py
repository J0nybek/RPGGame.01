import cv2
import numpy as np
from tensorflow.keras.models import load_model

class CarDamageDetector:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def preprocess_image(self, image_path):
        # Implement image preprocessing logic (resize, normalization, etc.)
        # Example: use OpenCV to read and preprocess the image
        image = cv2.imread(image_path)
        image = cv2.resize(image, (224, 224))  # Adjust the size according to your model requirements
        image = image / 255.0  # Normalize pixel values

        return image.reshape(1, 224, 224, 3)

    def predict_damage(self, image_path):
        preprocessed_image = self.preprocess_image(image_path)
        prediction = self.model.predict(preprocessed_image)

        # Interpret the prediction based on your model's output
        # Example: assuming binary classification (damaged or not)
        damage_probability = prediction[0][0]
        is_damaged = damage_probability > 0.5

        return is_damaged, damage_probability

class CarDamageReporter:
    def __init__(self):
        # You can add additional initialization logic here
        pass

    def generate_report(self, is_damaged, damage_probability):
        if is_damaged:
            report = f"The car is damaged with a probability of {damage_probability:.2%}."
        else:
            report = f"The car is not damaged with a probability of {damage_probability:.2%}."

        return report

# Example usage:
model_path = 'path/to/your/model.h5'
image_path = 'path/to/your/car_image.jpg'

damage_detector = CarDamageDetector(model_path)
is_damaged, damage_probability = damage_detector.predict_damage(image_path)

damage_reporter = CarDamageReporter()
report = damage_reporter.generate_report(is_damaged, damage_probability)

print(report)
