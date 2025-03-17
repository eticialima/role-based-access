from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Role, Permission, UserRole
from .decorators import has_permission
from django.contrib import messages

@login_required
@has_permission('listar_roles')
def role_list(request):
    roles = Role.objects.all()
    return render(request, 'core/role_list.html', {'roles': roles})

@login_required
@has_permission('criar_role')
def role_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        permissions = request.POST.getlist('permissions')
        
        role = Role.objects.create(name=name)
        role.permissions.set(Permission.objects.filter(id__in=permissions))
        messages.success(request, 'Função criada com sucesso!')
        return redirect('role_list')
    
    permissions = Permission.objects.all()
    return render(request, 'core/role_form.html', {'permissions': permissions})

@login_required
@has_permission('editar_role')
def role_edit(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        permissions = request.POST.getlist('permissions')
        
        role.name = name
        role.save()
        role.permissions.set(Permission.objects.filter(id__in=permissions))
        messages.success(request, 'Função atualizada com sucesso!')
        return redirect('role_list')
    
    permissions = Permission.objects.all()
    return render(request, 'core/role_form.html', {
        'role': role,
        'permissions': permissions
    })
