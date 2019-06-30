# **Behavioral Cloning** 
<<<<<<< HEAD
=======

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file, but feel free to use some other method and submit a pdf if you prefer.
>>>>>>> 2d6e97945840d706b2a99cd2a003f8b66f72e9e5

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* data.py containing the script to load, generate and augment the data
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup_report.md or writeup_report.pdf summarizing the results

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

The architecture starts with a lambda layer for normalization.
Then a `Cropping2D` layer to crop the unneeded areas of the input images.
Next we have a `Conv2D` with 32 filters and 3x3 kernel size.
Moving into a `MaxPooling2D` with a pool size of 2x2.
To improve generalisation we have a `Dropout` layer with a drop rate of 0.5.
Then a `RELU` layer to introduce nonlinearity.
Afterwards we flatten and introduce a `dense` layer that has an output of 128.
Another `RELU` layer is used here before moving to the final `Dense` layer that has an output of 1 which is our steering angle.

#### 2. Attempts to reduce overfitting in the model

<<<<<<< HEAD
The model contains a dropout layer in order to reduce overfitting.
The model was trained and validated on 20% of the data which was made into a validation set to ensure that the model was not overfitting. The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.
=======
#### 2. Attempts to reduce overfitting in the model
>>>>>>> 2d6e97945840d706b2a99cd2a003f8b66f72e9e5

#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually.

<<<<<<< HEAD
#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center, right and left cameras images with adjusted steering angle for both left and right cameras to help the model recover from right and left to center. Plus to double the amount of training data, the pictures have been augmented by being flipped which helps the model generlise even more.
=======
#### 3. Model parameter tuning

The model used an adam optimizer, so the learning rate was not tuned manually (model.py line 25).

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road ... 
>>>>>>> 2d6e97945840d706b2a99cd2a003f8b66f72e9e5

For details about how I created the training data, see the next section. 

### Model Architecture and Training Strategy
<<<<<<< HEAD
=======

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was to ...

My first step was to use a convolution neural network model similar to the ... I thought this model might be appropriate because ...

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. This implied that the model was overfitting. 

To combat the overfitting, I modified the model so that ...

Then I ... 

The final step was to run the simulator to see how well the car was driving around track one. There were a few spots where the vehicle fell off the track... to improve the driving behavior in these cases, I ....

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 18-24) consisted of a convolution neural network with the following layers and layer sizes ...

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![alt text][image1]

#### 3. Creation of the Training Set & Training Process
>>>>>>> 2d6e97945840d706b2a99cd2a003f8b66f72e9e5

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was understanding that the best thing to have is a vast amount of training data that generalise and teach the model what it needs to learn. After acgieving that all that's needed was a simple CNN that trains efficiently on the data.

My first model architecture did the trick all thanks to the sufficient data that was used.

The final step was to run the simulator to see how well the car was driving around track one. And the car drove perfectly throughout the track.

#### 2. Final Model Architecture

The final model architecture consisted of:

| Layer         		|
|:---------------------:|
| Input         		|
| Lambda        	    |   
| Cropping2D		    |
| Conv2D	      	    |   
| Max pooling	      	|
| Dropout	      	    |
| RELU		            |
| Flatten		        |
| Dense		            |
| RELU		            |
| Dense		            |

#### 3. Creation of the Training Set & Training Process

I used the simulation data provided by Udacity which is recorded on track 1 in the simulator.

To augment the data set, I flipped images and angles thinking that this would help generalising by tricking the model into thinking i drove the car the other direction in the simulator.

I finally randomly shuffled the data set and put 20% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or under fitting. One epoch was sufficient as evidenced by running the simulator on the trained model. I used an adam optimizer so that manually training the learning rate wasn't necessary.