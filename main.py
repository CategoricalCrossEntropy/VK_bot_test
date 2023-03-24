from vk_api.keyboard import VkKeyboardColor
from vk_api.longpoll import VkEventType

from functions import send_message, get_city
from init import longpoll, user_cities
from keyboards import get_keyboard, main_menu
from parse_data import get_weather, get_courses


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text
        user_id = event.user_id
        city = get_city(user_id)

        if msg.lower() == "начать":
            if user_id not in user_cities and city is None:
                send_message(user_id, "Введи название своего города:")
                user_cities[user_id] = "Enter_city_name"
            elif user_id not in user_cities and city is not None:
                buttons = ["Да", "Нет"]
                button_colors = [VkKeyboardColor.POSITIVE, VkKeyboardColor.NEGATIVE]
                send_message(user_id, "Твой город - {}?".format(city),
                             keyboard=get_keyboard(buttons, button_colors))
                user_cities[user_id] = "Is_it_your_city"
            else:
                main_menu(user_id)

        elif user_id in user_cities and user_cities[user_id] == "Enter_city_name":
            user_cities[user_id] = msg
            main_menu(user_id)

        elif user_id in user_cities and user_cities[user_id] == "Is_it_your_city":
            if msg == "Да":
                user_cities[user_id] = city
                main_menu(user_id)
            elif msg == "Нет":
                send_message(user_id, "Введи название своего города:")
                user_cities[user_id] = "Enter_city_name"

        elif msg == "Погода":
            buttons = ["Сегодня", "Завтра", "Меню"]
            button_colors = [VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY, VkKeyboardColor.PRIMARY]
            send_message(user_id, "Выбери день, на который хочешь посмотреть погоду:",
                         keyboard=get_keyboard(buttons, button_colors))

        elif msg == "Меню":
            main_menu(user_id)

        elif msg == "Сегодня":
            temp, desc = get_weather(user_cities[user_id], day="today")
            if temp is None:
                send_message(user_id, "Не удалось найти данные о погоде(")
            else:
                send_message(user_id, "Температура сегодня: {}\n{}".format(temp, desc))
            main_menu(user_id)

        elif msg == "Завтра":
            temp, _ = get_weather(user_cities[user_id])
            if temp is None:
                send_message(user_id, "Не удалось найти данные о погоде(")
            else:
                send_message(user_id, "Температура на завтра: {}".format(temp))
            main_menu(user_id)

        elif msg == "Валюта":
            money = get_courses()
            text = "\n".join(["{}: {} рублей".format(key, val) for key, val in money.items()])
            send_message(user_id, text)
            main_menu(user_id)

        elif msg == "Пробка (в разработке)":
            main_menu(user_id)

        elif msg == "Афиша (в разработке)":
            main_menu(user_id)

        else:
            send_message(user_id, "Неизвестная команда")
