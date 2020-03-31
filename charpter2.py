
import vk_api

def main():

login, password = '+79161560488', '22bibebo'
vk_session = vk_api.VkApi(login, password)


try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

vk = vk_session.get_api()

response = vk.friends.addList(count=1)  # выводим друзей

    if response['items']:
        print(response['items'][0])


if __name__ == '__main__':
    main()






print(vk_session.friends.addList/n)  # более лучшей идеи выведения с каждой строки у меня нет