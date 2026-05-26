from engine.infrastructure.indexer.memory_indexer import MemoryIndexer
from engine.infrastructure.loader.txt_impl import LoaderTxtImpl
from engine.infrastructure.tokenizer.simple_tokenizer import SimpleTokenizer
from logger import get_logger, setup_logger

logger = get_logger(__name__)


def run(level: int) -> None:
    setup_logger(level)

    logger.info("=== Motor de Busca Experimental ===")

    loader = LoaderTxtImpl()
    tokenizer = SimpleTokenizer()
    indexer = MemoryIndexer()

    documents = loader.load()
    logger.info("Documentos carregados: %d", len(documents))

    total_tokens = 0
    for doc in documents:
        tokens = tokenizer.tokenize(doc.content)
        total_tokens += len(tokens)
        indexer.index_document(doc.id, tokens)
        logger.info("  [%s] %-25s → %d tokens", doc.id, doc.title, len(tokens))

    logger.info("Total de tokens no corpus: %d", total_tokens)
