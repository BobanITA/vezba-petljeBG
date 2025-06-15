pocetna_pozicija = 20
cilj = 80
trenutna_pozicija = 0
brzina = 20

for x in range(20):
    print(trenutna_pozicija)
    if trenutna_pozicija == cilj:
        print("stigao do cilja")
        break
    elif trenutna_pozicija > cilj:
        print("prosli ste")
        break
    elif trenutna_pozicija < cilj:
        print("niste jos stigli")
    trenutna_pozicija += brzina
