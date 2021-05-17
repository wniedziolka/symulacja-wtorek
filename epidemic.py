# -*- coding: utf-8 -*-
"""Program do symulacji rozprzestrzeniania choroby w populacji
Kod do wykorzystania na zajęciach 01.04.2020
"""

import random


class Pacjent:
    """Pojedyncza osoba w symulacji. 
    
    Atrybuty:
        x (float): współrzędna x pozycji Pacjenta
        y (float): współrzędna y pozycji Pacjenta
        status (str): status ze zbioru 'zdrowy', 'chory', 'nosiciel'
    
    """
    
    def __init__(self, x=0, y=0, czy_zdrowy=True):
        self.x = x
        self.y = y
        if czy_zdrowy:
            self.status = 'zdrowy'
        else:
            self.status = 'chory'
            
            
    def ruch(self):
        """Wykonaj ruch zmieniając współrzędne x,y.
        
        Zdrowy pacjent przesuwa się o 0-1, a chory o 0-0.1"""
        if self.status == 'chory':
            zasieg = 0.1
        else:
            zasieg = 1
        self.x = self.x + random.uniform(-zasieg, zasieg)
        self.y = self.y + random.uniform(-zasieg, zasieg)
        
        
    def __str__(self):
        return "Pacjent " + self.status + " @ "  + str(self.x) + " x " + str(self.y)
        
    
    
class Populacja:
    """Zbiór Pacjentów w ograniczonym obszarze przestrzeni
    
    Atrybuty:
        szerokosc (float): szerokosć dostępnego obszaru
        wysokosc (float): wysokosć dostępnego obszaru
        
    """
        
    def __init__(self, n, wysokosc=100, szerokosc=100):
        """Tworzy populację n Pacjentów na danym obszarze.
        
        Argumenty:
            n (int): liczba pacjentów
            wysokosc (float, optional): wysokosć planszy
            szerokosc (float, optional): szerokosć planszy            
        """
        self._pacjenci = []
        self.__wysokosc = wysokosc
        self.__szerokosc = szerokosc
        
        for i in range(n):
            x = random.uniform(0, szerokosc)
            y = random.uniform(0, wysokosc)
            zdrowy = random.choices( [True, False], [80, 20] )[0]
            self._pacjenci.append( Pacjent(x, y, zdrowy) )
    
    def set_szerokosc(self, value):
        if self.szerokosc > value:
            for pacjent in self._pacjenci:
                if pacjent.x > value:
                    pacjent.x = random.uniform(0, value)
        self.__szerokosc = value
    
    def set_wysokosc(self, value):
        if self.wysokosc > value:
            for pacjent in self._pacjenci:
                if pacjent.y > value:
                    pacjent.y = random.uniform(0, value)
        self.__wysokosc = value
    
    def get_szerokosc(self):
        return self.__szerokosc
    
    def get_wysokosc(self):
        return self.__wysokosc
    
    wysokosc = property(get_wysokosc, set_wysokosc)
    szerokosc = property(get_szerokosc, set_szerokosc)

    def __str__(self):
        s = ""
        for p in self._pacjenci:
            s += str(p) + "\n"
        return s
    
    
    def zapisz_do_pliku(self, nazwa_pliku):
        print("TODO: w tym miejscu powinno sie zapisac do pliku {}".format(nazwa_pliku))
        
    
    def ruch(self):
        """ Wykonaj ruch przesuwając każdego z pacjentów"""
        for p in self._pacjenci:
            p.ruch()
            p.x = p.x % self.szerokosc
            p.y = p.y % self.wysokosc
