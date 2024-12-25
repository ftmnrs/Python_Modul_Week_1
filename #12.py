#12. soru 
for ders in range(1, 5):
    print(f"\nDers {ders}:")


    vize=float(input("vize notunuzu giriniz:"))
    final=float(input("final notunuzu giriniz:"))

    ortalama = (vize * 0.4) + (final * 0.6)
    if ortalama >= 50:
        print("successful")
    else:
        print ("Failed")
