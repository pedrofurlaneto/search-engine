from dataclasses import dataclass


@dataclass
class Document:
    id: str
    title: str
    content: str
    path: str

@dataclass
class SearchResult:
    document_id: str
    score: int
