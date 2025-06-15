pocetna_pozicija = 0
cilj = 80
trenutna_pozicija  = 0
brzina = 20

for x in range(10):
    print(trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("Stigao do cilja.")
        break
    elif trenutna_pozicija > cilj:
        print("Premasili ste")
    elif trenutna_pozicija < cilj:
        print("Niste jos stigli")
    trenutna_pozicija += brzina
