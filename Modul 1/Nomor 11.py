import datetime;
def apakahKabisat(n):
    if (n % 4) == 0:
        if (n % 100) == 0:
            if (n % 400) == 0:
                print("Tahun Kabisat")
            else:
                print("Bukan Tahun Kabisat")
        else:
            print("Tahun Kabisat")
    else:
        print("Bukan Tahun Kabisat")
