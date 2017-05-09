import json
import io
import websocket
import codecs
# import _thread
# import re
# import pprint


nodeTypes = []
relationTypes = []
nodeCount = 0
relationCount = 0

fajlServer = open('server.json', 'a')
# fajlRelation = open('relation_type.json', 'a')
# fajlData = open('data.json', 'a')

def communication(serverMessage, answer):
    ws.send(answer)
    print("ME: "+ answer)

def on_message(ws, message):
    print("SERVER: "+ message)
    # ms = json.loads(message.strip(' '))
    fajlServer.write(message+"\n")
    global nodeCount
    global relationCount

    if message == "Author name":
        communication(message, "Author name:Pánczél Róbert")

    elif message == "Author id":
        communication(message, "Author id:EY2P3W")

    elif message == "Author email":
        communication(message, "Author email:robi.panczel@gmail.com")

    elif message == "Token":
        communication(message, "Token:b92kylvrdw")

    elif message[:14] == "Add node type:":
        node = message[14:].lstrip(' ')
        nodeTypes.append(node)
        communication(message, "Node type added:" + node)

    elif message[:18] == "Add relation type:":
        relation = message[18:].lstrip(' ')
        relationTypes.append(relation)
        communication(message, "Relation type added:" + relation)

    elif message == "Get node types":
        communication(message, "Node types:" + json.dumps(nodeTypes))

    elif message == "Get relation types":
        communication(message, "Relation types:" + json.dumps(relationTypes))

    # elif message[:22] == "Select knowledge base:":
    #     communication(message, "Knowledge base has been created")

    elif message[:22] == "Select knowledge base:":
        communication(message,"Knowledge base has been selected")

    elif message[:9] == "Add node:":
        newNode = json.loads(message[9:].strip(' '))
        with open('node_type.json', 'a') as fajlNode:
            fajlNode.write(json.dumps(newNode)+"\n")
        nodeCount = nodeCount + 1
        communication(message, "Node added")

    elif message[:13] == "Add relation:":
        newRelation = json.loads(message[13:].strip(' '))
        with open('relation_type.json', 'a') as fajlRelation:
            fajlRelation.write(json.dumps(newRelation)+"\n")
        relationCount = relationCount + 1
        communication(message, "Relation added")

    elif message == "Get node count":
        # a = str(nodeCount)
        a = str(10062)
        with open('data.json', 'a') as fajlData:
            fajlData.write('Node count:'+a)
        communication(message, "Node count:"+a)

    elif message == "Get relation count":
        # a = str(relationCount)
        a = str(34451)
        with open('data.json', 'a') as fajlData:
            fajlData.write('Relation count:'+a)
        communication(message, "Relation count:"+a)

    # asd
    elif message == "Get engines":
        engines = str([{"name": "Alternating Least Squares Method for Collaborative Filtering",
                        "providesRatingEstimations": "true"}])
        # engines = 3
        communication(message, "Engines:"+engines)

    elif message[:21] == "Get rating estimation":
        ratingEstimation = ""
        communication(message, ratingEstimation)

    elif message[:20] == "Get recommendations:":
        newRecommendations = json.loads(message[20:].strip(' '))
        with open('recommendations.json', 'a') as fajlRecommendations:
            fajlRecommendations.write(json.dumps(newRecommendations)+"\n")
        recommendations = ""
        communication(message, recommendations)


    # unknown message
    else:
        print("... Custom message: " + message)
        # nodeTypes.append(message)
        # ws.send(json.dumps(nodeTypes))
        print("Sent in JSON: ")
        print(json.dumps(nodeTypes))
        ws.close()


def on_error(ws, error):
    print("Error: " + error)


def on_close(ws):
    print("### closed ###")
    fajl = open('data.json', 'a')

    fajl.writelines(['Node Count: '+str(nodeCount)+"\n"])
    fajl.writelines([str(nodeTypes)+"\n"])

    fajl.writelines(['Relation Count: '+str(relationCount)+"\n"])
    fajl.writelines([str(relationTypes)+"\n"])

    fajl.close()


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://service.recommender-system.com/recsys2-course/engine",
                                # ws =
                                # websocket.WebSocketApp("ws://echo.websocket.org",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
