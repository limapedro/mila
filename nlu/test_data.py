import yaml
import os
import json


data = yaml.safe_load(open('nlu\\train.yml').read())

for command in data['commands']:
    print(command)