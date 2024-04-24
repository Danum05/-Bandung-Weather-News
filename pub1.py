# pub1.py (Publisher)
import paho.mqtt.client as mqtt
import requests

# Definisikan nama broker yang akan digunakan
nama_broker = "localhost"

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
    client.publish("Suhu", temp)

# Metode utama
def main():
    city = "Bandung"
    print()
    try:
        query = city
        w_data = data_suhu(query)
        print_suhu(w_data, city)
        print()
    except:
        print("Tidak ada data")

if __name__ == '__main__':
    main()
    client.loop_stop()