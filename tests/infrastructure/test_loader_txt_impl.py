from pathlib import Path

import pytest

from engine.domain.models import Document
from engine.infrastructure.txt_loader import LoaderTxtImpl


def test_load_single_file(tmp_path: Path):
    filepath = tmp_path / "01_foo.txt"
    filepath.write_text("hello world", encoding="utf-8")
    sut = LoaderTxtImpl(str(tmp_path))
    docs = sut.load()
    assert len(docs) == 1
    assert docs[0] == Document(
        id="01", title="foo", content="hello world", path=str(filepath)
    )


def test_load_parses_id_and_title(tmp_path: Path):
    (tmp_path / "42_foo_bar_baz.txt").write_text("content", encoding="utf-8")
    sut = LoaderTxtImpl(str(tmp_path))
    docs = sut.load()
    assert docs[0].id == "42"
    assert docs[0].title == "foo_bar_baz"


def test_load_strips_content(tmp_path: Path):
    (tmp_path / "01_test.txt").write_text("  line1\n  line2\n\n\n", encoding="utf-8")
    sut = LoaderTxtImpl(str(tmp_path))
    docs = sut.load()
    assert docs[0].content == "line1\n  line2"


def test_load_multiple_files_sorted(tmp_path: Path):
    for name in ["03_c.txt", "01_a.txt", "02_b.txt"]:
        (tmp_path / name).write_text(name, encoding="utf-8")
    sut = LoaderTxtImpl(str(tmp_path))
    docs = sut.load()
    assert [d.title for d in docs] == ["a", "b", "c"]


def test_load_empty_directory(tmp_path: Path):
    sut = LoaderTxtImpl(str(tmp_path))
    assert sut.load() == []


def test_load_ignores_non_txt(tmp_path: Path):
    (tmp_path / "01_foo.txt").write_text("txt", encoding="utf-8")
    (tmp_path / "bar.md").write_text("md", encoding="utf-8")
    (tmp_path / "baz.py").write_text("py", encoding="utf-8")
    sut = LoaderTxtImpl(str(tmp_path))
    assert len(sut.load()) == 1


def test_load_utf8_content(tmp_path: Path):
    content = "Python é uma linguagem de programação"
    (tmp_path / "01_test.txt").write_text(content, encoding="utf-8")
    sut = LoaderTxtImpl(str(tmp_path))
    assert sut.load()[0].content == content


def test_load_file_not_found():
    sut = LoaderTxtImpl("/caminho/inexistente")
    with pytest.raises(FileNotFoundError):
        sut.load()
