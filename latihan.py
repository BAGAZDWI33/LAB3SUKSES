#akses list
list = ["Alice", "Ruby", "Json","Mac","Linus"]
print(list[2])
print(list[2:4])
print(list[-1])

#mengubah elemen list
list[3] = "pert"
print(list)
list[3:5] = ["Berg","Sret"]
print(list)

#menambahkan elemen list
list2 = list[0:2]
print(list2)
list2.append("siti")
print(list2)
list2.append("babeh")
print(list2)
list3 = list + list2
print(list3)