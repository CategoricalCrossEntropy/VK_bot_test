from init import vk_session, session_api


def send_message(id_, message, keyboard=None):
    post = {"user_id": id_, "message": message, "random_id": 0}

    if keyboard is not None:
        post["keyboard"] = keyboard.get_keyboard()

    vk_session.method("messages.send", post)


def get_city(id_):
    user_info = session_api.users.get(user_id=id_, fields='city')
    try:
        city_name = user_info[0]['city']['title']
    except KeyError:
        city_name = None
    return city_name
