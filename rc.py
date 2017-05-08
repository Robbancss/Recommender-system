import json
import io
import websocket
import codecs

def communication(serverMessage, answer):

def on_message(ws, message):
    
def on_error(ws, error):

def on_close(ws):

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://service.recommender-system.com/recsys2-course/engine",
                                # ws =
                                # websocket.WebSocketApp("ws://echo.websocket.org",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()
