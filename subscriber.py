# subscriber
import time
import paho.mqtt.client as mqtt_client
import requests
from logger import add_logger
logger = add_logger("subscriber")
broker = "broker.emqx.io"


def on_message(client, userdata, message):
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    logger.info(f"received message = { data}")


id = requests.get("http://127.0.0.1:8000/get_id").json()['user_id']
logger.info(f"id = {id}")

client = mqtt_client.Client(
    mqtt_client.CallbackAPIVersion.VERSION1,
    id
)
logger.info("connected")
client.on_message = on_message

logger.info(f"Connecting to {broker}")
client.connect(broker)
client.loop_start()
logger.info("start subscribe")
client.subscribe("lab/leds/state")
time.sleep(1800)
logger.info("stop subscribe")
client.disconnect()
client.loop_stop()
