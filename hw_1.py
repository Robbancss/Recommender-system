import websocket
import _thread
import json

nodeType = []
relationType = []

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
            
    elif message == "Add node type:":
            nodetype = message[14:].lstrip(' ')
            print("... Adding node type: " + nodetype)
            nodeType.append(nodetype)
            #ws.send("Node type added:" + nodetype)
            print("Sent: Node type added: " + nodetype)
            
    elif message == "Add relation type:":
            reltype = message[18:].lstrip(' ')
            print("... Adding relation type: " + reltype)
            relationType.append(reltype)
            #ws.send("Relation type added:" + reltype)
            print("Sent: Relation type added: " + reltype)
            
    elif message == "Get node types":
            print("... Sending: " + message)
            #ws.send("Node types:" + json.dumps(nodeType))
            print("Sent: ")
            print(nodeType)
            
    elif message == "Get relation types":
            print("... Sending: " + message)
            #ws.send("Relation types:" + json.dumps(relationType))
            print("Sent: ")
            print(relationType)
            
    else:
            print("... Custom message: " + message)
            nodeType.append(message)
            ws.send(json.dumps(nodeType))
            print("Sent in JSON: ")
            print(json.dumps(nodeType))
            ws.close()

def on_error(ws, error):
    print("Error: " + error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send("Handsake")
    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()