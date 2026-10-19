<<<<<<< HEAD
# DataQuantum YAML Reader

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Biblioteca Python para leitura de arquivos de configuração YAML, desenvolvida para simplificar o carregamento e a organização de configurações em projetos Python.

O `DataQuantum YAML Reader` permite ler múltiplos arquivos `.yaml` de um diretório e reunir suas configurações em um dicionário Python, utilizando o nome de cada arquivo como chave.

Desenvolvido pela **DataQuantum**, marca dedicada a soluções de análise de dados, ciência de dados e engenharia de dados.

## Funcionalidades

- Leitura de múltiplos arquivos `.yaml` de um diretório.
- Carregamento seguro dos arquivos utilizando `yaml.safe_load`.
- Organização das configurações em um dicionário Python.
- Utilização do nome de cada arquivo como chave do dicionário.
- Suporte a estruturas YAML aninhadas.
- Integração com projetos Python e pipelines ETL.

## Requisitos

- Python 3.11 ou superior.
- PyYAML 6.0.3 ou superior, dentro do intervalo de versões declarado pelo pacote.

## Instalação

### Com pip

Instale a biblioteca diretamente do PyPI:

```bash
pip install dataquantum-yaml-reader
```

### Com Poetry

Adicione a biblioteca como dependência do projeto:

```bash
poetry add dataquantum-yaml-reader
```

### Estrutura de diretórios

Crie o diretório `config` na raiz do projeto para armazenar os arquivos de configuração com extensão `.yaml`.

## Exemplo de utilização

Considere a seguinte estrutura de diretórios:

```text
projeto/
├── config/
│   └── logging.yaml
├── src/
│   └── main.py
└── pyproject.toml
```

O arquivo `logging.yaml` contém:

```yaml
logging_info:
  level: "INFO"
  format: "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
  encoding: "utf-8"

logs:
  file: "logs/app.log"
```

### Lendo os arquivos YAML

Importe a função `get_reader_yaml` e informe o caminho do diretório que contém os arquivos de configuração.

```python
from pathlib import Path

from dataquantum_yaml_reader import get_reader_yaml


# Localiza a raiz do projeto, um nível acima de src/.
project_root = Path(__file__).resolve().parent.parent

# Define o caminho absoluto para o diretório de configurações.
config_path = project_root / "config"

configs = get_reader_yaml(config_path)

print(configs)
```
### Como funciona?
- ```__file__```: caminho do arquivo main.py.
- ```.resolve()```: transforma o caminho em absoluto.
- ```.parent```: retorna o diretório src/.
- ```.parent.parent```: retorna a raiz do projeto.
- ```/ "config"```: acrescenta o diretório config/ ao caminho.

### Resultado esperado

```python
{
    "logging": {
        "logging_info": {
            "level": "INFO",
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            "encoding": "utf-8"
        },
        "logs": {
            "file": "logs/app.log"
        }
    }
}
```

O dicionário contém uma entrada para cada arquivo `.yaml` encontrado. A chave corresponde ao nome do arquivo sem a extensão, e o valor corresponde ao conteúdo carregado.

## Utilizando as configurações

Após carregar os arquivos, você pode acessar os valores por meio das chaves do dicionário.

```python
from pathlib import Path

from dataquantum_yaml_reader import get_reader_yaml

# Localiza a raiz do projeto, um nível acima de src/.
project_root = Path(__file__).resolve().parent.parent

# Define o caminho absoluto para o diretório de configurações.
config_path = project_root / "config"

configs = get_reader_yaml(config_path)

logging_config = configs["logging"]

level = logging_config["logging_info"]["level"]
log_format = logging_config["logging_info"]["format"]
encoding = logging_config["logging_info"]["encoding"]
log_file = logging_config["logs"]["file"]

print(level)
print(log_format)
print(encoding)
print(log_file)
```

Saída:

```text
INFO
%(asctime)s - %(levelname)s - %(name)s - %(message)s
utf-8
logs/app.log
```

## Quais erros podem ocorrer?

| Exceção | Situação |
|---|---|
| `FileNotFoundError` | O caminho informado não existe. |
| `NotADirectoryError` | O caminho existe, mas aponta para um arquivo, não para um diretório. |
| `ValueError` | Um arquivo YAML contém sintaxe inválida. |
| `OSError` | Ocorre um erro do sistema operacional ao acessar ou ler arquivos. |

**Arquivos YAML vazios:** não geram erro com `yaml.safe_load()`.
O valor correspondente no dicionário será `None`.

## Aplicações

A biblioteca pode ser utilizada em diferentes contextos:

- **Análise de dados:** centralização de configurações de projetos analíticos.
- **Ciência de dados:** carregamento de parâmetros e configurações de experimentos.
- **Engenharia de dados:** gerenciamento de configurações de pipelines ETL.
- **Automação:** leitura de configurações utilizadas em scripts Python.
- **Integração de sistemas:** organização de parâmetros de conexão e configurações de aplicações.

## Desenvolvimento

Este projeto utiliza Poetry para gerenciamento de dependências e do ambiente de desenvolvimento.

Clone o repositório:

```bash
git clone https://github.com/jcarlossc/dataquantum-yaml-reader.git

cd dataquantum-yaml-reader
```

Instale as dependências:

```bash
poetry install
```

Execute os testes:

```bash
poetry run task pytest
```

Execute os testes com relatório de cobertura:

```bash
poetry run task covcmd
```

Execute as verificações de qualidade:

```bash
poetry run task check
poetry run task lint
poetry run task mypy
```

Execute a validação completa para o release:

```bash
poetry run task release-check
```

## Testes e qualidade

O projeto utiliza ferramentas para garantir a qualidade, a manutenção e a confiabilidade do código:

- **pytest:** execução dos testes automatizados.
- **pytest-cov:** medição da cobertura dos testes.
- **Ruff:** análise estática e formatação do código.
- **mypy:** verificação estática de tipos.
- **pre-commit:** execução de verificações automatizadas antes dos commits.
- **GitHub Actions:** integração contínua e automação de tarefas.
- **Release Please:** gerenciamento automatizado de releases e changelog.

## Versionamento

O projeto segue o Versionamento Semântico (*Semantic Versioning*), utilizando o formato:

`MAJOR.MINOR.PATCH`

- **MAJOR:** alterações incompatíveis com versões anteriores.
- **MINOR:** novas funcionalidades compatíveis com versões anteriores.
- **PATCH:** correções compatíveis com a versão existente.

Consulte o arquivo `CHANGELOG.md` para acompanhar o histórico de alterações.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

## Autor e contato

**DataQuantum**

- GitHub: [jcarlossc](https://github.com/jcarlossc)
- Repositório: [dataquantum-yaml-reader](https://github.com/jcarlossc/dataquantum-yaml-reader)
- E-mail: jcarlossc1977@gmail.com

=======
# DataQuantum YAML Reader

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Biblioteca Python para leitura de arquivos de configuração YAML, desenvolvida para simplificar o carregamento e a organização de configurações em projetos Python.

O `DataQuantum YAML Reader` permite ler múltiplos arquivos `.yaml` de um diretório e reunir suas configurações em um dicionário Python, utilizando o nome de cada arquivo como chave.

Desenvolvido pela **DataQuantum**, marca dedicada a soluções de análise de dados, ciência de dados e engenharia de dados.

## Funcionalidades

- Leitura de múltiplos arquivos `.yaml` de um diretório.
- Carregamento seguro dos arquivos utilizando `yaml.safe_load`.
- Organização das configurações em um dicionário Python.
- Utilização do nome de cada arquivo como chave do dicionário.
- Suporte a estruturas YAML aninhadas.
- Integração com projetos Python e pipelines ETL.

## Requisitos

- Python 3.11 ou superior.
- PyYAML 6.0.3 ou superior, dentro do intervalo de versões declarado pelo pacote.

## Instalação

### Com pip

Instale a biblioteca diretamente do PyPI:

```bash
pip install dataquantum-yaml-reader
```

### Com Poetry

Adicione a biblioteca como dependência do projeto:

```bash
poetry add dataquantum-yaml-reader
```

### Estrutura de diretórios

Crie o diretório `config` na raiz do projeto para armazenar os arquivos de configuração com extensão `.yaml`.

## Exemplo de utilização

Considere a seguinte estrutura de diretórios:

```text
projeto/
├── config/
│   └── logging.yaml
├── src/
│   └── main.py
└── pyproject.toml
```

O arquivo `logging.yaml` contém:

```yaml
logging_info:
  level: "INFO"
  format: "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
  encoding: "utf-8"

logs:
  file: "logs/app.log"
```

### Lendo os arquivos YAML

Importe a função `get_reader_yaml` e informe o caminho do diretório que contém os arquivos de configuração.

```python
from pathlib import Path

from dataquantum_yaml_reader import get_reader_yaml


# Localiza a raiz do projeto, um nível acima de src/.
project_root = Path(__file__).resolve().parent.parent

# Define o caminho absoluto para o diretório de configurações.
config_path = project_root / "config"

configs = get_reader_yaml(config_path)

print(configs)
```
### Como funciona?
- ```__file__```: caminho do arquivo main.py.
- ```.resolve()```: transforma o caminho em absoluto.
- ```.parent```: retorna o diretório src/.
- ```.parent.parent```: retorna a raiz do projeto.
- ```/ "config"```: acrescenta o diretório config/ ao caminho.

### Resultado esperado

```python
{
    "logging": {
        "logging_info": {
            "level": "INFO",
            "format": "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            "encoding": "utf-8",
        },
        "logs": {"file": "logs/app.log"},
    }
}
```

O dicionário contém uma entrada para cada arquivo `.yaml` encontrado. A chave corresponde ao nome do arquivo sem a extensão, e o valor corresponde ao conteúdo carregado.

## Utilizando as configurações

Após carregar os arquivos, você pode acessar os valores por meio das chaves do dicionário.

```python
from pathlib import Path

from dataquantum_yaml_reader import get_reader_yaml

# Localiza a raiz do projeto, um nível acima de src/.
project_root = Path(__file__).resolve().parent.parent

# Define o caminho absoluto para o diretório de configurações.
config_path = project_root / "config"

configs = get_reader_yaml(config_path)

logging_config = configs["logging"]

level = logging_config["logging_info"]["level"]
log_format = logging_config["logging_info"]["format"]
encoding = logging_config["logging_info"]["encoding"]
log_file = logging_config["logs"]["file"]

print(level)
print(log_format)
print(encoding)
print(log_file)
```

Saída:

```text
INFO
%(asctime)s - %(levelname)s - %(name)s - %(message)s
utf-8
logs/app.log
```

## Quais erros podem ocorrer?

| Exceção |	Situação |
| ------- | -------- |
| FileNotFoundError |	O caminho informado não existe. |
| NotADirectoryError | O caminho existe, mas aponta para um arquivo, não para um diretório. |
| ValueError | Um arquivo YAML contém sintaxe inválida, conforme o tratamento implementado.
| OSError |	Ocorre um erro de sistema operacional ao acessar ou ler arquivos. |

Um arquivo YAML vazio não gera erro com yaml.safe_load(): seu valor será None.

## Aplicações

A biblioteca pode ser utilizada em diferentes contextos:

- **Análise de dados:** centralização de configurações de projetos analíticos.
- **Ciência de dados:** carregamento de parâmetros e configurações de experimentos.
- **Engenharia de dados:** gerenciamento de configurações de pipelines ETL.
- **Automação:** leitura de configurações utilizadas em scripts Python.
- **Integração de sistemas:** organização de parâmetros de conexão e configurações de aplicações.

## Desenvolvimento

Este projeto utiliza Poetry para gerenciamento de dependências e do ambiente de desenvolvimento.

Clone o repositório:

```bash
git clone https://github.com/jcarlossc/dataquantum-yaml-reader.git

cd dataquantum-yaml-reader
```

Instale as dependências:

```bash
poetry install
```

Execute os testes:

```bash
poetry run task pytest
```

Execute os testes com relatório de cobertura:

```bash
poetry run task covcmd
```

Execute as verificações de qualidade:

```bash
poetry run task check
poetry run task lint
poetry run task mypy
```

Execute a validação completa para o release:

```bash
poetry run task release-check
```

## Testes e qualidade

O projeto utiliza ferramentas para garantir a qualidade, a manutenção e a confiabilidade do código:

- **pytest:** execução dos testes automatizados.
- **pytest-cov:** medição da cobertura dos testes.
- **Ruff:** análise estática e formatação do código.
- **mypy:** verificação estática de tipos.
- **pre-commit:** execução de verificações automatizadas antes dos commits.
- **GitHub Actions:** integração contínua e automação de tarefas.
- **Release Please:** gerenciamento automatizado de releases e changelog.

## Versionamento

O projeto segue o Versionamento Semântico (*Semantic Versioning*), utilizando o formato:

`MAJOR.MINOR.PATCH`

- **MAJOR:** alterações incompatíveis com versões anteriores.
- **MINOR:** novas funcionalidades compatíveis com versões anteriores.
- **PATCH:** correções compatíveis com a versão existente.

Consulte o arquivo `CHANGELOG.md` para acompanhar o histórico de alterações.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

## Autor e contato

**DataQuantum**

- GitHub: [jcarlossc](https://github.com/jcarlossc)
- Repositório: [dataquantum-yaml-reader](https://github.com/jcarlossc/dataquantum-yaml-reader)
- E-mail: jcarlossc1977@gmail.com
>>>>>>> 6c11a82 (docs: readme add)
