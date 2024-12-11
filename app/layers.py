import tensorflow as tf
# from tensorflow import keras
from tensorflow.keras.layers import Layer

class L1Dist(Layer):
    def __init__(self,**kwargs):
        super().__init__()
        
    def call(self,input_embedding,validation_embedding):
        # print(input_embedding);
        # print(type(input_embedding))
        # a=tf.convert_to_tensor(input_embedding);
        # # a=tf.reshape(a,[-1]);
        # print(a)
        # b=tf.convert_to_tensor(validation_embedding);
        # b=tf.reshape(b,[-1]);
        result= tf.math.abs(input_embedding-validation_embedding)
        print(result)
        return result
