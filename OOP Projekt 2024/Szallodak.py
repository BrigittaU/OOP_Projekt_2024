from abc import ABC, abstractmethod
from datetime import datetime
import random


class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar
        self.foglalva = []

    @abstractmethod
    def foglal(self, datum):
        pass

    @abstractmethod
    def lemond(self, datum):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 5000)

    def foglal(self, datum):
        self.foglalva.append(datum)
        print(f"Egyágyas szoba {self.szobaszam} foglalva az időpontra: {datum}. Ár: {self.ar} Ft")

    def lemond(self, datum):
        if datum in self.foglalva:
            self.foglalva.remove(datum)
            print(f"Egyágyas szoba {self.szobaszam} foglalása lemondva az időponton: {datum}")
        else:
            print(f"Nincs ilyen foglalás a(z) Egyágyas szoba {self.szobaszam} számára az időponton: {datum}")


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 8000)

    def foglal(self, datum):
        self.foglalva.append(datum)
        print(f"Kétágyas szoba {self.szobaszam} foglalva az időpontra: {datum}. Ár: {self.ar} Ft")

    def lemond(self, datum):
        if datum in self.foglalva:
            self.foglalva.remove(datum)
            print(f"Kétágyas szoba {self.szobaszam} foglalása lemondva az időponton: {datum}")
        else:
            print(f"Nincs ilyen foglalás a(z) Kétágyas szoba {self.szobaszam} számára az időponton: {datum}")


class Lakosztaly(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 40000)

    def foglal(self, datum):
        self.foglalva.append(datum)
        print(f"Lakosztály {self.szobaszam} foglalva az időpontra: {datum}. Ár: {self.ar} Ft")

    def lemond(self, datum):
        if datum in self.foglalva:
            self.foglalva.remove(datum)
            print(f"Lakosztály {self.szobaszam} foglalása lemondva az időponton: {datum}")
        else:
            print(f"Nincs ilyen foglalás a(z) Lakosztály {self.szobaszam} számára az időponton: {datum}")


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, datum):
        print("Milyen típusú szobát szeretne foglalni?")
        print("1. Egyágyas szoba")
        print("2. Kétágyas szoba")
        print("3. Lakosztály")
        valasztas = input("Válasszon: ")

        if valasztas == "1":
            szoba_tipus = EgyagyasSzoba
        elif valasztas == "2":
            szoba_tipus = KetagyasSzoba
        elif valasztas == "3":
            szoba_tipus = Lakosztaly
        else:
            print("Hibás választás!")
            return

        szobak_tipus_szerint = [szoba for szoba in self.szobak if isinstance(szoba, szoba_tipus)]
        if szobak_tipus_szerint:
            szoba = random.choice(szobak_tipus_szerint)
            if datum not in szoba.foglalva:
                szoba.foglal(datum)
            else:
                print("A választott szoba már foglalt az adott időpontra.")
        else:
            print("Nincs ilyen típusú szoba.")

    def lemondas(self, datum):
        while True:
            datum_input = input("Add meg a lemondani kívánt foglalás időpontját (YYYY-MM-DD formátumban): ")
            try:
                datum = datetime.strptime(datum_input, "%Y-%m-%d")
                break
            except ValueError:
                print("Hibás dátum. Kérem adjon meg egy valódi dátumot!")

        for szoba in self.szobak:
            if datum in szoba.foglalva:
                szoba.lemond(datum)
                return
        print("Nincs foglalás az adott időpontra.")

    def listaz_foglalasok(self):
        print("Foglalások:")
        for szoba in self.szobak:
            foglalasok_str = ", ".join([datum.strftime("%Y-%m-%d") for datum in szoba.foglalva])
            print(f"  Szoba {szoba.szobaszam}: {szoba.ar} Ft, foglalva: [{foglalasok_str}]")


def main():
    szalloda = Szalloda("Példa Szálloda")

    szoba1 = EgyagyasSzoba(101)
    szoba2 = EgyagyasSzoba(102)
    szoba3 = KetagyasSzoba(201)
    lakosztaly1 = Lakosztaly(301)

    szalloda.add_szoba(szoba1)
    szalloda.add_szoba(szoba2)
    szalloda.add_szoba(szoba3)
    szalloda.add_szoba(lakosztaly1)

    while True:
        print("\nVálassz egy műveletet:")
        print("1. Időpont Foglalás")
        print("2. Időpont Lemondás")
        print("3. Időpont Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Válassz: ")

        if valasztas == "1":
            print("Időpont Foglalás")
            while True:
                datum_input = input("Add meg a foglalás időpontját (YYYY-MM-DD formátumban): ")
                try:
                    datum = datetime.strptime(datum_input, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Hibás dátum. Kérem adjon meg egy valódi dátumot!")
            szalloda.foglalas(datum)
        elif valasztas == "2":
            print("Időpont Lemondás")
            szalloda.lemondas(datum)
        elif valasztas == "3":
            print("Időpont Foglalások listázása")
            szalloda.listaz_foglalasok()
        elif valasztas == "0":
            print("Kilépés")
            break
        else:
            print("Hibás választás!")


if __name__ == "__main__":
    main()



