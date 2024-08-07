import random
import string
while True:

    sifre = ""
    string.ascii_letters
    string.digits
    string.punctuation
    uzunluk=int(input("Welcome to random password generator.\n Please enter the lend of your password:"))
    secim=input(" If you want to add any special character (e.g.:?), please enter: ")
    kelime=input(" If you want to add any special word, please enter: ")

    if kelime != "" and uzunluk > len(kelime):
        ozel_kelime = kelime
    elif kelime != "" and uzunluk < len(kelime):
        print("Password lend can not be greater than word lend.")
        exit()
    else:
        ozel_kelime = ""

    sifre_uzunlugu = uzunluk - len(ozel_kelime) - 1 

    if secim in string.punctuation:
        ozel_secim=secim
    else:
        None

    for i in range(sifre_uzunlugu):
        sifre += random.choice(string.ascii_letters + string.digits)

    sifre_liste = list(sifre)
    sifre_liste.insert(random.randint(0, len(sifre_liste)), ozel_kelime)
    sifre_liste.insert(random.randint(0, len(sifre_liste)), ozel_secim)
    sifre = "".join(sifre_liste)

    print(sifre)