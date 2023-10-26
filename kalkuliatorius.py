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