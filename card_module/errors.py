class DeckCheatingError(Exception):
    """
    class of custom error for cheating
    """
    def __init__(self, message: str):
        super().__init__(message)