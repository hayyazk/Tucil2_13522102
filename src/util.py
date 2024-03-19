import os

def mid_point (x1, x2):
    return (x1+x2)/2

def file_input():
    file = input("\nTuliskan nama file: ")
    file_path = "../test/" + file

    while not os.path.exists(file_path):
        print("File tidak ditemukan. Silahkan input ulang.")
        file = input("Tuliskan nama file yang akan di cek: ")
        file_path = "../test/" + file

    xpoints = []
    ypoints = []

    f = open(file_path, "r")
    for i in range(3):
        line = f.readline().strip()
        print(f"P{i}:", line)
        x, y = line.split()
        xpoints.append(int(x))
        ypoints.append(int(y))

    n_iter = int(f.readline().strip())
    print("Jumlah iterasi:", n_iter)

    f.close()
    return xpoints, ypoints, n_iter

def manual_input():
    xpoints = []
    ypoints = []

    for i in range (1, 4):
        point = input(f"Masukkan titik ke-{i}: ").split()
        xpoints.append(int(point[0]))
        ypoints.append(int(point[1]))

    n_iter = int(input("Masukkan jumlah iterasi: "))

    return xpoints, ypoints, n_iter