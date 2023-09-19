file_size_gb=float(input("Введіть розмір (ГБ): "))
speed=float(input("Введіть швидкість  (bit/sec): "))
choice=input("Оберіть 'години', 'хвилини' або секунди для обчислення (введіть '1' або '2' або '3')")
file_size_bits = 1024*1024*1024*8*file_size_gb
zagruzka_seconds = file_size_bits/speed
if choice=='1':
    zagruzka_time = zagruzka_seconds/3600
    print(f"Час завантаження: {zagruzka_time:.2f}годин.")
elif choice=='2':
    zagruzka_time = zagruzka_seconds/60
    print(f"Час завантаження: {zagruzka_time:.2f}хвилин.")
elif choice=='3':
    print(f"Час завантаження: {zagruzka_seconds :.2f}секунд.")
else:
    print("Error")



