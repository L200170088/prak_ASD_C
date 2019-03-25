def cariTerkecil(Daftar):
    n = len(Daftar)
    #Anggap item pertama adalah yang terkecil
    terkecil = [Daftar[0]]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if Daftar[i].uangSaku < terkecil[0].uangSaku:
            terkecil = [Daftar[i]]
        elif Daftar[i].uangSaku == terkecil[0].uangSaku:
            terkecil.append(Daftar[i])
    return terkecil
