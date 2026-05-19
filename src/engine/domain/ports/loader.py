from abc import ABC, abstractmethod

from engine.domain.models import Document


class Loader(ABC):
    @abstractmethod
    def load(self) -> list[Document]:
        pass
