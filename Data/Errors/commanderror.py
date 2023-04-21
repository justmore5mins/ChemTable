class CommandsError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class WTFError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)