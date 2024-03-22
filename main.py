import clases

coordinador1 = clases.Coordinador("Juan", "Perez", 2221121, 300000, 45000)
print(f"""Coordinador
{coordinador1.nombre} {coordinador1.apellido}
""")

empleado_mostrador = clases.Empleado_mostrador("Ana", "Ortiz", 53535353, 300000, 5000)
print(f"""Empleado de mostrador
{empleado_mostrador.nombre} {empleado_mostrador.apellido}
""")
print(f" la caja es: ${empleado_mostrador.caja}")