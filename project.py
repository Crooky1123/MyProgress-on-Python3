# Mean

jumlahlist = input("jumlah list : ")

angkamean = []
stop = False
i = 0

# isi list mean
while(not stop):
    add = input("inputkan angka mean(1 saja dulu) : ".format(i))
    angkamean.append(add)

    # increment
    i += 1

    ask = input("jika sudah ketik n, jika belum enter : ")
    if(ask == "n"):
        stop = True

# hasil
intlist = list(map(int, angkamean))

hasil = sum(intlist) / int(jumlahlist)

print(f"meannya dari {intlist} adalah : {int(hasil)}")