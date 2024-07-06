from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from . forms import ArticleForm, UpdateUserForm

from teacher.models import Article

from django.http import HttpResponse

from . models import Articlee

from account.models import CustomUser

@login_required(login_url = '/my-login/')
def student_dashboard(request):
    return render(request, 'student/student-dashboard.html')


@login_required(login_url='/my-login/')
def create_article(request):
    
    form = ArticleForm()
    
    if request.method == 'POST':

        form = ArticleForm(request.POST)

        if form.is_valid():

            articlee = form.save(commit = False)

            articlee.user = request.user

            articlee.save()

            return redirect('my-articles2')

    context = {'CreateArticleForm': form}
    return render(request, 'student/create-article2.html', context)
    
@login_required(login_url='my-login')
def my_articles(request):
    current_user = request.user.id
    articlee = Articlee.objects.all().filter(user=current_user)

    context = {'AllArticles': articlee}

    return render(request, 'student/my-articles2.html', context)

@login_required(login_url='my-login')
def browse_articles(request):   

    articles = Article.objects.all()
    
    context = {'AllArticles': articles}

    return render(request, 'student/browse-articles.html', context)
    


@login_required(login_url='my-login')
def update_article(request, pk):

    try:
        articlee = Articlee.objects.get(id = pk, user=request.user)

    except:

        return redirect('my-articles2')
    form = ArticleForm(instance=articlee)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=articlee)

        if form.is_valid():
            form.save()

            return redirect('my-articles2')

    context = {'UpdateArticleForm':form}

    return render(request, 'student/update-article2.html', context)


@login_required(login_url='my-login')
def delete_article(request, pk):

    try:

    
        articlee = Articlee.objects.get(id=pk, user=request.user)
    except:
        return redirect('my-articles2')

    if request.method == 'POST':

        articlee.delete()

        return redirect('my-articles2')

    return render(request, 'student/delete-article2.html')


@login_required(login_url='my-login')
def account_management(request):
    
    form = UpdateUserForm(instance = request.user)

    if request.method == 'POST':

        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():

            form.save()

            return redirect('student-dashboard')

    context = {'UpdateUserForm': form}

    return render(request, 'student/account-management3.html', context)


@login_required(login_url='my-login')
def delete_account(request):

    if request.method == 'POST':

        deleteUser =CustomUser.objects.get(email=request.user)

        deleteUser.delete()

        return redirect('my-login')

    return render(request, 'student/delete-account2.html')


