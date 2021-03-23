import websocket
import json
from utils import logger


base = f"wss://stream.binance.com:9443/ws"


class WebsocketWrapper:
    def __init__(self):
        websocket.enableTrace(True)
        self.ws = None
        self.subscription = {
            'method': 'SUBSCRIBE',
            'params': ['btcusdt@aggTrade'],
            'id': 1}
        self.logger = logger.Logger('journal.log')

    def on_open(self, ws):
        def connect_ws(*args):
            ws.send(json.dumps(self.subscription))
        connect_ws()

    def on_message(self, ws, message):
        self.logger.log_info(message)

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print('closed')

    def connect(self):
        self.ws = websocket.WebSocketApp(
            base,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close)
        self.ws.run_forever()


if __name__ == '__main__':
    wsw = WebsocketWrapper()
