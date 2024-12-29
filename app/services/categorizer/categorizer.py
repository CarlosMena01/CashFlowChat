from langchain_ollama import OllamaLLM

""""
Este microservicio se encarga de clasificar gastos en categorías y subcategorías específicas utilizando un modelo de lenguaje natural. 
Funciones:
- `categorize_expense(entry)`: Toma una entrada que describe un gasto y devuelve un JSON estructurado con la descripción del gasto, el monto, la categoría principal, la subcategoría y una justificación de la clasificación.
El proceso de clasificación sigue estos pasos:
1. Entender el gasto: Extrae y corrige el monto y la descripción del gasto.
2. Categorizar el gasto: Clasifica el gasto en una categoría principal (Gasto básico, Lujos, Inversión).
3. Asignar una subcategoría: Propone una subcategoría específica dentro de la categoría principal.
4. Validar la clasificación: Analiza y justifica la categoría y subcategoría seleccionadas.
5. Resultado final: Devuelve un JSON con la descripción, monto, categoría, subcategoría y justificación del gasto.
"""


def categorize_expense(entry):
    model = OllamaLLM(model="llama3")

    prompt = f"""
    Eres un asistente inteligente especializado en la clasificación de gastos. Tu tarea es analizar una nota que describe un gasto y clasificarla en una categoría principal y una subcategoría adecuada, siguiendo estos pasos:  

    1. Entender el gasto:  
       - Extrae el monto y la descripción del gasto de la nota proporcionada, entendiendo que algunas palabras pueden estar mal escritas y deben corregirse.  
       - Asegúrate de que el monto esté expresado de forma numérica, convirtiéndolo si es necesario (por ejemplo, "7 mil" a "7000").  

    2. Categorizar el gasto:  
       Clasifica el gasto en una de las siguientes categorías principales:  
       - Gasto básico: Necesidades esenciales o recurrentes.  
       - Lujos: Gastos discrecionales que no son indispensables.  
       - Inversión: Gastos que generan valor a largo plazo o ahorros.  

    3. Asignar una subcategoría:  
       Propón una subcategoría específica para el gasto, basándote en las siguientes guías:  

       - Gasto básico:  
         - Alimentación  
         - Vivienda  
         - Transporte  
         - Salud  
         - Educación
         - Servicios públicos  

       - Lujos:  
         - Ocio  
         - Tecnología  
         - Moda  
         - Restaurantes  
         - Entretenimiento  

       - Inversión:  
         - Ahorro  
         - Activos financieros  
         - Educación a largo plazo  
         - Bienes duraderos  

    4. Validar la clasificación:  
       - Analiza si la descripción del gasto justifica la categoría y subcategoría seleccionadas.  
       - Proporciona una breve justificación de por qué encaja en dicha categoría y subcategoría.  

    5. Resultado final:  
       Devuelve un JSON estructurado con los siguientes campos:  
       - `"descripcion"`: Una descripción corta del gasto.  
       - `"monto"`: El monto del gasto como número.  
       - `"categoria"`: La categoría principal asignada.  
       - `"subcategoria"`: La subcategoría propuesta.  
       - `"justificacion"`: Una breve explicación de la clasificación.  

    Analiza esta entrada y devuelve el resultado en el formato solicitado, solo responde el JSON necesario, no escribas nada más: "{entry}"
    """

    result = model.invoke(input=prompt)
    return result

# if __name__ == "__main__":
#     entrada = "6k en cerveza"  # Ejemplo de entrada
#     resultado = categorize_expense(entrada)
#     print(resultado)