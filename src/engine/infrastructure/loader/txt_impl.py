from pathlib import Path

from engine.domain.models import Document
from engine.domain.ports.loader import Loader


class LoaderTxtImpl(Loader):
    def __init__(self, dataset_path: str = "dataset"):
        self.dataset_path = Path(dataset_path)

    def load(self) -> list[Document]:
        if not self.dataset_path.is_dir():
            msg = f"Diretório não encontrado: {self.dataset_path}"
            raise FileNotFoundError(msg)

        documents: list[Document] = []
        txt_files = sorted(self.dataset_path.glob("*.txt"))

        for filepath in txt_files:
            doc_id = filepath.stem.split("_", 1)[0]
            title = filepath.stem.split("_", 1)[1]
            content = filepath.read_text(encoding="utf-8").strip()
            documents.append(
                Document(
                    id=doc_id,
                    title=title,
                    content=content,
                    path=str(filepath),
                )
            )

        return documents
