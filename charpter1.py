

import vk_api

#типа попытался представиться
vk_session = vk_api.VkApi('+79161560488', '22bibebo')
vk_session.auth()

vk = vk_session.get_api()

# это попытка сделать запрос на список друзей
vk_session = vk_api.VkApi('+79161560488', '22bibebo')
vk_session.order.hints()

vk = vk_session.get_api()

print(vk_session.order.hints)


#выведение каждого друга с новой строки
vk_session = vk_api.VkApi('+79161560488', '22bibebo')
vk_session.order.hints()

vk = vk_session.get_api()

print(vk_session.order.hints/n)  # более лучшей идеи выведения с каждой строки у меня нет