# Ejercicios-prueba

# 📘 CRUD en Python – Gestión de Estudiantes

Este proyecto es una implementación básica de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) usando diccionarios en Python para gestionar información de estudiantes.

## 📌 Objetivo

Evaluar habilidades de programación en Python mediante la resolución de un problema del mundo real: la gestión de registros estudiantiles. El sistema permite registrar, consultar, modificar y eliminar estudiantes.

---

## 🔧 Tecnologías y herramientas requeridas

- **Python 3.9+**
- Editor de código como **VS Code** o **PyCharm**
- Acceso a documentación oficial de Python
- (Opcional) Terminal o consola para ejecutar scripts

---

## 🧩 Operaciones CRUD

### 1. Create – Crear datos

```python
dict_students_[id_estudiante] = {
    "nombre": nombre_estudiante,
    "edad": edad_estudiante,
    "nota": nota_estudiante
}
🔐 La clave id_estudiante debe ser única.

2. Read – Leer o consultar datos
python
Copiar
Editar
if id in dict_students_:
    print(dict_students_[id])
📌 También puedes usar un bucle for para imprimir todos los estudiantes.

3. Update – Actualizar datos
python
Copiar
Editar
if id_estudiante in dict_students_:
    dict_students_[id_estudiante]["nombre"] = nuevo_nombre
    dict_students_[id_estudiante]["edad"] = nueva_edad
    dict_students_[id_estudiante]["nota"] = nueva_nota
🔄 Solo si el estudiante ya existe.

4. Delete – Eliminar datos
python
Copiar
Editar
if id_estudiante in dict_students_:
    del dict_students_[id_estudiante]
⚠️ Verifica que el ID exista antes de eliminar.

🧠 Extras útiles
pop() elimina y devuelve el valor eliminado.

Promedios:

python
Copiar
Editar
suma = 0
cantidad = 0
for est in dict_students_.values():
    suma += float(est["nota"])
    cantidad += 1
promedio = suma / cantidad
Validación de entrada: Usa try-except para evitar errores al convertir tipos.

🔧 Estructuras recomendadas
Funciones propias (ejemplo)
python
Copiar
Editar
def crear_estudiante(diccionario, id, nombre, edad, nota):
    diccionario[id] = {"nombre": nombre, "edad": edad, "nota": nota}
✅ Recomendado para código modular y mantenible.

🧪 Conceptos evaluados en una prueba
Variables y tipos (str, int, float, bool)

Operadores aritméticos y lógicos

Condicionales y bucles (if, for, while)

Funciones y funciones lambda

Diccionarios y listas

Manejo de errores con try-except

Buenas prácticas: nombres claros, modularidad, comentarios

✅ Consejos para rendir bien
Lee el problema con atención

Esquematiza las funcionalidades

Prioriza funciones simples al inicio

Maneja errores y entradas de usuario

Comenta tu código y mantenlo limpio

🚀 ¡Sé un Codernnn!
Este proyecto es tu base para luego avanzar a bases de datos reales como SQLite o PostgreSQL.
