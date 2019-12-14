# -*- coding: utf-8"

class Perso() :
    def __init__(self, chance, moral, attaque, defence, pm, mana) :
        self.chance = chance
        self.moral = moral
        self.attaque = attaque
        self.defence = defence
        self.pm = pm
        self.mana = mana
        
        
    def jeter_sort(self) :
        dmg = 30*self.pm
        self.mana -= 4
        return dmg
        
    def frapper(self) :
        return "Il frappe"
