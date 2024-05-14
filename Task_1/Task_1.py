# Создать базовый шаблон для интернет-магазина,
# содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы «Одежда»,
# «Обувь» и «Куртка», используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shoes/')
def about():
    shoes = [{
        'shoes': 'Мужские туфли бренда BULVAR- выполнены из 100% высококачественной натуральной кожи.',
        'prices': 4379,
        'size': 41,
        'colour': 'черный'
    },
        {
            'sneakers': 'Кеды NIKE, размер 10.5 US',
            'prices': 15799,
            'size': 43.5,
            'colour': 'белый'
        }]
    context = {
        'shoe': shoes
    }
    return render_template('shoes.html', **context)


@app.route('/clothes/')
def clothes():
    clothes = [{
        'sweatshirt': 'Свитшот Zolla, размер XL',
        'prices': 1279,
        'size': 52,
        'colour': 'зеленый'
    },
        {
            'sweater': 'Джемпер FINN FLARE, размер 2XL',
            'prices': 2160,
            'size': 56,
            'colour': 'черный'
        }]
    context = {
        'clothe': clothes
    }
    return render_template('clothes.html', **context)


@app.route('/jacket/')
def jacket():
    jacket = [{
        'jacket': 'Кожаная куртка , размер XXL',
        'prices': 24911,
        'size': 54,
        'colour': 'черный'
    },
        {
            'jacket': 'Бомбер ALPHA INDUSTRIES, размер XS',
            'prices': 10799,
            'size': 42,
            'colour': 'зеленый'
        }]
    context = {
        'jacke': jacket
    }
    return render_template('jackets.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
