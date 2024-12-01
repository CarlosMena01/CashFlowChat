import speech_recognition as sr
from typing import Optional

class Transcriber:
    def __init__(self, language: str = 'es-ES', provider: str = 'google'):
        """
        Inicializa el transcriptor con configuraciones predeterminadas.
        
        :param language: Idioma para la transcripción (por defecto 'es-ES').
        :param provider: Proveedor de servicio de transcripción ('google' o futuro soporte).
        """
        self.language = language
        self.provider = provider
        self.recognizer = sr.Recognizer()
    
    def set_language(self, language: str):
        """
        Cambia el idioma predeterminado para la transcripción.
        
        :param language: Nuevo idioma a usar (ejemplo: 'en-US').
        """
        self.language = language
    
    def set_provider(self, provider: str):
        """
        Cambia el proveedor de servicio de reconocimiento de voz.
        
        :param provider: Proveedor a usar ('google', futuro soporte).
        """
        self.provider = provider

    def audio_to_text(self, audio_file_path: str) -> Optional[str]:
        """
        Convierte un archivo de audio a texto usando el proveedor configurado.
        
        :param audio_file_path: Ruta al archivo de audio.
        :return: Texto transcrito o mensaje de error.
        """
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio_data = self.recognizer.record(source)
            
            if self.provider == 'google':
                return self.recognizer.recognize_google(audio_data, language=self.language)
            else:
                raise NotImplementedError(f"El proveedor '{self.provider}' no está soportado.")
        
        except sr.UnknownValueError:
            return "No se pudo entender el audio."
        except sr.RequestError as e:
            return f"Error en el servicio de reconocimiento: {e}"
        except FileNotFoundError:
            return "El archivo de audio no existe."
        except Exception as e:
            return f"Se produjo un error inesperado: {e}"

    def transcribe_with_timeout(self, audio_file_path: str, timeout: int = 10) -> Optional[str]:
        """
        Transcribe audio con un límite de tiempo para la grabación.
        
        :param audio_file_path: Ruta al archivo de audio.
        :param timeout: Tiempo máximo para grabar el audio.
        :return: Texto transcrito o mensaje de error.
        """
        try:
            with sr.AudioFile(audio_file_path) as source:
                print(f"Cargando audio con timeout de {timeout} segundos...")
                audio_data = self.recognizer.record(source, duration=timeout)
            
            return self.recognizer.recognize_google(audio_data, language=self.language)
        
        except sr.UnknownValueError:
            return "No se pudo entender el audio en el tiempo establecido."
        except sr.RequestError as e:
            return f"Error en el servicio de reconocimiento: {e}"
        except FileNotFoundError:
            return "El archivo de audio no existe."
        except Exception as e:
            return f"Se produjo un error inesperado: {e}"

    def save_transcription(self, text: str, output_path: str):
        """
        Guarda la transcripción en un archivo de texto.
        
        :param text: Texto a guardar.
        :param output_path: Ruta del archivo de salida.
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(text)
            print(f"Transcripción guardada en {output_path}.")
        except Exception as e:
            print(f"No se pudo guardar la transcripción: {e}")

