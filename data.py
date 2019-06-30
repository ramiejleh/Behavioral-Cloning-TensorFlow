import csv
import cv2
import numpy as np
from PIL import Image

def get_data():
    car_images = []
    steering_angles = []
    with open('data/driving_log.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            steering_center = float(row[3])

            # create adjusted steering measurements for the side camera images
            correction = 0.2 # this is a parameter to tune
            steering_left = steering_center + correction
            steering_right = steering_center - correction

            # read in images from center, left and right cameras
            path = 'data/'
            img_center = np.asarray(Image.open(path + row[0].strip()))
            img_left = np.asarray(Image.open(path + row[1].strip()))
            img_right = np.asarray(Image.open(path + row[2].strip()))

            # add images and angles to data set
            car_images.extend([img_center, img_left, img_right])
            steering_angles.extend([steering_center, steering_left, steering_right])

    augmented_car_images, augmented_steering_angles = [], []
    
    for car_image, steering_angle in zip(car_images, steering_angles):
        augmented_car_images.append(car_image)
        augmented_steering_angles.append(steering_angle)
        augmented_car_images.append(np.fliplr(car_image))
        augmented_steering_angles.append(-steering_angle)
        
    X_train = np.array(augmented_car_images)
    y_train = np.array(augmented_steering_angles)
    print('Data fetched')
    return X_train, y_train