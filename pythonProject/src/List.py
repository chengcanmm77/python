list = ["aa","bb","cc","dd"]
print(list)

# 列表查询
#list.sort(reverse=True)

print(sorted(list,reverse=True))
# 列表插入
#list.index("00",0);
print(list)

print(len(list))


for tt in list:
    print(tt)

sqa = [value**2 for value in range(1, 11)]
print(sqa)

for value in sqa:
    if value == 9:
        print("tt")
    elif value == 9 and value == 8:
        print("1231")
    else:
        print(value)

print(100 in sqa)
print(20 in sqa)
print(str(1212)+"--1212")
print(int("2")+4)

map_value = {"name": "bucket", "age": "22"}
print(map_value["name"])

map_value['x'] = 3
map_value['y'] = 0

print(map_value)

for key, value in map_value.items():
    print("key=" + str(key)+" value=" + str(value))

for key in map_value.keys():
    print(key)
    print(map_value[key])

del map_value['x']
print(map_value)