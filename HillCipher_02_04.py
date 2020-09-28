# Nama  : Sitti Ufairoh Azzahra
#         Natasya Rizky Maharani
# NPM   : 140810180002
#         140810180004
# Deskripsi  : Program Hill Cipher 
import numpy as np

def mod_inverse(a, m) :
    a = a % m
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

def minor(m, i, j) :
    m = np.array(m)
    minor = np.zeros(shape = (len(m) - 1, len(m) - 1))
    p = 0
    for s in range(len(minor)) :
        if p == i :
            p += 1
        q = 0
        for t in range(len(minor)) :
            if q == j :
                q += 1
            minor[s][t] = m[p][q]
            q += 1
        p += 1
    return minor

def encrypt(x, mk = np.arange(4).reshape(2, 2)) :
    if mk.shape[0] != mk.shape[1] :
        print("Jumlah baris dan kolom kunci tidak sama!")
        return x
    elif len(x) < mk.shape[0] :
        print("Jumlah huruf lebih sedikit dari ordo matriks kunci!")
        return x

    x = list(x.upper())
    mx = list()
    for i in x :
        mx.append(int(ord(i)) - 65)
    mx = np.array(mx).reshape(int(len(x)/mk.shape[0]), mk.shape[0])

    my = np.dot(mx, mk) % 26
    my = my.ravel().tolist()
    y = list()
    for i in my :
        y.append(chr(i + 65))
    y = ''.join(y)
    
    return y

def decrypt(y, mk = np.arange(4).reshape(2, 2)) :
    x = ''
    if mk.shape[0] != mk.shape[1] :
        print("Jumlah baris dan kolom kunci tidak sama!")
        return y
    elif len(y) < mk.shape[0] :
        print("Jumlah huruf lebih sedikit dari ordo matriks kunci!")
        return y
    
    y = list(y.upper())
    my = list()
    for i in y :
        my.append(int(ord(i)) - 65)
    my = np.array(my).reshape(int(len(y)/mk.shape[0]), mk.shape[0])

    adj = np.zeros(shape=(mk.shape[0], mk.shape[0]))
    for i in range(mk.shape[0]) :
        for j in range(mk.shape[0]) :
            adj[i][j] = (-1)**(i+j) * int(round(np.linalg.det(minor(mk,j,i)))) % 26

    mk = int(mod_inverse(np.linalg.det(mk), 26)) * adj.astype(int) % 26
    mx = np.dot(my, mk) % 26
    mx = mx.ravel().tolist()
    x = list()
    for i in mx :
        x.append(chr(i + 65))
    x = ''.join(x)

    return x

def hill_key(x, y) :
    if len(x) != len(y) :
        print("Jumlah huruf plaintext dan ciphertext berbeda!")
        return 0
    
    m = np.sqrt(len(x)).astype(int)

    x = list(x[:(m*m)].upper())
    mx = list()
    for i in x :
        mx.append(int(ord(i)) - 65)
    mx = np.array(mx).reshape(int(len(x)/m), m)

    adj = np.zeros(shape=(m, m))
    for i in range(m) :
        for j in range(m) :
            adj[i][j] = (-1)**(i+j) * int(round(np.linalg.det(minor(mx,j,i)))) % 26

    y = list(y[:(m*m)].upper())
    my = list()
    for i in y :
        my.append(int(ord(i)) - 65)
    my = np.array(my).reshape(int(len(y)/m), m)

    k = np.dot((int(mod_inverse(round(np.linalg.det(mx)), 26)) * adj.astype(int) % 26), my) % 26

    return k

def encrypt_() :
    k = []
    x = input("\nMasukkan Plaintext\t: ")
    rc = int(input("\nMasukkan Ordo Matriks\t: "))

    print("Masukkan isi matriks (satu angka langsung enter) \t: ")
    for i in range(rc) :
        m = []
        for j in range(rc) :
            m.append(int(input()))
        k.append(m)
    mk = np.array(k)

    y = encrypt(x, mk)
    x = decrypt(y, mk)

    print("\nHasil Enkripsi Plaintext\t: " + y)
    print("Dekripsi dari Ciphertext\t: " + x)

def searchkey() : 
    x = input("\nMasukkan Plaintext\t: ")
    y = input("Masukkan Ciphertext\t: ")
    k = hill_key(x, y)

    print("\nKey Hill Cipher adalah\t: ")
    print(k)


pil = int(input("\n==============================\n=     PROGRAM HILL CIPHER    =\n==============================\n1. Enkripsi\n2. Cari Kunci \n==============================\nMasukkan Pilihan Anda: "))
if pil == 1 :
    encrypt_()
elif pil == 2 :
    searchkey()
else :
    print("Pilihan salah.")