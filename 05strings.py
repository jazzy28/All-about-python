name = "Tony Stark"
print(name.upper())#methods, will only change this string, not the original
print(name)
print(name.lower())

print(name.find('S'))
print(name.find('s')) #find - use either "" or '', index starts with 0 - counts space too, if it is not there then -1 is returned


print(name.replace("Tony Stark", "Ironman")) #will only replace this string, not the original
print(name)
print(name.replace("Stark", "Ironman"))


print('T' in name) #find a character/substring in a string
print('m' in name)
print('Stark' in name)
print('Ironman' in name)