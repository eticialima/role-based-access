from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Module, Permission, Role, UserRole

class Command(BaseCommand):
    help = 'Setup initial data for the role-based access control system'

    def handle(self, *args, **kwargs):
        # Create modules
        usuario_padrao = Module.objects.create(name="Usuario Padrão")
        colaborador = Module.objects.create(name="Colaborador")
        gerente = Module.objects.create(name="Gerente")

        # Create permissions for Usuario Padrão
        Permission.objects.create(name="visualizar_perfil", module=usuario_padrao)
        Permission.objects.create(name="editar_perfil", module=usuario_padrao)
        Permission.objects.create(name="alterar_senha", module=usuario_padrao)

        # Create permissions for Colaborador
        Permission.objects.create(name="visualizar_tarefas", module=colaborador)
        Permission.objects.create(name="criar_tarefa", module=colaborador)
        Permission.objects.create(name="editar_tarefa", module=colaborador)
        Permission.objects.create(name="excluir_tarefa", module=colaborador)

        # Create permissions for Gerente
        Permission.objects.create(name="listar_roles", module=gerente)
        Permission.objects.create(name="criar_role", module=gerente)
        Permission.objects.create(name="editar_role", module=gerente)
        Permission.objects.create(name="gerenciar_usuarios", module=gerente)
        Permission.objects.create(name="criar_projeto", module=gerente)
        Permission.objects.create(name="editar_projeto", module=gerente)
        Permission.objects.create(name="excluir_projeto", module=gerente)
        Permission.objects.create(name="visualizar_relatorios", module=gerente)

        # Create roles
        role_admin = Role.objects.create(name="Administrador")
        role_colaborador = Role.objects.create(name="Colaborador")
        role_usuario = Role.objects.create(name="Usuário Padrão")

        # Assign permissions to roles
        role_admin.permissions.set(Permission.objects.all())
        role_colaborador.permissions.set(Permission.objects.filter(
            module__in=[usuario_padrao, colaborador]
        ))
        role_usuario.permissions.set(Permission.objects.filter(
            module=usuario_padrao
        ))

        self.stdout.write(self.style.SUCCESS('Successfully set up initial data'))
