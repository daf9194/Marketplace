from django.shortcuts import render
from django.views import generic, View
from app_goods.models import Good, GoodBasket
from app_goods.forms import AddGoodForm, ClearBasketForm
from app_users.models import Profile
from django.db import transaction

@transaction.atomic
def pay(summ, request):                                                                 #реализация работы с ТРАНЗАКЦИЕЙ
                                                                                        #если нажата другая кнопка (оформить заказ)
        old_bal = Profile.objects.get(user_id=request.user.id).balance                  #изменяем текущий баланс
        Profile.objects.filter(user_id=request.user.id).update(balance=old_bal-summ)    #на сумму покупок
        
        old_total_buy = Profile.objects.get(user_id=request.user.id).total_buy           #меняем total_buy
        Profile.objects.filter(user_id=request.user.id).update(total_buy=old_total_buy+summ)
        
        if Profile.objects.get(user_id=request.user.id).total_buy > 20000:
            Profile.objects.filter(user_id=request.user.id).update(status='MDL')

        if Profile.objects.get(user_id=request.user.id).total_buy > 40000:
            Profile.objects.filter(user_id=request.user.id).update(status='SEN')


        basket_list = Profile.objects.get(user_id=request.user.id).basket.all()          #изменяем остаток товаров
        for b in basket_list:                                                            #на складе
            old_am = Good.objects.get(id=b.good.id).amount
            Good.objects.filter(id=b.good.id).update(amount=old_am-b.count)

            old_pop = Good.objects.get(id=b.good.id).pop        
            Good.objects.filter(id=b.good.id).update(pop=old_pop+b.count)

        Profile.objects.get(user_id=request.user.id).basket.clear()                     #чистим корзину после заказа 

class GoodListView(View):
    def get(self, request):
        good_list = Good.objects.all()
        return render(request, 'good_list.html', context={'good_list' : good_list})

class GoodDetailView(View):
    def get(self, request, pk):
        good = Good.objects.get(id = pk)
        add_good = AddGoodForm()
        return render(request, 'good_detail.html', context={'good' : good, 'add_good': add_good})

    def post(self, request, pk):
        add_good = AddGoodForm(request.POST)
        good = Good.objects.get(id = pk)
        prof = Profile.objects.get(user_id=request.user.id)
        prof.basket.create(good=good, count=add_good.data['quan'])
        return render(request, 'good_detail.html', context={'add_good': add_good})

class BasketView(View):
    def get(self, request):
        basket_list = Profile.objects.get(user_id=request.user.id).basket.all()
        summ = 0
        for b in basket_list:
            summ += b.good.price*b.count


        return render(request, 'basket.html', context={'summ' : summ})

    def post(self, request):
        basket_list = Profile.objects.get(user_id=request.user.id).basket.all()             #считаем сумму покупок 
        summ = 0                                                                            #в корзине
        for b in basket_list:
            summ += b.good.price*b.count

        cl_basket = ClearBasketForm(request.POST)
        submit_button = request.POST.get('b1')
        if submit_button == 'clear':                                                        #если нажата кнопка очистить корзину
            Profile.objects.get(user_id=request.user.id).basket.clear()                     #чистим корзину

        else:
            pay(summ=summ, request=request)

        return render(request, 'basket.html', context={'cl_basket':cl_basket})

class ReportView(View):
    def get(self, request):

        good_list = Good.objects.order_by('-pop')[:5] #Первые 5 самых продаваемых товаров

        return render(request, 'report.html', context={'good_list' : good_list})

            