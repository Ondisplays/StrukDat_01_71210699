print("""
========== Menu ==========
1. Pertambahan
2. Pengurangan
3. Perkalian
4. Pembagian

Q. End Program
""")
while True:

    choice = input("Menu berapa :")

    if choice == "1":
        a = int(input("Masukan angka pertama :"))
        b = int(input("Masukan angka kedua :"))
        print(a + b)

    elif choice == "2":
        a = int(input("Masukan angka pertama :"))
        b = int(input("Masukan angka kedua :"))
        print(a - b)

    elif choice == "3":
        a = int(input("Masukan angka pertama :"))
        b = int(input("Masukan angka kedua :"))
        print(a * b)

    elif choice == "4":
        a = int(input("Masukan angka pertama :"))
        b = int(input("Masukan angka kedua :"))
        print(a / b)

    elif choice == "Q" or choice == "q":
        break

    else:
        print("Angka tidak sesuai")
