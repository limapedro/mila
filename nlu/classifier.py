from tensorflow.keras.models import load_model
import numpy as np

labels = open('nlu\entities.txt', 'r', encoding='utf-8').read().split('\n')
model = load_model('nlu\model.h5')

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label


# Classify any given text into a category of our NLU framework
def classify(text):
    # Create an input array
    x = np.zeros((1, 48, 256), dtype='float32')

    # Fill the x array with data from input text
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    out = model.predict(x)
    idx = out.argmax()

    #print('Text: "{}" is classified as "{}"'.format(text, idx2label[idx]))
    return idx2label[idx]

'''
if __name__=='__main__':
    while True:
        text = input('Enter some text:')
        print(classify(text))
'''