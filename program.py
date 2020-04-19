# /usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json

with open(r'token.txt', 'r', encoding='windows-1251') as f:
    access_token = f.read()
help = 'Для того, чтобы узнать закрытых друзей пользователя, введите его id.\n' \
       'Чтобы выйти из программы, введите "end".\n' \
       'Для корректного результата страница пользователя должна существовать и быть открытой.\n'


class VkApi:
    def __init__(self, access_token):
        self.access_token = access_token
        self.request = "https://api.vk.com/method/"
        print('Данная программа позволяет узнать список друзей пользователя ВКонтакте, имеющих закрытый профиль.\n'
              '(при условии, что пользователь существует и имеет открытый профиль)\n')

    def main(self):
        while True:
            user_id = input("Введите id пользователя.\n")
            if user_id == "end":
                break
            if user_id == "help":
                print(help)
            else:
                closed_friends = self.get_closed_friends(user_id)
                for friend in closed_friends:
                    print(friend)

    def get_friends(self, user_id):
        request = self.request + f"friends.get?user_id={user_id}&fields=nickname,%20domain&v=5.103&access_token={self.access_token}"
        r = requests.get(request)
        # print(r.text)
        if 'error' in r.text:
            print('Пользователь удалён или имеет закрытый профиль.')
            return []
        return json.loads(r.text)['response']['items']

    def get_closed_friends(self, user_id):
        data = self.get_friends(user_id)
        closed_friends = []
        for user in data:
            if 'is_closed' in user:
                if user['is_closed']:
                    closed_friends.append(f'{user["first_name"]} {user["last_name"]}')
        return closed_friends


if __name__ == '__main__':
    api = VkApi(access_token)
    api.main()
