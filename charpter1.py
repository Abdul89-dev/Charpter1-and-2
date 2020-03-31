

import vk_api

#типа попытался представиться
vk_session = vk_api.VkApi('+79161560488', '22bibebo')
vk_session.auth()

vk = vk_session.get_api()

