def rekursif(jumlah, current_index=1):
    if current_index > jumlah:
        return 0
    else:
        angka = int(input(f"Masukkan angka ke-{current_index}: "))
        return angka + rekursif(jumlah, current_index + 1)

def main():
    jumlah = int(input("Masukkan Jumlah: "))
    hasil = rekursif(jumlah)
    print(f"Hasil penjumlahan: {hasil}")

if __name__ == "__main__":
    main()
