from keras.applications.inception_v3 import InceptionV3
from keras.layers import Input, Lambda, Dense, GlobalAveragePooling2D
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import Model
import tensorflow as tf
from keras.backend import tf as ktf
from data import get_data

#getting the data
X_train, y_train = get_data()
# Setting the input size for the model
input_size = 299

# Using Inception with ImageNet pre-trained weights
inception = InceptionV3(weights='imagenet', include_top=False,
                        input_shape=(input_size,input_size,3))
print('Model Initialized')

# Freezing the parameters
## Iterate through the layers of the Inception model loaded above and set all of them to have trainable = False
for layer in inception.layers:
    layer.trainable = False
print('Parameters Frozen')

# Makes the input placeholder layer 32x32x3
sim_input = Input(shape=(160,320,3))

# Re-sizes the input with Kera's Lambda layer & attach to sim_input
resized_input = Lambda(lambda image: ktf.image.resize_images( 
    image, (input_size, input_size)))(sim_input)

# Feeds the re-sized input into Inception model
inp = inception(resized_input)

# Finishing up the model architecture
x = GlobalAveragePooling2D()(inp)
dense = Dense(512, activation='relu')(x)
predictions = Dense(1, activation='softmax')(dense)

# Creates the model
model = Model(inputs=sim_input, outputs=predictions)
# Compile the model
model.compile(optimizer='Adam', loss='mse', metrics=['accuracy'])
# Check the summary of this new model to confirm the architecture
model.summary()
# Init Callbacks
checkpoint = ModelCheckpoint(filepath='model.h5', monitor='val_loss', save_best_only=True)
stopper = EarlyStopping(monitor='val_acc', min_delta=0.0003, patience=5)
# Train the model
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, callbacks=[stopper], epochs=1)
model.save('model.h5')