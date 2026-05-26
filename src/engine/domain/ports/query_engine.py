from abc import ABC, abstractmethod

from engine.domain.models import SearchResult


class QueryEngine(ABC):
    @abstractmethod
    def search(self, query: str) -> list[SearchResult]:
        pass
