<div align="center">

# 🚀 API de Gestão de Projetos (SIS Innov Challenge)

### Solução High-End com Django Rest Framework, Clean Arch e Docker.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

</div>

> Solução técnica desenvolvida para o desafio da **SIS Innov & Tech**, focada em **Clean Architecture**, **Escalabilidade** e **Segurança**.

## 📋 Sobre o Projeto
Este projeto consiste em uma API RESTful para gerenciamento do ciclo de vida de projetos de inovação. Diferente de uma estrutura Django padrão, este sistema foi arquitetado visando desacoplamento e facilidade de manutenção, utilizando princípios de **DDD (Domain-Driven Design)**.

### ✨ Diferenciais Técnicos
- **Arquitetura Modular:** Separação clara entre configurações (`config`) e domínios de negócio (`apps/projects`, `apps/users`).
- **Autenticação JWT:** Implementação de segurança *stateless* via `SimpleJWT`.
- **Regras de Negócio Isoladas:** Lógica de "Owner" (Dono do projeto) automatizada e protegida no nível da View.
- **Ambiente Dockerizado:** `Dockerfile` configurado para deploy rápido e reprodutível.
- **Dependency Management:** Controle estrito de versões via `requirements.txt`.

---

## 🛠 Tech Stack

| Tecnologia | Função | Motivação |
|------------|--------|-----------|
| **Django 5.2** | Framework Web | Robustez e segurança nativa (ORM, Auth). |
| **DRF** | API Toolkit | Padronização REST e Serialização eficiente. |
| **PostgreSQL** | Banco de Dados | (Configurado via driver `psycopg2` para produção). |
| **SimpleJWT** | Autenticação | Padrão de mercado para APIs seguras. |
| **Docker** | Container | Garantia de ambiente idêntico em Dev/Prod. |

---

## 🏛 Estrutura do Projeto (Clean Arch)
A organização de pastas foi pensada para escalabilidade:

```bash
desafio-sis-innov/
├── apps/                  # Domínios da Aplicação
│   ├── projects/          # Lógica de Projetos (Models, Serializers, Views)
│   └── users/             # Gestão de Identidade
├── config/                # Configurações Globais (Settings, URLs, WSGI)
├── .gitignore             # Arquivos ignorados pelo Git
├── Dockerfile             # Receita de Container
├── manage.py              # CLI do Django
└── requirements.txt       # Dependências do Projeto
```

---

## Como Rodar Localmente
**Pré-requisitos**
- Python 3.11+
- Git

**Passo a passo**
1. **Clone o repositório**

```bash
git clone [https://github.com/davidabx-dev/desafio-sis-innov.git](https://github.com/davidabx-dev/desafio-sis-innov.git)
cd desafio-sis-innov
```

---

2. **Crie e ative o ambiente virtual**

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

---

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

---

4. **Execute as migrações**

```bash
python manage.py migrate
```

---

5. **Crie um Superusuário (Admin)**

```bash
python manage.py createsuperuser
```

---

6. **Inicie o servidor**

```bash
python manage.py runserver
```
>Acesse a API em: `http://127.0.0.1:8000/api/projects/`

---

## Endpoints da API

| Método | Endpoint | Descrição | Auth Requerida |
|------------|--------|-----------|-----------|
| **`POST`** | **`/api/token/`** | Obter Token JWT (Login) | **❌ Não** |
| **`GET`** | **`/api/projects/`** | Listar seus projetos | **✅ Sim** |
| **`POST`** | **`/api/projects/`** | Criar novo projeto | **✅ Sim** |
| **`PUT`** | **`/api/projects/{id}/`** | Atualizar projeto | **✅ Sim** |
| **`DELETE`** | **`/api/projects/{id}/`** | GDeletar projeto | **✅ Sim** |

---

## 👨‍💻 Autor
**DavidABx** Desenvolvedor Python focado em soluções escaláveis e arquitetura limpa.

---
