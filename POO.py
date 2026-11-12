import yaml
from pathlib import Path

class Pregunta:
    def __init__(self, title, prompt, hints, tags):
        self.title = title
        self.prompt = prompt
        self.hints = hints
        self.tags = tags
        
    def to_dict(self):
        return {
            "title": self.title,
            "prompt": self.prompt,
            "hints": self.hints,
            "tags": self.tags
        }

# --- 10 Retos de Python ---

reto_1 = Pregunta(
    title="Suma dos números",
    prompt="Escribe una función `suma(a, b)` que devuelva a + b.",
    hints=["Usa el operador '+'", "Devuelve el resultado con 'return'"],
    tags=["funciones", "aritmética", "principiante"]
)

reto_2 = Pregunta(
    title="Es Palíndromo",
    prompt="Escribe una función `es_palindromo(texto)` que retorne True si la cadena es un palíndromo.",
    hints=["Puedes invertir la cadena usando slicing `texto[::-1]`", "Recuerda limpiar espacios y poner todo en minúsculas"],
    tags=["cadenas", "lógica"]
)

reto_3 = Pregunta(
    title="Factorial de un número",
    prompt="Crea una función `factorial(n)` que calcule el factorial de un número entero positivo.",
    hints=["Puedes usar recursividad o un bucle `for`", "El factorial de 0 es 1"],
    tags=["matemáticas", "bucles", "recursividad"]
)

reto_4 = Pregunta(
    title="FizzBuzz",
    prompt="Escribe un programa que retorne 'Fizz' si es divisible por 3, 'Buzz' por 5, y 'FizzBuzz' por ambos.",
    hints=["Usa el operador módulo `%`", "El orden de las condiciones if/elif importa mucho"],
    tags=["condicionales", "entrevista"]
)

reto_5 = Pregunta(
    title="Contador de vocales",
    prompt="Crea una función `contar_vocales(texto)` que devuelva la cantidad de vocales en una frase.",
    hints=["Itera sobre cada letra de la cadena", "Comprueba si la letra está en la lista ['a', 'e', 'i', 'o', 'u']"],
    tags=["cadenas", "bucles"]
)

reto_6 = Pregunta(
    title="Invertir una lista",
    prompt="Escribe una función `invertir_lista(lista)` que reciba una lista y la devuelva al revés sin usar `reverse()`.",
    hints=["Puedes crear una nueva lista y agregar elementos desde el final", "El slicing `lista[::-1]` también es válido"],
    tags=["listas", "slicing"]
)

reto_7 = Pregunta(
    title="Número Máximo",
    prompt="Crea una función `maximo(lista)` que encuentre el número más grande en una lista sin usar `max()`.",
    hints=["Inicializa una variable con el primer elemento", "Recorre la lista y actualiza la variable si encuentras un número mayor"],
    tags=["listas", "lógica"]
)

reto_8 = Pregunta(
    title="Filtrar números pares",
    prompt="Escribe una función `solo_pares(lista)` que devuelva una nueva lista solo con los números pares.",
    hints=["Usa un bucle `for` o una lista por comprensión", "Verifica la paridad con `numero % 2 == 0`"],
    tags=["listas", "matemáticas"]
)

reto_9 = Pregunta(
    title="Diccionario de cuadrados",
    prompt="Crea una función `diccionario_cuadrados(n)` que retorne un diccionario con claves del 1 al n y valores sus cuadrados.",
    hints=["Usa un bucle que vaya desde 1 hasta n+1", "Asigna `diccionario[i] = i**2`"],
    tags=["diccionarios", "bucles"]
)

reto_10 = Pregunta(
    title="Contar palabras",
    prompt="Escribe una función `contar_palabras(texto)` que devuelva la cantidad de palabras en una cadena.",
    hints=["El método `.split()` te será muy útil", "Devuelve la longitud de la lista resultante con `len()`"],
    tags=["cadenas", "métodos"]
)

def cargar_preguntas():
    # Definir la ruta relativa al archivo problems.yaml
    ruta_yaml = Path(__file__).parent / "problems.yaml"
    
    # Leer las preguntas actuales
    datos_actuales = []
    if ruta_yaml.exists():
        with ruta_yaml.open("r", encoding="utf-8") as f:
            datos_actuales = yaml.safe_load(f) or []
            
    # Crear una lista con los 10 objetos convertidos a diccionarios
    nuevas_preguntas = [
        reto_1.to_dict(),
        reto_2.to_dict(),
        reto_3.to_dict(),
        reto_4.to_dict(),
        reto_5.to_dict(),
        reto_6.to_dict(),
        reto_7.to_dict(),
        reto_8.to_dict(),
        reto_9.to_dict(),
        reto_10.to_dict()
    ]
    
    # Unir los datos
    datos_actualizados = datos_actuales + nuevas_preguntas
    
    # Sobreescribir el archivo YAML
    with ruta_yaml.open("w", encoding="utf-8") as f:
        yaml.dump(
            datos_actualizados, 
            f, 
            allow_unicode=True, 
            default_flow_style=False, 
            sort_keys=False
        )
        
    print("¡Las 10 preguntas se han agregado correctamente a problems.yaml!")

# Bloque de ejecución principal para probar el archivo
if __name__ == '__main__':
    cargar_preguntas()
