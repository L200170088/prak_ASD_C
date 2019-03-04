x="asas"
def hitung(x):
    vokal = "aiueoAIUEO"
    aa=0
    for i in x:
        if i in vokal:
            aa+=1
    return(len(x),aa)

print(hitung("Surakarta"))
