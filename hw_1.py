import json
import websocket
# import _thread
# import re
# import pprint

nodeTypes = []
relationTypes = []
nodeCount = 0
relationCount = 0

def communication(serverMessage, answer):
    print("SERVER: "+ serverMessage)
    ws.send(answer)
    print("ME: "+ answer)

def on_message(ws, message):
    # print("Message: %s" % message)

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

    elif message[:22] == "Select knowledge base:":
        communication(message, "Knowledge base has been created")

    # elif message[:22] == "Select knowledge base:":
    #     communication(message,"Knowledge base has been selected")

    elif message[:9] == "Add node:":
        newNode = str(message[9:])
        fajl = open('node_type.json', 'a')
        fajl.writelines(newNode+"\n")
        nodeCount = nodeCount + 1
        communication(message, "Node added")

    elif message[:13] == "Add relation:":
        newRelation = str(message[13:])
        fajl = open('relation_type.json', 'a')
        fajl.print(newRelation)
        relationCount = relationCount + 1
        communication(message, "Relation added")

    elif message == "Get node count":
        fajl = open('data.json', 'a')
        a = str(nodeCount)
        fajl.write(['Node count:', a])
        communication(message, "Node count:"+a)

    elif message == "Get relation count":
        fajl = open('data.json', 'a')
        a = str(relationCount)
        fajl.write(['Relation count:', a])
        communication(message, "Relation count:"+a)

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
    fajl.write(['Node Count:', nodeCount])
    fajl.write(['Relation Count:', relationCount])
    fajl.write([nodeTypes])
    fajl.write([relationTypes])
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
