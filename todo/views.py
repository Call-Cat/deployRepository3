from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse #new_todoで利用。
from .forms import TodoForm, TodoEditForm


@login_required
def index(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort_by', '')
    sort_order = request.GET.get('sort_order', 'asc')  # 昇順をデフォルトとする

    todos = TodoItem.objects.filter(user=request.user)
    
    if query:
        todos = todos.filter(title__icontains=query)  # タイトルであいまい検索
    
    if sort_by == 'title':
        if sort_order == 'asc':
            todos = todos.order_by('title')
        else:
            todos = todos.order_by('-title')  # タイトルでの降順
    elif sort_by == 'created_at':
        if sort_order == 'asc':
            todos = todos.order_by('created_at')
        else:
            todos = todos.order_by('-created_at')  # 作成日時での降順

    return render(request, 'todo/index.html', {'todos': todos})


def logout_check_view(request):
    # ログアウトの確認画面のテンプレートをレンダリングする
    return render(request, 'todo/logout_check.html')

def logout_view(request):
    logout(request)
    # ログアウト後にリダイレクトするページを指定する
    return redirect('login') # 'login' は《class Views》に対応した『accounts/urls.py』の URL パターンの名前

def index_view(request):
    # キャンセルボタンが押された時のリダイレクト先を指定する
    return redirect('index')  # これは適切なページにリダイレクトする必要があります



def mypage_view(request):
    # マイページへ遷移する。
    return render(request, 'todo/mypage.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # パスワード変更後にセッションを更新
            messages.success(request, 'パスワードが変更されました。')
            return redirect('mypage')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'todo/change_password.html', {'form': form})



@login_required
def new_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            user = request.user
            TodoItem.objects.create(title=title, user=user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TodoForm()

    return render(request, 'todo/new_todo.html', {'form': form})

def todo(request, todo_id):
    todo = TodoItem.objects.get(pk=todo_id)
    return render(request, 'todo/todo.html', {'todo': todo})


def edit_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)

    if request.method == 'POST':
        form = TodoEditForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            # titleがNoneの場合は空文字にする
            if title is not None:
                todo.title = title
            todo.description = form.cleaned_data.get('description', '')  # descriptionがない場合は空文字にする
            todo.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TodoEditForm(initial={'title': todo.title, 'description': todo.description})

    return render(request, 'todo/edit_todo.html', {'form': form, 'todo': todo})


def update_todo(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.save()
        return redirect('index')  # メモを更新した後、トップページにリダイレクトする
    return render(request, 'edit_todo.html', {'todo': todo})

def delete_todo(request, todo_id):
    try:
        todo = TodoItem.objects.get(pk=todo_id)
    except TodoItem.DoesNotExist:
        return HttpResponseNotFound("Todo does not exist")

    # Delete the todo
    todo.delete()

    # Redirect to index or any other appropriate page
    return redirect('index')
