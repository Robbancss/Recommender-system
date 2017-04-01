import websocket
import _thread
import json

nodeTypes = []
relationTypes = []

def on_message(ws, message):
    print("Message: %s" % message)
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
            
    elif message[:14] == "Add node type:":
        print("... Sending: " + message)
        nodetype = message[14:].lstrip(' ')
        nodeTypes.append(nodetype)
        ws.send("Node type added:" + nodetype)
        print("Sent: " + message)
        f = open('data.json', 'a')
        f.write(nodetype)  

    elif message[:18] == "Add relation type:":
        print("... Sending: " + message)
        relationtype = message[18:].lstrip(' ')
        relationTypes.append(relationtype)
        ws.send("Relation type added:" + relationtype)
        print("Sent: " + message)
        f = open('data.json', 'a')
        f.write(relationtype)  

    elif message == "Get node types":
        print("... Sending: " + message)
        ws.send("Node types:" + json.dumps(nodeTypes))
        print("Sent node types: ")
        print(nodeTypes)
        
    elif message == "Get relation types":
        print("... Sending: " + message)
        ws.send("Relation types:" + json.dumps(relationTypes))
        print("Sent relation types: ")
        print(relationTypes)
        print()
        
    else:
        print("... Custom message: " + message)
        nodeTypes.append(message)
        ws.send(json.dumps(nodeTypes))
        print("Sent in JSON: ")
        print(json.dumps(nodeTypes))
        ws.close()

def on_error(ws, error):
    print("Error: " + error)

def on_close(ws):
    prisnt("### closed ###")
    f = open('data.json', 'a')
    f.write(relationTypes)
    f.write(nodeTypes)  

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://service.recommender-system.com/recsys2-course/engine",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.run_forever()