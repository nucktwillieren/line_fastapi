import paho.mqtt.client as mqtt


class Listener:
    def __init__(self, scope, username, password) -> None:
        self.scope = scope
        self.username = username
        self.password = password

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(f"ideasky/{self.scope}/#")

    def on_message(self, client, userdata, msg):
        print(msg.topic+" " + msg.payload.decode('utf-8'))

    def run(self):

        client = mqtt.Client()

        client.on_connect = self.on_connect

        client.on_message = self.on_message

        client.username_pw_set(self.username, self.password)

        client.connect("ideasky.app", 1883, 60)

        client.loop_start()
