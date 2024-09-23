class DVD:
    def __init__(self, id, name, description) -> None:
        self.id = id
        self.name = name
        self.description = description
    def __repr__(self) -> str:
        return f'DVD: id={self.id}, name={self.name}, description={self.description}'
    def __eq__(self, other) -> bool:
        return self.id == other.id and self.name == other.name and self.description == other.description    
    def __eq__(self, other) -> bool:
        return hash(self.id)