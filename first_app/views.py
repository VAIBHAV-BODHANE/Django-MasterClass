from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_app.models import Item
# from django.template import loader
from .forms import ItemForm


def index(request):
    # print(request.META.get('REMOTE_ADDR'))
    qs = Item.objects.all()
    print(qs)
    # template = loader.get_template('first_app/index.html')
    context = {
        'item_list': qs
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'first_app/index.html', context)


def item(request):
    return HttpResponse("<h1 style='text-align: center;'>This is an item view!<h1>")


def detail(request, item_id):
    try:
        qs = Item.objects.get(id=item_id)
        print(qs)
        context = {
            'list_item': qs,
        }
    except Item.DoesNotExist:
        return HttpResponse("<h1>NOT FOUND!</h1>")
    

    return render(request, 'first_app/detail.html', context)


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'first_app/item-form.html', {'form': form})


def update_item(request, id):
    item = Item.objects.get(id=id)
    print(item)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'first_app/item-form.html', {'form':form, 'item': item})


def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'first_app/delete-confirm.html', {'item':item})