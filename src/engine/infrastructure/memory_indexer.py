from engine.domain.ports.indexer import Indexer
from logger import get_logger


class MemoryIndexer(Indexer):
    logger = get_logger(__name__)

    def __init__(self) -> None:
        self._index: dict[str, dict[str, int]] = {}

    @property
    def index(self) -> dict[str, dict[str, int]]:
        return self._index

    def index_document(self, doc_id: str, tokens: list[str]) -> None:
        for token in tokens:
            if token not in self._index:
                self._index[token] = {}
            self._index[token][doc_id] = self._index[token].get(doc_id, 0) + 1

        self.logger.debug(
            "Indexed document %s: %d tokens (%d unique)",
            doc_id,
            len(tokens),
            len(set(tokens)),
        )
