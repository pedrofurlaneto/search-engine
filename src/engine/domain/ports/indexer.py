from abc import ABC, abstractmethod


class Indexer(ABC):
    @abstractmethod
    def index_document(self, doc_id: str, tokens: list[str]) -> None: ...
