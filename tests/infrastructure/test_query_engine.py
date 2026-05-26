import pytest

from engine.domain.models import SearchResult
from engine.infrastructure.simple_query_engine import SimpleQueryEngine
from engine.infrastructure.simple_tokenizer import SimpleTokenizer


@pytest.fixture
def engine() -> SimpleQueryEngine:
    index = {
        "python": {"01": 2, "02": 1},
        "linguagem": {"01": 1},
        "programacao": {"02": 3},
        "dados": {"03": 1},
    }
    return SimpleQueryEngine(SimpleTokenizer(), index)


class TestSimpleQueryEngine:
    def test_single_term_one_document(self, engine: SimpleQueryEngine):
        results = engine.search("linguagem")
        assert results == [SearchResult("01", 1)]

    def test_single_term_multiple_documents(self, engine: SimpleQueryEngine):
        results = engine.search("python")
        assert results == [SearchResult("01", 2), SearchResult("02", 1)]

    def test_multi_term_scores_sum(self, engine: SimpleQueryEngine):
        results = engine.search("python programacao")
        assert len(results) == 2
        assert SearchResult("02", 4) in results
        assert SearchResult("01", 2) in results

    def test_ranking_order(self, engine: SimpleQueryEngine):
        results = engine.search("python programacao")
        assert results[0].score >= results[1].score

    def test_no_match(self, engine: SimpleQueryEngine):
        assert engine.search("inexistente") == []

    def test_no_match_partial(self, engine: SimpleQueryEngine):
        assert engine.search("py") == []

    def test_empty_query(self, engine: SimpleQueryEngine):
        assert engine.search("") == []

    def test_case_insensitive(self, engine: SimpleQueryEngine):
        results = engine.search("Python")
        assert results == [SearchResult("01", 2), SearchResult("02", 1)]

    def test_punctuation_ignored(self, engine: SimpleQueryEngine):
        results = engine.search("python!")
        assert results == [SearchResult("01", 2), SearchResult("02", 1)]
