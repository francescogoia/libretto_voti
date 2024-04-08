import datetime
from dataclasses import dataclass

@dataclass
class VotoDto:
    nome: str
    CFU: int
    punteggio: int
    lode: bool
    data: datetime.date


    def __str__(self):
        return f"{self.nome}-{self.CFU}-{self.punteggio}-{self.lode}-{self.data}"

    def __eq__(self, other):
        return self.nome == other.nome

    def __hash__(self):
        return hash(self.nome)
