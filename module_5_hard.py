"""
Задание "Свой YouTube":

Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики
на тему IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы
базовые знания программирования.
Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий
функционал на сайте.
Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео,
авторизации и регистрации пользователя и т.д.

Подробное ТЗ:
Создаем класс User. Каждый объект класса User должен обладать следующими атрибутами и методами:
•	Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число).
"""
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __hash__(self):
        return hash(self.password)

    def __int__(self):
        return self.age

"""
Подробное ТЗ:
Создаем класс Video. Каждый объект класса Video должен обладать следующими атрибутами и методами:
•	Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки
(изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию)).
"""
class Video:
    def __init__(self, title, duration, adult_mode = bool(False)):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return (self.title)

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return item in self.title

"""
Подробное ТЗ:
Создаем класс UrTube. Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
•	Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User);
•	Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните,
что password передаётся в виде строки, а сравнивается по хэшу;
•	Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname}
уже существует". После регистрации, вход выполняется автоматически;
•	Метод log_out для сброса текущего пользователя на None;
•	Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
названием видео ещё не существует. В противном случае ничего не происходит;
•	Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр);
•	Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
После текущее время просмотра данного видео сбрасывается.

Для метода watch_video так же учтены следующие особенности:
1.	Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time;
2.	Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль
надпись: "Войдите в аккаунт, чтобы смотреть видео";
3.	Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу";
4.	После воспроизведения нужно выводить: "Конец видео".
"""

import time  # Импортируем модуль time

class UrTube:
    def __init__(self):
        self.users =  []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user == user.nickname and password == user.password:
                self.current_user = user
                return

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Вы успешно зарегистрированы под именем {nickname}. Вход в аккаунт осуществлен!')

    def add(self, *files):
        for film in files:
            if film.title not in [video.title for video in self.videos]:
                self.videos.append(film)

    def get_videos(self, text):
        files_ = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                files_.append(video.title)
        return  files_

    def watch_video(self, film):
        if self.current_user:
            for video in self.videos:
                if self.current_user and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                if film in video.title:
                    for i in range(1, 11):
                        print(i, end = ' ')
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print('Конец видео')

        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

# Код для проверки:
if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')