import paho.mqtt.Client as mqtt

pub_client=mqtt.Client()
pub_client.connect('broker.hivemq.com',1883)
print('Broker Connected')

pub_client.publish('gpcet/ai','i am uzair')