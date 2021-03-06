from flask import Flask, url_for, request
import os

app = Flask(__name__)

@app.route('/')
def show():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return f"""Человечество вырастает из детства.<br>
            Человечеству мала одна планета.<br>
            Мы сделаем обитаемыми безжизненные пока планеты.<br>
            И начнем с Марса!<br>
            Присоединяйся!"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpeg')}" 
                        alt="здесь должна была быть картинка, но не нашлась" width= "100%">
                    <h3>Вот она какая, красная планета</h3>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!!</h1>
                    <img src="{url_for('static', filename='img/mars.jpeg')}" 
                        alt="здесь должна была быть картинка, но не нашлась" width="100%">
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-dark" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>
            """


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles5.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body class="container">
                            <h1>Анкета претендента</h1>
                            <h4>на участие в миссии</h4>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <input type="text" class="form-control" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">

                                    <div class="form-group">
                                        <label for="eduselect">Какое у Вас образование?</label>
                                        <select class="form-control" id="eduselect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                          <option>3 класса церковно-приходской школы</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="engineer" value="инженер-исследователь">
                                          <label class="form-check-label" for="engineer">
                                            инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="pilot" value="пилот">
                                          <label class="form-check-label" for="pilot">
                                            пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="builder" value="строитель">
                                          <label class="form-check-label" for="builder">
                                            строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="exobiologist" value="экзобиолог">
                                          <label class="form-check-label" for="exobiologist">
                                            экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="doctor" value="врач">
                                          <label class="form-check-label" for="doctor">
                                            врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="terraformingengineer" value="инженер по терраформированию">
                                          <label class="form-check-label" for="terraformingengineer">
                                            инженер по терраформированию
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="climatologist" value="климатолог">
                                          <label class="form-check-label" for="climatologist">
                                            климатолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="radprotectspec" value="специалист по радиационной защите">
                                          <label class="form-check-label" for="radprotectspec">
                                            специалист по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="astrogeologist" value="астрогеолог">
                                          <label class="form-check-label" for="astrogeologist">
                                            астрогеолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="skills[]" id="glaciologist" value="гляциолог">
                                          <label class="form-check-label" for="glaciologist">
                                            гляциолог
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="motivation">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="motivation" rows="3" name="motivation"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="longstay" name="longstay">
                                        <label class="form-check-label" for="longstay">Готовы ли остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''

    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form.getlist('skills[]'))
        if request.files['file']:
            print(request.files['file'].read())

        print(request.form['motivation'])
        print(request.form['sex'])
        print(request.form['longstay'])
        return "Форма отправлена"

@app.route('/choice/<planet_name>')
def choice(planet_name):
    planets = {
        "марс": {
            "name": "Марс",
            "benefits": [
                'Марс называют Красной планетой из-за характерного оттенка поверхности. Все из-за железа – ржавая пыль не только покрывает саму планету, но и поднимается в атмосферу.',
                'На Марсе есть вода!',
                'Чтобы долететь до Марса, нужен примерно год.',
                'Самый большой из кратеров называется Великой Северной равниной и занимает около 40% поверхности планеты'
            ]},
        "венера": {
            "name": "Венера",
            "benefits": [
                'Венера ближе чем Марс',
                'Атмосфера Венеры в 93 раза плотнее, чем у Земли, а значит в ней легче затормозить при приземлении',
                'По размеру Венера сопоставима с Землёй и у неё почти такая же сила тяжести',
                'Ионосфера Венеры защитит от радиации'
            ]},
        "юпитер": {
            "name": "Юпитер",
            "benefits": [
                'Юпитер – самая большая планета в Солнечной системе',
                'Юпитер – планета, у которой обнаружено наибольшее количество естественных лун. Всего их 79, но самые известные – Ио, Ганимед, Каллисто и Европа.',
                'Ураганы на Юпитере разгоняются до скорости в 600 км/ч, и результат этого прекрасно виден из космоса или даже в простенький телескоп!',
                'В 2011 году к Юпитеру отправился космический аппарат «Юнона». Планеты он достиг только летом 2016 года, и с тех пор регулярно отправляет на Землю снимки и данные исследований. Вместе с миссией «Юнона» к газовому гиганту отправились три фигурки LEGO'
            ]},
        "нептун": {
            "name": "Нептун",
            "benefits": [
                "Третья по массе планета Солнечной системы!",
                "Никогда не жарко - самая дальняя планета от Солнца(кроме Плутона, но он уже не планета Т-Т)",
                "Очень долго о нем ничего не было известно - его открыли с помощью рассчетов в XIX веке",
                "Здорово пускать воздушного змея - самые сильные ветры во всей Солнечной системе(до 600 м\с)"
            ]},
        "плутон": {
            "name": "Плутон",
            "benefits": [
                'Плутон не планета',
                'Плутон это МАЛАЯ планета по классаификации 2006',
                'Он очень маленький и холодный',
                'На нем есть пятно в форме сердечка'
            ]
        },
    }
    key = planet_name.lower()
    try:
        test = planets[key]['name']
    except KeyError:
        return 'упс'

    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planets[key]['name']}!</h1>


                    <div class="alert alert-secondary" role="alert">
                      {planets[key]['benefits'][0]}
                    </div>
                    <div class="alert alert-success" role="alert">
                      {planets[key]['benefits'][1]}
                    </div>
                    <div class="alert alert-warning" role="alert">
                      {planets[key]['benefits'][2]}
                    </div>
                    <div class="alert alert-danger" role="alert">
                      {planets[key]['benefits'][3]}
                    </div>
                  </body>
                </html>
            """


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body class="container">
                    <h1>Результаты отбора</h1>
                    <h2>Претендерта на участие в миссии {nickname}:<h2>

                    <div class="alert alert-success" role="alert">
                      <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                    </div>
                    <div class="alert" role="alert">
                      <h3>составляет {rating}!</h3> 
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h2>Желаем удачи!</h2>
                    </div>
                  </body>
                </html>
            """

@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    profile_photo = 'img/default.jpg'
    if os.path.isfile('./static/img/profile.jpg'):
        profile_photo = 'img/profile.jpg'

    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                            <h2>для участия в миссии</h2>
                            <form class="p-3" method="post" enctype="multipart/form-data">
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <div class="form-group pt-3">
                                    <img src="{url_for('static', filename=profile_photo)}" width="300px">
                                </div>
                                <div class="form-group pt-3">
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </div>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        f.save('./static/img/profile.jpg')
        return "Форма отправлена"


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                            <title>Пейзажи Марса</title>
                        </head>
                        <body>
                            <div class="container">
                                <h1>Пейзажи Марса</h1>
                                <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                                  <div class="carousel-indicators">
                                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                                    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
                                  </div>
                                    <div class="carousel-inner">
                                        <div class="carousel-item active">
                                            <img class="d-block w-100" src="{url_for('static', filename='img/mars1.jpg')}" alt="First slide">
                                        </div>
                                        <div class="carousel-item">
                                            <img class="d-block w-100" src="{url_for('static', filename='img/mars2.jpg')}" alt="Second slide">
                                        </div>
                                        <div class="carousel-item">
                                            <img class="d-block w-100" src="{url_for('static', filename='img/mars3.jpg')}" alt="Third slide">
                                        </div>
                                    </div>
                                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Previous</span>
                                    </button>
                                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                        <span class="visually-hidden">Next</span>
                                    </button>
                                </div>
                            </div>
                            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
                        </body>
                    </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')