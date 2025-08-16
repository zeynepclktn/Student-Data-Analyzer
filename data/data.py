import json


students = [
    {"ad": "Zeynep", "soyad": "Celikten", "yas": 25, "sehir": "İstanbul", "not": 90},
    {"ad": "İsmet", "soyad": "Tosun", "yas": 26, "sehir": "İstanbul", "not": 80},
    {"ad": "Eylül", "soyad": "Demir", "yas": 24, "sehir": "Barcelona", "not": 45},
    {"ad": "Ahmet", "soyad": "Yılmaz", "yas": 27, "sehir": "Ankara", "not": 65},
    {"ad": "Fatma", "soyad": "Kaya", "yas": 23, "sehir": "Malatya", "not": 70},
    {"ad": "Ercan", "soyad": "Şahin", "yas": 28, "sehir": "Sanlıurfa", "not": 55},
    {"ad": "Selin", "soyad": "Güneş", "yas": 22, "sehir": "İzmir", "not": 95}
]

with open ("student_data/data/data.json","w") as f :
    json.dump(students,f,ensure_ascii=False, indent=4)