clientes = {
    "7654677": {
        "nombre": "Osvaldo",
        "apellidos": "Zelaya Lopez"
    }
}

def buscar_cliente(ci):
    if ci in clientes:
        return {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci,
            "nombre": clientes[ci]["nombre"],
            "apellidos": clientes[ci]["apellidos"]
        }
    else:
        return {
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }
