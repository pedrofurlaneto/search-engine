import pytest

from engine.infrastructure.simple_tokenizer import SimpleTokenizer


@pytest.fixture
def tokenizer() -> SimpleTokenizer:
    return SimpleTokenizer()


class TestSimpleTokenizer:
    def test_lowercase(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("Hello World") == ["hello", "world"]

    def test_removes_punctuation(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("olá, mundo!") == ["olá", "mundo"]

    def test_multiple_spaces(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("hello    world") == ["hello", "world"]

    def test_preserves_portuguese_accents(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("programação") == ["programação"]

    def test_empty_string(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("") == []

    def test_only_punctuation(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("!!! ??? ...") == []

    def test_leading_trailing_whitespace(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("  hello world  ") == [
            "hello",
            "world",
        ]

    def test_numbers(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("python 3.12") == ["python", "3", "12"]

    def test_hyphen_removed(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("bem-vindo") == ["bem", "vindo"]

    def test_newline_as_separator(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("hello\nworld") == ["hello", "world"]

    def test_tab_as_separator(self, tokenizer: SimpleTokenizer):
        assert tokenizer.tokenize("hello\tworld") == ["hello", "world"]
