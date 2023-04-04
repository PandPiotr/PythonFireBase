import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyD0pA_Ys2PMqTHQZCPHoso7zuhpLn9kfo0",
  "authDomain": "pythonqt-3b164.firebaseapp.com",
  "databaseURL": "https://pythonqt-3b164-default-rtdb.firebaseio.com",
  "projectId": "pythonqt-3b164",
  "storageBucket": "pythonqt-3b164.appspot.com",
  "messagingSenderId": "79517993418",
  "appId": "1:79517993418:web:17b60769458a0e3731e733",
  "measurementId": "G-7GYB3YZBDG"
};
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

#uczen = {"nazwa": "Martra", "wiek": 10, "waga": 200}
# uczen1 = {"nazwa": "Kondrat", "wiek": 19, "waga": 70}
# uczen2 = {"nazwa": "Marusz", "wiek": 32, "waga": 97.6}
# db.child("uczniowie").child("Moje ID niemieckie").set(uczen2)
# db.child("uczniowie").child("Moje ID nie niemieckie").set(uczen1)
# print("dziala")
# uczniowie = db.child("uczniowie").get()
# for uczen in uczniowie.each():
#   print(uczen)
#   print(uczen.key())
#   print(uczen.val())
# for uczen in uczniowie.each():
#   if uczen.val()["nazwa"] == "Piotr":
#     db.child("uczniowie").child(uczen.key()).update({"waga": 100})
#     print(uczen)

# ludz ={"imie": "Maruszek", "waga": 87, "wzrost": 1.6}
# db.child("db_skasowania").push(ludz)
# ludzie = db.child("db_skasowania").get()
# for ludz in ludzie:
#   if ludz.val()["imie"] == "Maruszek":
#     db.child("db_skasowania").child(ludz.key()).remove()
# db.child("db_skasowania").child("id_1").child("waga").remove()
# db.child("db_skasowania").child("id_1").remove()
hagrid = db.child("db_skasowania").child("-NSA6rGDC3SCbkYvB7dL").get()
print(hagrid.val())
