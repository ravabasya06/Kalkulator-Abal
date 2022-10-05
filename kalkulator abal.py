def ulang():

    angka1 = int(input("Masukkan angka pertama : "))
    angka2 = int(input("Masukkan angka kedua : "))
    perintah = input("Masukkan perintah (tambah / kurang / kali / bagi) : ")
    
    if perintah == "tambah":
        print("Hasilnya adalah : "+str(angka1 + angka2))
    elif perintah == "kurang":
        print("Hasilnya adalah : "+str(angka1 - angka2))
    elif perintah == "kali":
        print("Hasilnya adalah : "+str(angka1 * angka2))
    elif perintah == "bagi":
        print("Hasilnya adalah : "+str(angka1 / angka2))
    else:
        print("Saya tidak mengerti perintah yang diberi")
        
ulang()
        
perhitungan = input("Lakukan perhitungan lagi? ya / tidak : ")

if perhitungan == "ya":
    ulang()
elif perhitungan == "tidak":
    print("bruh")
else:
    print("Saya tidak mengerti perintah yang diberikan, saya akan mengira anda menjawab tidak.")