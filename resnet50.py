from keras.applications.resnet50 import ResNet50
from keras.models import Model
from keras.layers import Flatten, Dense, Activation


def get_resnet50():

    base_model = ResNet50(include_top=False, weights='imagenet')
    x = base_model.output
    x = Flatten()(x)
    logits = Dense(256)(x)
    probabilities = Activation('softmax')(logits)

    return Model(base_model.input, probabilities)