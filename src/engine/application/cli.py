from engine.infrastructure.memory_indexer import MemoryIndexer
from engine.infrastructure.simple_query_engine import SimpleQueryEngine
from engine.infrastructure.simple_tokenizer import SimpleTokenizer
from engine.infrastructure.txt_loader import LoaderTxtImpl
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

    query_engine = SimpleQueryEngine(tokenizer, indexer.index)
    titles = {doc.id: doc.title for doc in documents}

    logger.info("=== Busca interativa (Enter vazio para sair) ===")

    while True:
        query = input("consulta > ").strip()
        if not query:
            break
        results = query_engine.search(query)
        if not results:
            logger.info("  Nenhum resultado encontrado.")
        else:
            for result in results:
                title = titles.get(result.document_id, "?")
                logger.info(
                    "  [%s] %-25s score=%d",
                    result.document_id,
                    title,
                    result.score,
                )
