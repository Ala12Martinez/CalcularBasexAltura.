def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

base = float(input("Ingresa la medida de la base del rectángulo: "))
altura = float(input("Ingresa la medida de la altura del rectángulo: "))


area_rectangulo = calcular_area_rectangulo(base, altura)
print(f"El área del rectángulo con base {base} y altura {altura} es: {area_rectangulo}")
