#PUB1
# pub1.py (Publisher)
import paho.mqtt.client as mqtt
import requests
import time

# Definisikan nama broker yang akan digunakan
nama_broker = "test.mosquitto.org"  # Ganti dengan alamat broker

# Buat client baru bernama P2
print("Creating new instance")
client = mqtt.Client("P2")

# Koneksi ke broker
print("Connecting to broker")
client.connect(nama_broker)
client.loop_start()

# Fungsi untuk mengambil data dari API cuaca baru
def data_suhu(query):
    url = "https://api.weatherapi.com/v1/current.json?key=1cb5c317dbd04b81b2010700242404&q=" + query
    res = requests.get(url)
    return res.json()

# Fungsi untuk mencetak data suhu dan mengirimkannya ke subscriber
def print_suhu(result, city):
    temp = result['current']['temp_c']
    print(f"Suhu Kota {city} : {temp} °C")
    client.publish("Suhu", str(temp))  # Konversi suhu ke string

# Metode utama
def main():
    while True:
        try:
            cities = ["Bandung"]
            for city in cities:
                query = city
                w_data = data_suhu(query)
                print_suhu(w_data, city)
            time.sleep(10)  # Jeda 10 detik sebelum mengambil data untuk ketiga kota lagi
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)  # Jeda 10 detik sebelum mencoba lagi


if __name__ == '__main__':
    main()
    client.loop_stop()