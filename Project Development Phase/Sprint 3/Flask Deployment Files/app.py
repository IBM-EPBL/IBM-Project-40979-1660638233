# -*- coding: utf-8 -*-
"""app
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/17Yx8hioHPopCN4EFPvJYw6TuixjXcrwY
Data Collection & Image Processing
Collecting images of different food items organized into subdirectories based on their respective names
"""

ls

cd /content/drive/MyDrive/dataset

pwd

!unzip TRAIN_SET.zip

!unzip TEST_SET-20221103T125409Z-001.zip

"""Importing and configuring the Image data generator library from Keras"""

from tensorflow.keras.preprocessing.image import ImageDataGenerator#scaling,zooming

train_datagen=ImageDataGenerator(rescale=1./255,zoom_range=0.2,shear_range=0.2,horizontal_flip=True,vertical_flip=True)

test_datagen=ImageDataGenerator(rescale=1./255)

"""Applying Image data generator functionality to training set and testing set"""

x_train=train_datagen.flow_from_directory(r"/content/drive/MyDrive/dataset/TRAIN_SET",target_size=(64,64),color_mode='rgb',class_mode="categorical",batch_size=24)

x_test=test_datagen.flow_from_directory(r"/content/drive/MyDrive/dataset/TEST_SET",target_size=(64,64),color_mode='rgb',class_mode="categorical",batch_size=24)

x_train.class_indices

""" Model Building & Testing
"""

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dropout

"""Initializing the model"""

model=Sequential()

"""Creating the model"""

model.add(Conv2D(32,(3,3),activation="relu",strides=(1,1),input_shape=(64,64,3)))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(300,activation="relu"))
model.add(Dense(300,activation="relu"))

model.add(Dense(5,activation="softmax"))

model.summary()

model.add(Dense(300,activation='relu'))
model.add(Dense(300,activation='relu'))

model.add(Dense(4,activation='softmax'))

model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=['accuracy'])

len(x_train)

model.fit(x_train,epochs=10,validation_data=x_test,steps_per_epoch=len(x_train),validation_steps=len(x_test))

"""Saving the Model"""

model.save('train.h5')

model.save('dataset.h5')

model.save('fruits.h5')

model.save('nutrition.h5')

"""Testing the Model"""

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model=load_model('train.h5')

model=load_model('dataset.h5')

model=load_model('fruits.h5')

model=load_model('nutrition.h5')

img=image.load_img(r"/content/drive/MyDrive/dataset/TEST_SET/APPLES/32_100.jpg")

img

img=image.load_img(r"/content/drive/MyDrive/dataset/TEST_SET/APPLES/32_100.jpg",target_size=(64,64))

img

x=image.img_to_array(img)

x

x=np.expand_dims(x,axis=0)

x

pred = model.predict
pred

predict_x=model.predict(x_test) 
classes_x=np.argmax(predict_x,axis=0)

predict_x

classes_x

x_test.class_indices

index=['APPLES','BANANA','ORANGE','PINEAPPLE','WATERMELON']

index[np.argmax(pred)]

"""Build Python Code"""

from flask import Flask,render_template,request
# Flask-It is our framework which we are going to use to run/serve our application.
#request-for accessing file which was uploaded by the user on our application.
import os
import numpy as np #used for numerical analysis
from tensorflow.keras.models import load_model#to load our trained model
from tensorflow.keras.preprocessing import image
import requests

"""Creating our flask application and loading our model by using the load_model method"""

app = Flask(__name__,template_folder="templates") # initializing a flask app
# Loading the model
model=load_model('nutrition.h5')
print("Loaded model from disk")

"""Routing to *Html* page"""

@app.route('/')# route to display the home page
def home():
    return render_template('home.html')

@app.route('/image1',methods=['GET','POST'])# routes to the index html
def image1():
    return render_template("image.html")

@app.route('/predict',methods=['GET', 'POST'])# route to show the predictions in a web UI
def launch():
    if request.method=='POST':
        f=request.files['file'] #requesting the file
        basepath=os.path.dirname('__file__')#storing the file directory
        filepath=os.path.join(basepath,"uploads",f.filename)#storing the file in uploads folder
        f.save(filepath)#saving the file
        img=image.load_img(filepath,target_size=(64,64)) #load and reshaping the image
        x=image.img_to_array(img)#converting image to an array
        x=np.expand_dims(x,axis=0)#changing the dimensions of the image
        pred=np.argmax(model.predict(x), axis=1)
        print("prediction",pred)#printing the prediction
        index=['APPLES','BANANA','ORANGE','PINEAPPLE','WATERMELON']
        result=str(index[pred[0]])
        x=result
        print(x)
        result=nutrition(result)
        print(result)
        return render_template("0.html",showcase=(result))

x=result
print(x)
result=nutrition(result)
print(result)

def nutrition(index):


    url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
    
    querystring = {"query":index}
    
    headers = {
        'x-rapidapi-key': "5d797ab107mshe668f26bd044e64p1ffd34jsnf47bfa9a8ee4",
        'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
        }
    response = requests.request("GET", url="https://calorieninjas.p.rapidapi.com/v1/nutrition", headers =
                                {
        'x-rapidapi-key': "5d797ab107mshe668f26bd044e64p1ffd34jsnf47bfa9a8ee4",
        'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
        }, params= {"query":index} )
    print(response.text)     
    return response.json()['items']

if __name__ == "__file__":
   # running the app
    app.run(debug=False)
