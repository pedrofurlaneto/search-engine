import re

from engine.domain.ports.tokenizer import Tokenizer
from logger import get_logger


class SimpleTokenizer(Tokenizer):
    logger = get_logger(__name__)

    def tokenize(self, text: str) -> list[str]:
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        return text.split()
