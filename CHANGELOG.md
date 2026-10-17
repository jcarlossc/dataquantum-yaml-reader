# Changelog

Todas as alterações relevantes deste projeto serão documentadas neste arquivo.

Este projeto segue as convenções do [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e utiliza [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [0.1.0] - 2026-10-17

### Added
- Implementa a leitura de arquivos de configuração YAML.
- Adiciona a função `get_reader_yaml()` para carregar arquivos `.yaml` de um diretório.
- Retorna as configurações em um dicionário, utilizando o nome do arquivo como chave.
- Adiciona testes automatizados com `pytest`.
- Configura ferramentas de qualidade de código: Ruff, mypy, pytest-cov e pre-commit.
- Configura integração contínua com GitHub Actions.
- Configura automação de releases com Release Please.
- Adiciona documentação inicial do projeto.
