class ModelInferenceError(Exception):
    """Exceção lançada quando ocorre um erro durante a inferência dos modelos de IA."""
    def __init__(self, message: str = "Erro durante o processamento do modelo de IA."):
        self.message = message
        super().__init__(self.message)