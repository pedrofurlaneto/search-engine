import pytest

from engine.infrastructure.indexer.memory_indexer import MemoryIndexer


@pytest.fixture
def indexer() -> MemoryIndexer:
    return MemoryIndexer()


class TestMemoryIndexer:
    def test_index_single_document(self, indexer: MemoryIndexer):
        indexer.index_document("01", ["python", "linguagem", "python"])
        assert indexer._index["python"] == {"01": 2}
        assert indexer._index["linguagem"] == {"01": 1}

    def test_index_multiple_documents(self, indexer: MemoryIndexer):
        indexer.index_document("01", ["python", "linguagem"])
        indexer.index_document("02", ["python", "programacao"])
        assert indexer._index["python"] == {"01": 1, "02": 1}
        assert indexer._index["linguagem"] == {"01": 1}
        assert indexer._index["programacao"] == {"02": 1}

    def test_index_empty_tokens(self, indexer: MemoryIndexer):
        indexer.index_document("01", [])
        assert indexer._index == {}

    def test_index_repeated_word_in_document(self, indexer: MemoryIndexer):
        indexer.index_document("01", ["python", "python", "python"])
        assert indexer._index["python"] == {"01": 3}

    def test_index_same_word_in_different_docs(self, indexer: MemoryIndexer):
        indexer.index_document("01", ["python"])
        indexer.index_document("02", ["python"])
        assert indexer._index["python"] == {"01": 1, "02": 1}
