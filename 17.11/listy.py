#Uzupełnij brakujące elementy - wypełnij ____ w poniższym kodzie
#Przydatne: .append(), .remove()

my_list=[]
my_list.append("Python")
my_list.append("is ok")
my_list.append("sometimes")
my_list.remove("sometimes")
my_list[1]="is neat"
assert my_list == ["Python", "is neat"]

#Utwórz nową listę bez modyfikowania oryginalnej
original = ["I", "am", "learning", "hacking", "in"]
modified=original[:]
modified.append("Python")
modified[3]="lists"

assert original == ["I", "am", "learning", "hacking", "in"]
assert modified == ["I", "am", "learning", "lists", "in", "Python"]

#Utwórz połączoną posortowaną listę
#Przydatne: sorted()
list1 = [6, 12, 5]
list2 = [6.2, 0, 14, 1]
list3 = [0.9]
# Twoja implementacja
my_list = list1.copy()
my_list.extend(list2)
my_list.extend(list3)
my_list.sort()
my_list.reverse()

# Sprawdźmy czy otrzymaliśmy poprawny wynik
assert my_list == [14, 12, 6.2, 6, 5, 1, 0.9, 0]
