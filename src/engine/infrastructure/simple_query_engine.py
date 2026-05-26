from collections import defaultdict

from engine.domain.models import SearchResult
from engine.domain.ports.query_engine import QueryEngine
from engine.domain.ports.tokenizer import Tokenizer


class SimpleQueryEngine(QueryEngine):
    def __init__(self, tokenizer: Tokenizer, index: dict[str, dict[str, int]]) -> None:
        self._index = index
        self._tokenizer = tokenizer

    def search(self, query: str) -> list[SearchResult]:
        tokens = self._tokenizer.tokenize(query)
        scores = defaultdict(int)

        for token in tokens:
            postings = self._index.get(token, {})

            for document_id, frequency in postings.items():
                scores[document_id] += frequency

        ranked_results = sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [
            SearchResult(document_id=document_id, score=score)
            for document_id, score in ranked_results
        ]
