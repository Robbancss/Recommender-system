import json
import io
import websocket
import codecs
import numpy as np

# userfile = open('relation_type.json', mode='r')
# a = {"type": "Gender", "externalId": "M", "recommendable": "false", "title": "Male", "id": 1}
# for line in itemsfile:
#     b = json.loads(itemsfile.readline())
#     counter+= 1
#     if b['recommendable'] == True:
#         maxid = max(a,b['id'])
# 

itemLen = 0
userLen = 0
a = 0
with open('node_type.json', mode='r') as itemsfile:
    for line in itemsfile:
        nodeLine = json.loads(itemsfile.readline())
        lineID = nodeLine['id']
        if nodeLine['type'] == 'Item':
            itemLen = max(itemLen,lineID)
        if nodeLine['type'] == 'Person':
            userLen = max(userLen,lineID)
print(itemLen)
print(userLen)

y = np.ndarray(shape=(6000, 4000))
print(y)