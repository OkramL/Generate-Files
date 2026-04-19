import os
import random
import string

def loo_sisu(suurus_kb):
    suurus_baitides = suurus_kb * 1024
    return ''.join(random.choices(
        string.ascii_letters + string.digits + ' \nõäöüÕÄÖÜ',
        k=suurus_baitides
    ))

def loo_fail(kaust, failinimi, suurus_kb):
    tee = os.path.join(kaust, failinimi)
    with open(tee, "w", encoding="utf-8") as f:
        f.write(loo_sisu(suurus_kb))

def genereeri_failinimi(eesnimi, perenimi, laiendid):
    baasnimed = [
        "andmed", "aruanne", "märkus", "projekt",
        "fail", "kirjeldus", "logi", "test", "info", "ülevaade"
    ]

    lisad = [
        "", "_v1", "_final", "_2024",
        " koopia", " lõplik", " test"
    ]

    nimi = random.choice(baasnimed)

    # Otsusta kas lisada nimi (mitte alati)
    valik = random.choice(["none", "ees", "pere", "mõlemad"])
    if valik == "ees":
        nimi += f"_{eesnimi}"
    elif valik == "pere":
        nimi += f"_{perenimi}"
    elif valik == "mõlemad":
        nimi += f"_{eesnimi}_{perenimi}"

    nimi += random.choice(lisad)
    laiend = random.choice(laiendid)

    return f"{nimi}.{laiend}"

def main():
    eesnimi = input("Sisesta eesnimi: ").strip()
    perenimi = input("Sisesta perekonnanimi: ").strip()

    if not eesnimi or not perenimi:
        print("Eesnimi ja perekonnanimi peavad olema täidetud.")
        return

    siht = input("Sisesta sihtkaust (Enter = jooksev kaust): ").strip()

    if siht == "":
        juurkaust = os.getcwd()
    else:
        juurkaust = os.path.abspath(siht)
        os.makedirs(juurkaust, exist_ok=True)

    print(f"Kasutatav kaust: {juurkaust}")

    kaustad = [
        "Dokumendid",
        "Minu failid",
        "Tähtsad andmed",
        "Projektid 2024",
        "Varukoopiad",
        "Pildid ja meedia",
        "Ajutised failid",
        "Ülevaated",
        "Äri dokumendid",
        "Test kaust ÄÖÜ",
        "Veel üks kaust"
    ]

    laiendid = ["txt", "csv", "json", "log", "md"]

    kaustade_teed = []
    # Loo failid ka juurkausta
    juurkausta_failide_arv = random.randint(10, 30)

    for _ in range(juurkausta_failide_arv):
        failinimi = genereeri_failinimi(eesnimi, perenimi, laiendid)
        suurus = random.randint(1, 5)
        loo_fail(juurkaust, failinimi, suurus)
        
    for kaust in kaustad:
        tee = os.path.join(juurkaust, kaust)
        os.makedirs(tee, exist_ok=True)
        kaustade_teed.append(tee)

    failide_arv = random.randint(200, 400)

    for _ in range(failide_arv):
        kaust = random.choice(kaustade_teed)
        failinimi = genereeri_failinimi(eesnimi, perenimi, laiendid)
        suurus = random.randint(1, 5)
        loo_fail(kaust, failinimi, suurus)

    print(f"Loodud {failide_arv} faili.")

if __name__ == "__main__":
    main()