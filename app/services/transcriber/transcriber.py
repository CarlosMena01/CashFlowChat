import speech_recognition as sr

def audio_to_text(audio_file_path):
    # Crear un objeto Recognizer
    recognizer = sr.Recognizer()

    try:
        # Cargar el archivo de audio
        with sr.AudioFile(audio_file_path) as source:
            print("Cargando el audio...")
            audio_data = recognizer.record(source)  # Leer el audio
        
        # Reconocer el texto del audio
        print("Reconociendo...")
        text = recognizer.recognize_google(audio_data, language='es-ES')  # Cambiar el idioma si es necesario
        return text
    
    except sr.UnknownValueError:
        return "No se pudo entender el audio."
    except sr.RequestError as e:
        return f"Error en el servicio de reconocimiento: {e}"

# Ruta al archivo de audio
audio_file_path = "tests/Test_06.wav"  
resultado = audio_to_text(audio_file_path)
print("Texto reconocido:", resultado)
