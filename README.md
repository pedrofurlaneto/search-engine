# search-engine

Um motor de busca experimental feito em Python. Nasceu como um brinquedo para estudar **spec-driven development** na prática: escrever especificações (interfaces, contratos, comportamento esperado) e usar IA para gerar as implementações a partir delas, num ciclo de refino contínuo.

A ideia aqui é ter um código enxuto onde dá pra enxergar padrões de arquitetura limpa, separação por camadas e facilidade de manutenção.

## O que o projeto faz

1. Carrega documentos de texto (`dataset/*.txt`)
2. Tokeniza o conteúdo (lowercase, remove pontuação)
3. Constrói um índice invertido em memória (termo → documento → frequência)
4. Permite buscar por termos via REPL interativo ranqueando por TF

```
$ uv run python -m engine
consulta > python
  [01] python_basics               score=2
```

## Como rodar

```bash
# instalar dependências
uv sync

# testes
uv run pytest -v

# lint
uv run ruff check src/ tests/

# pipeline completo + busca interativa
uv run python -m engine
```

No REPL, digite uma consulta e veja os documentos ranqueados. Enter vazio sai.