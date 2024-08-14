from time import sleep

class user:

    def __init__(self, nickname = None, password = None, age = None):
        self.name = nickname
        self.password = hash(password)
        self.age = age

class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.abult_mode = adult_mode

class UrTube:

    def __init__(self, users=None, videos=None, current_user=None):
        if videos is None:
            videos = []
        if users is None:
            users = []
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        false_count = 2
        for people in self.users:
            if nickname == people.name:
                if hash(password) == people.password:
                    self.current_user = people
                    print(f'Вход выполнен, добро пожаловать, {self.current_user.name}')
                else:
                    while password != people.password and false_count > 0:
                        print(f'Пароль неверный. Количество оставшихся попыток: {false_count}')
                        password = int(input(f'Повторите пароль: '))
                        false_count -= 1
                    if password == people.password:
                        self.current_user = people
                        print(f'Вход выполнен, добро пожаловать, {self.current_user.name}')
                    else:
                        print('Возвращайтесь, когда вспомните пароль. До свидания :)')
                        break

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        check = False
        new_people = user()
        new_people.name = nickname
        new_people.password = password
        new_people.age = age
        for people in self.users:
            if new_people.name == people.name:
                check = True
        if check == True:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(new_people)
            self.log_in(nickname, password)

    def add(self, *element_case):
        for element in element_case:
            self.videos.append(element)

    def get_videos(self, slovo):
        found = []
        for video in self.videos:
            if slovo.lower() in video.title.lower():
                found.append(video.title)
        return found

    def watch_video(self, title_video):
        if self.current_user != None:
            for video in self.videos:
                if title_video == video.title:
                    if video.abult_mode is False or (video.abult_mode is True and self.current_user.age >= 18):
                        print(*range(1, video.duration+1), 'Конец видео')
                    else:
                        print('Вам нет 18 лет, вы не сможете посмотреть данное видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def viev_users(self):
        for people in self.users:
            print(people.name, people.password, people.age, len(self.users))

    def viev_videos(self):
        for video in self.videos:
            video: Video
            print(video.title, video.duration, video.time_now, video.abult_mode)


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

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
    print(ur.current_user.name)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')