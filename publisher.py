# publisher
import random
import time

import paho.mqtt.client as mqtt_client
import requests

from logger import add_logger

logger = add_logger("publisher")

broker = "broker.emqx.io"
user_id = requests.get("http://127.0.0.1:8000/get_id").json()['user_id']
logger.info(f"id = {user_id}")
client = mqtt_client.Client(
    mqtt_client.CallbackAPIVersion.VERSION1,
    user_id
)

logger.info(f"Connect to {broker}")
logger.debug(client.connect(broker))
client.loop_start()

logger.info("start publish")
for i in range(10):
    state = "on" if random.randint(0, 1) == 0 else "off"
    state = state + "ArtemV"
    logger.info(f"State is {state}")
    client.publish("lab/leds/state", state)
    time.sleep(2)
logger.info("exit")
client.disconnect()
client.loop_stop()
