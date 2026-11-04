# API de Análise de Texto com FastAPI e Hugging Face 🚀

Uma API REST desenvolvida em **FastAPI** para sumarização e análise de sentimentos utilizando modelos avançados do **Hugging Face Transformers** (com execução otimizada em **CPU**). O projeto segue uma arquitetura modular e limpa, ideal para aplicações de Processamento de Linguagem Natural (PLN) em português.

---

## 🏗️ Arquitetura do Projeto

O projeto foi organizado de forma modular para separar responsabilidades (`routers`, `services`, `ml`, `schemas` e `core`, `tests`):

### 📁 Estrutura do Projeto

```text
ProjetoIA/
├── app/
│   ├── core/          # Configurações globais e exceções
│   ├── ml/            # Modelos de Machine Learning
│   ├── routers/       # Endpoints da API (FastAPI)
│   ├── schemas/       # Validação de dados (Pydantic)
│   ├── services/      # Regras de negócio e processamento
│   └── main.py        # Ponto de entrada da aplicação
│
├── tests/             # Testes automatizados
├── requirements.txt   # Dependências do projeto
├── pytest.ini         # Configurações do Pytest
├── .gitignore
└── README.md
```
