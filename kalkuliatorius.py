while True:
    print("1. Jei norite sudėti įveskite *1*\n"
          "2. Jei norite atimti įveskite *2*\n"
          "3. Jei norite sudauginti įveskite *3*\n"
          "4. Jei norite padalinti įveskite *4*\n"
          "5. Jei norite išeiti iš programos įveskite *5*\n")
    pasirinkimas = input(">>>")
    print("*" * 20)
    if pasirinkimas == "5":
        print("Jūs išėjote iš programos.")
        break
    if pasirinkimas not in ("1", "2", "3", "4"):
        print("Tokio pasirinkimo nėra")
        continue
    ivestis1 = float(input("Įveskite pirmąjį skaičių: "))
    ivestis2 = float(input("Įveskite antrajį skaičių: "))
    if pasirinkimas == "1":
        print(f"Jūsų įvestų skaičių suma: {ivestis1 + ivestis2}")
    if pasirinkimas == "2":
        print(f"Jūsų įvestų skaičių skirtumas: {ivestis1 - ivestis2}")
    if pasirinkimas == "4":
        print(f"Jūsų įvestų skaičių dalmuo: {ivestis1 / ivestis2}")
