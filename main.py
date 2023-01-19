import json
import time
import requests


# JSON lar yükleniyor.
f = open("data/042.json")
data = json.load(f)
chunckVeri = []

#chunk işlemi yapılıyor
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# Liste chunk ile eşit dağıtılıyor.
chunckVeri = list(divide_chunks(data, 200))


#Json oluşturan Foknsiyon
def gonderiStrOlustur(liste):
    urunler = {
        "items" : liste
    }
    return json.dumps(urunler)

# Fiyat Gönderme Fonksiyonu
def FiyatGonder():
    url = "https://apis.ciceksepeti.com/api/v1/Products/price-and-stock"
    for i in chunckVeri:
        payload = gonderiStrOlustur(i)
        print(payload)
        headers = {
            'x-api-key': 'appCode',
            'Content-Type': 'application/json'
        }
        response = requests.request("PUT", url, headers=headers, data=payload)
        print(response.text)
        time.sleep(2)
    print("Bitti")



FiyatGonder()
