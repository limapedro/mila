import yaml
import os
import json
import numpy as np

data = yaml.safe_load(open('nlu\\train.yml').read())

# Reading the data

inputs, outputs = [], []

for command in data['commands']:
    inputs.append(command['input'])
    outputs.append('{}\{}'.format(command['entity'], command['action']))

# Create a dataset
# Choose a level of tokenization: words, chars, BPEs

chars = set()

# Read all chars in the dataset

for i in inputs + outputs:
    for ch in i:
        if ch not in chars:
            chars.add(ch)

# Create input data


#print(len(chars))