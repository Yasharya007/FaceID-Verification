from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.logger import Logger

import cv2 
import tensorflow as tf
from layers import L1Dist
import os
import numpy as np

 # Build app and layout
class CamApp(App):
    def build(self):
        self.web_cam=Image(size_hint=(1,.8))
        self.button=Button(text="Verify",on_press=self.verify,size_hint=(1,.1))
        self.verification_label=Label(text="Verification Unintiated",size_hint=(1,.1))  

        layout=BoxLayout(orientation='vertical')
        layout.add_widget(self.web_cam)
        layout.add_widget(self.button)
        layout.add_widget(self.verification_label)

        self.model=tf.keras.models.load_model('siamesemodel1.h5',custom_objects={'L1Dist':L1Dist})
        self.capture=cv2.VideoCapture(0)
        Clock.schedule_interval(self.update,1.0/33.0)
        return layout
    
    def update(self,*args):
        ret,frame=self.capture.read()
        frame=frame[50:50+250,250:250+250,:]

        buf=cv2.flip(frame,0).tostring()
        img_texture=Texture.create(size=(frame.shape[1],frame.shape[0]),colorfmt='bgr')
        img_texture.blit_buffer(buf,colorfmt='bgr',bufferfmt='ubyte')
        self.web_cam.texture=img_texture
    
    def preprocess(self,file_path):
        byte_img=tf.io.read_file(file_path)
        img=tf.io.decode_jpeg(byte_img)
        img=tf.image.resize(img,(100,100))
        img=img/255.0
        return img
    
    def verify(self,*args):
        detection_threshold=0.7
        verification_threshold=0.5

        SAVE_PATH=os.path.join('Application_Data','Input_image','input_image.jpg')
        ret,frame=self.capture.read()
        frame=frame[50:50+250,250:250+250,:]
        cv2.imwrite(SAVE_PATH,frame)
        results=[]
        for image in os.listdir(os.path.join('Application_Data','Verification__Images')):
            input_img=self.preprocess(os.path.join('Application_Data','Input_image','input_image.jpg'))
            validation_img=self.preprocess(os.path.join('Applciation_Data','Verification__Images',image))
            result=self.model.predict(list(np.expand_dims([input_img,validation_img],axis=1)))
            results.append(result)
        detection=np.sum(np.array(results)>detection_threshold)
        print(detection)
        verification=detection/len(os.listdir(os.path.join('Application_Data','Verification__Images')))
        verified=verification>verification_threshold
        self.verification_label.text='verified' if verified==True else 'Unverified'
        return results,verified


if __name__  == '__main__':
    CamApp().run()