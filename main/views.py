from django.shortcuts import render, redirect
from django.views import View
from .models import Link
from .forms import LinkForm
from .back import shortner


def Home(request, token):
    urls = Link.objects.all()
    # print(urls.values())
    # for i in urls:
    #     print(i)
    long_url = Link.objects.filter(short_link=token)[0]
    return redirect(long_url.original_link)


def Create(request):
    form = LinkForm(request.POST)
    token = ''
    print(form)
    if request.method == 'POST':
        if form.is_valid():
            original_link_list = [key['original_link'] for key in Link.objects.values()]
            ShortLink = form.save(commit=False)
            if ShortLink.original_link in original_link_list:
                token = Link.objects.get(original_link=ShortLink.original_link).short_link
            else:
                token = shortner().issue_token()
                token_list = [key['short_link'] for key in Link.objects.values()]
                while token in token_list:
                    token = shortner().issue_token()
                ShortLink.short_link = token
                ShortLink.save()
        else:
            form = LinkForm()
            token = "Invalid URL"
    return render(request, 'base.html', {'form': form, 'token': token})
