import whisper

class Transcriber:
    def __init__(self, model_size: str = "base"):
        """
        Inicializa el modelo Whisper local.
        
        Parámetros:
        - model_size (str): Puede ser "tiny", "base", "small", "medium", o "large".
        """
        print(f"Cargando modelo Whisper '{model_size}' localmente...")
        self.model = whisper.load_model(model_size).to("cuda")
        print("Modelo cargado correctamente.")

    def audio_to_text(self, file_path: str, language: str = None) -> str:
        """
        Transcribe un archivo de audio a texto.
        
        Parámetros:
        - file_path (str): Ruta al archivo de audio.
        - language (str, opcional): Código de idioma ISO 639-1 (por ejemplo, 'es' para español).
        
        Retorna:
        - str: Texto transcrito.
        """
        try:
            print(f"Transcribiendo archivo: {file_path}")
            result = self.model.transcribe(file_path, language=language)
            return result["text"]
        except Exception as e:
            raise RuntimeError(f"Error en la transcripción: {e}")
