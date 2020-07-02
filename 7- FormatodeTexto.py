Datos = ["Juan", "Perez", 53.44]
format_string = "hola"
print(format_string, Datos[0], Datos[1], ". Tu balance es de:", Datos[2], "$")


Datos = ("Juan", "Perez", 53.44)
format_string = "hola %s %s. tu balance es de: %.2f$"
print(format_string % Datos)
