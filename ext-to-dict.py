
extensions = {}
with open("extensions.txt","r") as file:
	i = 0
	for line in file:
		
		print(i + 1, line)
		key = line.split(" ")[1]
		value = line.split(" ")[0]
		print(key)
		print(value + "\n\n\n")
		extensions[key] = value
		i += 1
print(extensions)
print(len(extensions))

file.close()