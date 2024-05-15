import paho.mqtt.client as mqtt
import time
import datetime
from datetime import date
import threading

# Inisialisasi variabel untuk menyimpan total suhu dari ketiga kota
total_suhu = 0
jumlah_data = 0

# Buat lock untuk menghindari kondisi balapan
lock = threading.Lock()

# Callback fungsi on_message
def on_message(client, userdata, message):
    global total_suhu, jumlah_data
    
    temp = float(message.payload.decode("utf-8"))
    
    with lock:
        total_suhu += temp  # Menambahkan nilai suhu ke total_suhu
        jumlah_data += 1  # Menghitung jumlah data suhu yang diterima
    
    a = datetime.datetime.now()
    hr = a.hour
    mn = a.minute
    sc = a.second
    # print("Suhu Kota Bandung pada tanggal {} jam {}:{}:{} adalah {} °C".format(str(date.today()), hr, mn, sc, temp))

# Definisi nama broker
nama_broker = "test.mosquitto.org"

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
    # Tunggu 10 detik untuk mengumpulkan data suhu
    time.sleep(10)
    
    # Hitung rata-rata suhu
    with lock:
        if jumlah_data > 0:
            rata_rata_suhu = total_suhu / jumlah_data
            print(f"Rata-rata suhu dari ketiga kota pada tanggal {str(date.today())} adalah {rata_rata_suhu} °C")
        else:
            print("Tidak ada data suhu yang diterima.")
        
        # Reset total_suhu dan jumlah_data untuk perhitungan berikutnya
        total_suhu = 0
        jumlah_data = 0

# Stop loop (baris ini tidak akan pernah tercapai dalam loop while True)
client.loop_stop()