immutable_var = tuple([1,"6",True])
print(immutable_var)
#immutable_var[1] = "6" кортеж не поддерживает обращение по элементам
mutable_list = [1,"5",False]
mutable_list[1] = "6"
print(mutable_list)