# sub1.py (Subscriber)
import paho.mqtt.client as mqtt
import time
import datetime
from datetime import date

# Callback fungsi on_message
def on_message(client, userdata, message):
    temp = float(message.payload.decode("utf-8"))
    a = datetime.datetime.now()
    hr = a.hour
    mn = a.minute
    sc = a.second
    print(f"Suhu Kota Bandung pada tanggal {str(date.today())} jam {hr}:{mn}:{sc} adalah {temp} °C")

# Definisi nama broker
nama_broker = "localhost"

# Buat client baru bernama P1
print("Creating new instance")
client = mqtt.Client("P1")

# Kaitkan callback on_message ke client
client.on_message = on_message

# Buat koneksi ke broker
print("Connecting to broker")
client.connect(nama_broker)

# Jalankan loop client
client.loop_start()

# Client melakukan subscribe ke topik suhu
print("Subscribing Weather Sensor")
client.subscribe("Suhu")

# Loop forever
while True:
    # Berikan waktu tunggu 1 detik
    time.sleep(1)

# Stop loop
client.loop_stop()