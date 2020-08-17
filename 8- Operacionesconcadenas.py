s = "hola ahi! Que debe ser esta cadena?"

# longitud dede ser de 35
print("longitud de s = %d" % len(s))

# Primer Evento de "a" debera estar en el lugar 3
print("Primer evento de la letra a = %d" % s.index("a"))

# el numero de a's debera ser 5
print("a ocurre %d veces" % s.count("a"))

# start to 5
print("The first five characters are '%s'" % s[:5])
# 5 to 10
print("The next five characters are '%s'" % s[5:10])
# just numer 12
print("The thirteenth characters is '%s'" % s[12])

# 5th-from-last to end
print("The last five characters are '%s'" % s[-5:])

# Convert everithing to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everithing to lowercase
print("String in lowercase %s" % s.lower())

# Check how a string ends
if s.endswith("ena?"):
    print("String end with 'ena?'. Good!")

# Check how a string starts
if s.startswith("hola"):
    print("String starts with 'hola'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" ", 2))
