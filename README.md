# Sistema de Controle de Acesso Baseado em Funções

Este é um sistema de controle de acesso baseado em funções (RBAC) desenvolvido com Django. O sistema permite gerenciar usuários, funções e permissões de forma eficiente.

## Módulos

O sistema possui três módulos principais:
- **Usuário Padrão**: Gerenciamento de perfil e configurações básicas
- **Colaborador**: Gerenciamento de tarefas
- **Gerente**: Gerenciamento de projetos e usuários

## Configuração do Ambiente

1. Certifique-se de ter Python 3.10+ instalado
2. Clone o repositório
3. Crie um ambiente virtual:
```bash
python -m venv venv
```

4. Ative o ambiente virtual:
```bash
source venv/bin/activate  # Linux/Mac
```

5. Instale as dependências:
```bash
pip install django
```

6. Execute as migrações:
```bash
python manage.py migrate
```

7. Crie um superusuário:
```bash
python manage.py createsuperuser
```

8. Configure os dados iniciais:
```bash
python manage.py setup_initial_data
```

9. Inicie o servidor:
```bash
python manage.py runserver
```

## Estrutura de Permissões

### Usuário Padrão
- visualizar_perfil
- editar_perfil
- alterar_senha

### Colaborador
- visualizar_tarefas
- criar_tarefa
- editar_tarefa
- excluir_tarefa

### Gerente
- gerenciar_usuarios
- criar_projeto
- editar_projeto
- excluir_projeto
- visualizar_relatorios

## Desenvolvimento

O projeto utiliza:
- Django 5.1+
- Python 3.10+
- SQLite (padrão)

## Contribuição

1. Faça um Fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Crie um Pull Request
