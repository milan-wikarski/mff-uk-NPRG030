#!/usr/bin/env python3
#coding: utf-8


class Clovek:
  def __init__(self, vek, dalsi=None):
    # věk člověka
    self.vek = vek
    # další člověk ve frontě
    self.dalsi = dalsi


class Fronta:
  def __init__(self):
    prev = None
    clovek = None
    for age in list(reversed(list(map(int, input().split())))):
      # for age in list(reversed([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])):
      clovek = Clovek(age, prev)
      prev = clovek

    self.prvni = clovek
    pass

  def __str__(self):
    if (self.prvni is None):
      return "PRAZDNY"

    res = ""

    clovek = self.prvni
    while (clovek is not None):
      res += str(clovek.vek) + " "
      clovek = clovek.dalsi

    return res.strip()

  def length(self):
    res = 0

    clovek = self.prvni
    while (clovek is not None):
      res += 1
      clovek = clovek.dalsi

    return res

  def getMaxAge(self):
    if (self.prvni is None):
      return 0

    max_age = self.prvni.vek

    clovek = self.prvni.dalsi
    while (clovek is not None):
      max_age = max(clovek.vek, max_age)
      clovek = clovek.dalsi

    return max_age

  def getMinAge(self):
    if (self.prvni is None):
      return 0

    min_age = self.prvni.vek

    clovek = self.prvni.dalsi
    while (clovek is not None):
      min_age = min(clovek.vek, min_age)
      clovek = clovek.dalsi

    return min_age

  def getLast(self):
    if (self.prvni is None):
      return None

    clovek = self.prvni
    while (clovek.dalsi is not None):
      clovek = clovek.dalsi

    return clovek

  def append(self, clovek):
    clovek.dalsi = None

    if (self.prvni is None):
      self.prvni = clovek
    else:
      self.getLast().dalsi = clovek

  def vyhodNejstarsi(self):
    if (self.prvni is None):
      return 0

    n_deleted = 0

    max_age = self.getMaxAge()

    while (self.prvni is not None and self.prvni.vek == max_age):
      self.prvni = self.prvni.dalsi
      n_deleted += 1

    clovek = self.prvni
    while (clovek is not None):
      while (clovek.dalsi is not None and clovek.dalsi.vek == max_age):
        clovek.dalsi = clovek.dalsi.dalsi
        n_deleted += 1

      clovek = clovek.dalsi

    return n_deleted

  def nejstarsiDozadu(self):
    if (self.prvni is None):
      return

    max_age = self.getMaxAge()
    n_deleted = self.vyhodNejstarsi()

    for _ in range(n_deleted):
      self.append(Clovek(max_age))

  def zdvojVsechny(self):
    if (self.prvni is None):
      return

    clovek = self.prvni
    while (clovek is not None):
      majk_spirit = Clovek(clovek.vek, clovek.dalsi)
      clovek.dalsi = majk_spirit
      clovek = majk_spirit.dalsi

  def zdvojNejmladsi(self):
    if (self.prvni is None):
      return

    min_age = self.getMinAge()

    clovek = self.prvni
    while (clovek is not None):
      if (clovek.vek == min_age):
        majk_spirit = Clovek(clovek.vek, clovek.dalsi)
        clovek.dalsi = majk_spirit
        clovek = majk_spirit.dalsi
      else:
        clovek = clovek.dalsi

  def vyhodTriPosledni(self):
    length = self.length()

    if (length <= 3):
      self.prvni = None
    else:
      clovek = self.prvni
      for _ in range(length - 4):
        clovek = clovek.dalsi

      clovek.dalsi = None

  def licheSude(self):
    # Přerovná frontu tak, aby v ní nejprve stáli všichni lidi s lichým
    # věkem (se zachováním jejich původního vzájemného pořadí)
    # a následně všichni lidé se sudým věkem (opět se zachováním jejich
    # původního vzájemného pořadí)

    if (self.prvni is None):
      return

    n_even = 0
    clovek = self.prvni
    while (clovek is not None):
      if (clovek.vek % 2 == 0):
        n_even += 1

      clovek = clovek.dalsi

    if (n_even == 0):
      return

    n_swaps = 0

    while (self.prvni is not None and self.prvni.vek % 2 == 0 and n_swaps < n_even):
      temp = self.prvni
      self.prvni = self.prvni.dalsi
      self.append(temp)
      n_swaps += 1

      # print(self)

    clovek = self.prvni
    while(clovek is not None):
      while (n_swaps < n_even and clovek.dalsi is not None and clovek.dalsi.vek % 2 == 0):
        # print(clovek.dalsi.vek)
        temp = clovek.dalsi
        clovek.dalsi = clovek.dalsi.dalsi
        self.append(temp)
        n_swaps += 1

      clovek = clovek.dalsi

  def zrus(self):
    self.prvni = None


fronta = Fronta()
print(fronta)
fronta.vyhodNejstarsi()
print(fronta)
fronta.nejstarsiDozadu()
print(fronta)
fronta.vyhodTriPosledni()
print(fronta)
fronta.licheSude()
print(fronta)
fronta.zdvojNejmladsi()
print(fronta)
fronta.zdvojVsechny()
print(fronta)
fronta.zrus()
print(fronta)
fronta.vyhodNejstarsi()
print(fronta)
