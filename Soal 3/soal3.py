try:
    file1 = input("Masukkan nama file pertama : ")
    file2 = input("Masukkan nama file kedua : ")

    handle1 = open(file1)
    handle2 = open(file2)

    set1 = set()
    set2 = set()

    for baris in handle1:
        kata_kata = baris.split()
        for kata in kata_kata:
            kata = kata.strip(".,?!-:").lower()
            set1.add(kata)

    for baris in handle2:
        kata_kata = baris.split()
        for kata in kata_kata:
            kata = kata.strip(".,?!-:").lower()
            set2.add(kata)

    hasil = set1 & set2
    print(f"Kata-kata yang muncul pada kedua file tersebut : {hasil}")

except:
    print("Error.. File tidak ditemukan, silahkan coba lagi.")

