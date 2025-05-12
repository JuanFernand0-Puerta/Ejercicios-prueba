from rich.console import Console
from rich.table import Table

usuarios = {
    "1": {
        "nombre": "Daniel",
        "apellido": "Herrera",
        "contacto": {
            "correo": "garyford@gmail.com",
            "telefono": "001-512-801-0651x67779",
            "direccion": {
                "calle": "178 Walker Island Suite 840",
                "ciudad": "Gonzalezmouth",
                "estado": "Michigan",
                "codigo_postal": "92488",
                "pais": "Bermuda"
            }
        },
        "perfil": {
            "username": "bradley18",
            "fecha_nacimiento": "1987-07-15",
            "genero": "Masculino",
            "ocupacion": "Financial planner"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/mistytaylor",
            "linkedin": "https://linkedin.com/in/nancythomas",
            "instagram": ""
        },
        "preferencias": {
            "idioma": "Francés",
            "newsletter": True,
            "temas_interes": ["arte", "moda", "tecnología"]
        }
    },
    "2": {
        "nombre": "Joseph",
        "apellido": "Sullivan",
        "contacto": {
            "correo": "grussell@hotmail.com",
            "telefono": "006-305-4158x3659",
            "direccion": {
                "calle": "9638 Hawkins Crossing Apt. 914",
                "ciudad": "Robertchester",
                "estado": "Illinois",
                "codigo_postal": "28682",
                "pais": "Ethiopia"
            }
        },
        "perfil": {
            "username": "kennethtaylor",
            "fecha_nacimiento": "1981-03-26",
            "genero": "Otro",
            "ocupacion": "Clinical psychologist"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/claire15",
            "linkedin": "",
            "instagram": "https://instagram.com/kellycooper"
        },
        "preferencias": {
            "idioma": "Francés",
            "newsletter": False,
            "temas_interes": ["deportes", "arte", "viajes"]
        }
    },
    "3": {
        "nombre": "Kristina",
        "apellido": "Bradley",
        "contacto": {
            "correo": "mark58@hotmail.com",
            "telefono": "771-464-1767",
            "direccion": {
                "calle": "9396 Martin Bridge Apt. 544",
                "ciudad": "South Ryan",
                "estado": "Iowa",
                "codigo_postal": "41958",
                "pais": "Philippines"
            }
        },
        "perfil": {
            "username": "christine51",
            "fecha_nacimiento": "1966-09-21",
            "genero": "Femenino",
            "ocupacion": "Restaurant manager, fast food"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/dickersonjustin",
            "linkedin": "https://linkedin.com/in/michaela78",
            "instagram": ""
        },
        "preferencias": {
            "idioma": "Español",
            "newsletter": True,
            "temas_interes": ["cocina", "tecnología", "viajes"]
        }
    },
    "4": {
        "nombre": "Monica",
        "apellido": "Molina",
        "contacto": {
            "correo": "daniel59@yahoo.com",
            "telefono": "(925)185-9544x03157",
            "direccion": {
                "calle": "53484 Garrett Wall",
                "ciudad": "East Sherri",
                "estado": "Washington",
                "codigo_postal": "81748",
                "pais": "Syrian Arab Republic"
            }
        },
        "perfil": {
            "username": "kayla97",
            "fecha_nacimiento": "1987-11-19",
            "genero": "Femenino",
            "ocupacion": "Company secretary"
        },
        "redes_sociales": {
            "twitter": "https://twitter.com/rgomez",
            "linkedin": "",
            "instagram": "https://instagram.com/sarah44"
        },
        "preferencias": {
            "idioma": "Español",
            "newsletter": True,
            "temas_interes": ["viajes", "deportes", "tecnología"]
        }
    },
    "5": {
        "nombre": "Angela",
        "apellido": "House",
        "contacto": {
            "correo": "pwaters@dixon.biz",
            "telefono": "(616)639-1141",
            "direccion": {
                "calle": "8264 Morgan Lights",
                "ciudad": "Dianetown",
                "estado": "North Dakota",
                "codigo_postal": "64546",
                "pais": "Bolivia"
            }
        },
        "perfil": {
            "username": "randy13",
            "fecha_nacimiento": "2006-02-20",
            "genero": "Masculino",
            "ocupacion": "Airline pilot"
        },
        "redes_sociales": {
            "twitter": "",
            "linkedin": "https://linkedin.com/in/watkinsjessica",
            "instagram": "https://instagram.com/longlaura"
        },
        "preferencias": {
            "idioma": "Inglés",
            "newsletter": False,
            "temas_interes": ["moda", "arte", "cocina"]
        }
    }
}


console = Console()

# Crear la tabla con color en los títulos
table = Table(title="Usuarios Registrados", title_style="bold magenta", show_lines=True)

# Agregar columnas con estilo
table.add_column("ID", style="cyan", justify="center")
table.add_column("Nombre", style="green")
table.add_column("Apellido", style="green")
table.add_column("Correo", style="yellow")
table.add_column("Teléfono", style="yellow")
table.add_column("Ciudad", style="blue")
table.add_column("Ocupación", style="magenta")
table.add_column("Idioma", style="bright_cyan")
table.add_column("Temas de Interés", style="bright_white")



for key, usuario in usuarios.items():

    table.add_row(
        key,
        usuario["nombre"],
        usuario["apellido"],
        usuario["contacto"]["correo"],
        usuario["contacto"]["telefono"],
        usuario["contacto"]["direccion"]["ciudad"],
        usuario["perfil"]["ocupacion"],
        usuario["preferencias"]["idioma"],
        ", ".join(usuario["preferencias"]["temas_interes"])
    )

    
    
    '''
for uid, usuario in usuarios.items():
    table.add_row(
        uid,
        usuario["nombre"],
        usuario["apellido"],
        usuario["contacto"]["correo"],
        usuario["contacto"]["telefono"],
        usuario["contacto"]["direccion"]["ciudad"],
        usuario["perfil"]["ocupacion"],
        usuario["preferencias"]["idioma"],
        ", ".join(usuario["preferencias"]["temas_interes"])
    )

    '''

# Mostrar la tabla
console.print(table)
