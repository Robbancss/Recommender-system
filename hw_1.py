import json
import _thread
import websocket
import re
import pprint

nodeTypes = []
relationTypes = []
nodeCount = 0
relationCount = 0


def on_message(ws, message):
    print("Message: %s" % message)

    global nodeCount
    global relationCount
    # basic identification
    if message == "Author name":
        print("... Sending: " + message)
        ws.send("Author name:Pánczél Róbert")
        print("Sent: " + message)

    elif message == "Author id":
        print("... Sending: " + message)
        ws.send("Author id:EY2P3W")
        print("Sent: " + message)

    elif message == "Author email":
        print("... Sending: " + message)
        ws.send("Author email:robi.panczel@gmail.com")
        print("Sent: " + message)

    # my token : b92kylvrdw
    elif message == "Token":
        print("...Sending ", message, " b92kylvrdw")
        ws.send("Token:b92kylvrdw")
        print("Sent: ", message)

    # adding types
    elif message[:14] == "Add node type:":
        print("... Sending: " + message)
        node = message[14:].lstrip(' ')
        nodeTypes.append(node)
        ws.send("Node type added:" + node)
        print("Sent: " + message)
        # fajl = open('node_type.json', 'a')
        # fajl.write(json.dumps(node))
        # fajl.close()

    elif message[:18] == "Add relation type:":
        print("... Sending: " + message)
        relation = message[18:].lstrip(' ')
        relationTypes.append(relation)
        ws.send("Relation type added:" + relation)
        print("Sent: " + message)
        # fajl = open('relation_type.json', 'a')
        # fajl.write(json.dumps())
        # fajl.close()

    # getting types
    elif message == "Get node types":
        print("... Sending: " + message)
        ws.send("Node types:" + json.dumps(nodeTypes))
        print("Sent node types: ", nodeTypes)

    elif message == "Get relation types":
        print("... Sending: " + message)
        ws.send("Relation types:" + json.dumps(relationTypes))
        print("Sent relation types: ", relationTypes)

    # checking the knowledge base
    elif message[:22] == "Select knowledge base:":
        print("... Sending knowledge base")
        ws.send("Knowledge base has been created")
        print("Sent Knowledge base has been created")

    # elif message[:22] == "Select knowledge base:":
    #     print("..Sending knowledge base")
    #     ws.send("Knowledge base has been selected")
    #     print("Sent Knowledge base has been selected")

    # Add node
    elif message[:9] == "Add node:":
        print("..Sending:", message)
        newNode = str(message[9:])
        fajl = open('node_type.json', 'a')
        fajl.writelines(newNode+"\n")
        ws.send("Node added")
        nodeCount = nodeCount + 1
        # fajl.close()

    # Add relation
    elif message[:13] == "Add relation:":
        print("..Sending:", message)
        newRelation = str(message[13:])
        fajl = open('relation_type.json', 'a')
        fajl.print(newRelation)
        ws.send("Relation added")
        relationCount = relationCount + 1
        # fajl.close()

    # Get Node Count
    elif message == "Get node count":
        print("..Sending Node Count")
        fajl = open('data.json', 'a')
        a = str(nodeCount)
        fajl.write(json.dumps(['Node count:', a]))
        ws.send("Node count:"+a)
        # fajl.close()

    # Get relation Count
    elif message == "Get relation count":
        print("..Sending relation count")
        fajl = open('data.json', 'a')
        a = str(relationCount)
        fajl.write(json.dumps(['Relation count:', a]))
        ws.send("Relation count:"+a)
        # fajl.close()

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
    fajl.write(json.dumps(['Node Count:', nodeCount]))
    fajl.write(json.dumps(['Relation Count:', relationCount]))
    fajl.write(json.dumps([nodeTypes]))
    fajl.write(json.dumps([relationTypes]))
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
