import json
import io
import websocket
import codecs

nodeTypes = []
relationTypes = []
nodeCount = 0
relationCount = 0

def communication(serverMessage, answer):
    with open('aaa.json',mode='a') as aaa:
        aaa.write(answer+"\n")
    print("ME: "+ answer)

with open('server.json', 'r') as server:
            for message in server.readlines():

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
                    #
                    person = newRecommendations.get("personId")
                    count = newRecommendations.get("count")
                    with open.. 
                    #
                    recommendations = ""
                    communication(message, recommendations)


                # unknown message
                else:
                    print("... Custom message: " + message)
                    # nodeTypes.append(message)
                    # ws.send(json.dumps(nodeTypes))
                    print("Sent in JSON: ")
                    print(json.dumps(nodeTypes))