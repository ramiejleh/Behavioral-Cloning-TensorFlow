from keras.layers import Lambda, Cropping2D
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Flatten, Dropout
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
import tensorflow as tf
from data import get_data

#getting the data
X_train, y_train = get_data()

model = Sequential()
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160, 320, 3)))
model.add(Cropping2D(cropping=((70,25), (0,0))))
model.add(Conv2D(32, (3, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Dropout(0.5))
model.add(Activation('relu'))
model.add(Flatten())
model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dense(1))
# Compile the model
model.compile(optimizer='Adam', loss='mse', metrics=['accuracy'])
# Check the summary of this new model to confirm the architecture
model.summary()
# Init Callbacks
checkpoint = ModelCheckpoint(filepath='model.h5', monitor='val_loss', save_best_only=True)
stopper = EarlyStopping(monitor='val_acc', min_delta=0.0003, patience=5)
# Train the model
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, callbacks=[checkpoint, stopper], epochs=1)
model.save('model.h5')