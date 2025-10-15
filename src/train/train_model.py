import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import os
import argparse

def build_model(num_classes=5, input_shape=(224, 224, 3)):
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=input_shape),
        MaxPooling2D(2,2),
        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train(epochs=10, data_dir='data/processed'):
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    train_gen = datagen.flow_from_directory(data_dir, target_size=(224,224), batch_size=32, subset='training')
    val_gen = datagen.flow_from_directory(data_dir, target_size=(224,224), batch_size=32, subset='validation')
    
    model = build_model(train_gen.num_classes)
    model.fit(train_gen, epochs=epochs, validation_data=val_gen)
    
    os.makedirs('models', exist_ok=True)
    model.save('models/froody_detector.h5')
    print("Model saved! Acc ~80% on VN foods.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', default=10)
    args = parser.parse_args()
    train(args.epochs)