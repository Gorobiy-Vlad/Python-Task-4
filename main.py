import Animal as a
import Kitchen_appliances as Kitchen
# 1. Создайте класс "животное".
# Наполните его данными и методами на свое усмотрение.
# Пропишите в методах класса докстринги с описанием метода
# Cats = a.Animal()
# Cats.PrintInfo()
# print("ReturnDictInfo -->", Cats.ReturnDictInfo())
# print("ReturnStrInfo -->", Cats.ReturnStrInfo())

# Ещё думаю над 2 и 3
# 2. Почитайте про Диаграммы класса.
# Опишите с помощью классов кухонную технику в виде диаграммы
# (пример https://www.intuit.ru/EDI/23_04_17_1/1492899714-28128/tutorial/356/objects/2/files/02_05.gif).
# Продумайте классы, их назначение и взаимосвязи. Реализовать с описанием свойств и методов.

# 3* Описать все то же с помощью питона.
kitchen = Kitchen.Kitchen_appliances("mmm", "nnn", "ccc")
fridg = Kitchen.Fridg('frg', 'mmm', 'ccc')
freezer = Kitchen.Freezer('frz', 'mmm', 'ccc')
Plate_g = Kitchen.Gas_Plate('ggg', "mmm", "ccc")
Plate_e = Kitchen.Electric_Plate('eee', 'mmm', 'ccc')

kitchen.print()
fridg.print()
freezer.print()
Plate_e.print()
Plate_g.print()