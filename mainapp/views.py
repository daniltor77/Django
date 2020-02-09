import datetime
from django.shortcuts import render

def main(request):
    title="главная"
    products= [
        {
        "name": "Отличный стул",
        "desc": "Расположитесь комфортно",
        "image_scr": "product-1.jpg",
        "image_href": "/product/1/",
        "alt": "продукт 1"
         },
        {
            "name":"Стул повышенного качества",
            "desc":"Не оторватся.",
            "image_scr": "product-2.jpg",
            "image_href": "/product/2/",
            "alt": "продукт 2"
        }
    ]
    content={"title": title,"products": products}
    return render(request, "mainapp/index.html", content)

def products (request):
    title="продукты"
    links_menu=[
        {"href":"products_all","name":"все"},
        {"href":"products_home","name":"дом"},
        {"href":"products_office","name":"офис"},
        {"href":"products_modern","name":"модерн"},
        {"href":"products_classic","name":"классика"}
    ]
    same_products=[
        {"name":"Отличный стул","desc":"Не отораваться","image_scr":"product-11.jpg","alt":"продукт 11"},
        {"name":"Стул повышенного качества","desc":"Комфортно.","image_scr":"product-21.jpg","alt":"продукт 21"},
        {"name":"Стул премиального качества","desc":"Просто попробуйте.","image_scr":"product-31.jpg","alt":"продукт 31"},
        {"name":"Попа влюбится","desc":"Получайте удовольствие снова и снова","image_scr":"product-51.jpg","alt":"продукт 51"}
    ]
    content={"title": title, "links_menu":links_menu, "same_products":same_products}
    return render(request, "mainapp/products.html", content)

def contact(request):
    title="наши контакты"
    visit_date=datetime.datetime.now()
    locations=[
        {"city":"Москва", "phone":"+7-888-888-8888", "email": "info@geekshop.ru", "address": "Впределах МКАД"},
        {
            "city":"Екатеренбург",
            "phone":"+7-777-777-7777",
            "email":"info@geekshop.ru",
            "address":"Близко к центру"
        },
        {
            "city":"Владивосток",
            "phone":"+7-999-999-9999",
            "email":"info@geekshop.ru",
            "address":"Близко к океану"
        }

    ]
    content={"title": title, "visit_date": visit_date, "locations": locations}
    return render(request, "mainapp/contact.html", content)

