import sys
import os

# Obtener la ruta del directorio padre
directorio_padre = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Añadir el directorio al sys.path
sys.path.append(directorio_padre)

from transcriber import Transcriber

transcriber = Transcriber()

for i in range(0,6):
    audio_file_path = f"tests/Test_0{i}.wav"  
    resultado = transcriber.audio_to_text(audio_file_path)
    print(f"Texto reconocido {i}:", resultado)
