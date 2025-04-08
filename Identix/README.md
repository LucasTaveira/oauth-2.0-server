# 🧪 POC - Provedor de Identidade com OAuth2 (Django + django-oauth-toolkit)

## 📌 Objetivo

Criar um provedor de identidade OAuth2 que permita:

- Emissão de tokens via `client_credentials`.
- Gerenciamento dinâmico de escopos via banco de dados.
- Consulta de informações do usuário com token válido.

---

## ⚙️ Tecnologias Utilizadas

- Python 3.12
- Django
- Djando Rest Framework
- [django-oauth-toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/)


---

## 📂 Estrutura do Projeto

```
oauth-2.0-server/
├── Identix             #Base do projeto
├── api                 #Onde fica as request para projetos externs
└── auth_core           #Base de customização do django-oauth-toolkit
```

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone <URL_DO_SEU_REPO>
cd <nome-do-diretorio>
```

### 2. Instala as dependências
```
python -m venv .venv
source .venv/bin/activate  # No Windows use: .venv\Scripts\activate
```

### 3. Instala as dependências

```bash
pip install -r requirements.txt
```

### 4. Cria o banco de dados

```bash
python manage.py migrate
```

### 5. Inicia o servidor

```bash
python manage.py runserver
```
O projeto estará acessível em: http://localhost:8000

---
## 🔐 Fluxo de Autenticação

### 1. Criação de Application
- Tipo: `Confidential`
- Grant: `Client Credentials`
- Escopos vinculados via banco

### 2. Requisição de Token

```bash
curl -X POST http://localhost:8000/o/token/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=<client_id>" \
  -d "client_secret=<client_secret>" \
  -d "scope=wallet profile"
```

### 3. Resposta

```json
{
  "access_token": "<token>",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "wallet profile"
}
```

### 4. Requisição a recursos protegidos

```bash
curl http://localhost:8000/api/wallet/info-user \
  -H "Authorization: Bearer <access_token>"
```

---

## 🧠 Implementação de Escopos Dinâmicos

- Criação de model `Scope` e vínculo com `Application`
- Customização do backend:

```python
class ScopeBackend(BaseScopesBackend):
    def get_available_scopes(self, application=None, request=None, *args, **kwargs):

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
```

- Definido em `settings.py`:

```python
OAUTH2_PROVIDER = {
    "SCOPES_BACKEND_CLASS": "auth_core.oauth2.ScopeBackend",
}
```

---

## 🧪 Testes realizados

- ✅ Token com 1 escopo
- ✅ Token com múltiplos escopos
- ✅ Validação automática de escopos no banco
- ✅ Requisição negada com escopo inválido
- ✅ Verificação de `Content-Type`

---

## 🧾 Referências

- [OAuth2 RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)
- [django-oauth-toolkit Docs](https://django-oauth-toolkit.readthedocs.io/en/latest/)