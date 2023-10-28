from django import forms
from .models import Client, Product, Order

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, label='Название товара')
    description = forms.CharField(widget=forms.Textarea, label='Описание товара')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='Цена товара')
    quantity = forms.IntegerField(label='Количество товара')
    photo = forms.ImageField(label='Фотография товара')  # Добавляем поле для загрузки фотографии

class OrderForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Выберите клиента')
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple, label='Выберите товары')
    total_amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Общая сумма заказа')
    order_date = forms.DateField(label='Дата оформления заказа')

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя клиента')
    email = forms.EmailField(label='Email клиента')
    phone_number = forms.CharField(max_length=15, label='Номер телефона клиента')
    address = forms.CharField(widget=forms.Textarea, label='Адрес клиента')
    registration_date = forms.DateField(label='Дата регистрации клиента')
    
class ClientTimePeriodForm(forms.Form):
    client = forms.ModelChoiceField(queryset=Client.objects.all(), empty_label="Выберите клиента")
    time_period = forms.ChoiceField(choices=[("7 дней", "Последние 7 дней"), ("30 дней", "Последние 30 дней"), ("365 дней", "Последние 365 дней")])

class InfoForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок')
    content = forms.CharField(widget=forms.Textarea, label='Содержание')
