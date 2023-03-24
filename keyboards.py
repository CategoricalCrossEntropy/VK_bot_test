from vk_api.keyboard import VkKeyboard, VkKeyboardColor

from functions import send_message


def get_keyboard(texts, colors, one_time=True):
    kbd = VkKeyboard(one_time=one_time)
    for text, color in zip(texts, colors):
        kbd.add_button(text, color)
    return kbd


def main_menu(id_):
    kbd = VkKeyboard(one_time=True)
    kbd.add_button("Погода", VkKeyboardColor.PRIMARY)
    kbd.add_line()
    kbd.add_button("Пробка (в разработке)", VkKeyboardColor.PRIMARY)
    kbd.add_line()
    kbd.add_button("Афиша (в разработке)", VkKeyboardColor.PRIMARY)
    kbd.add_line()
    kbd.add_button("Валюта", VkKeyboardColor.PRIMARY)
    kbd.add_line()
    kbd.add_button("Сменить город", VkKeyboardColor.PRIMARY)
    send_message(id_, "Выбери пункт, который хочешь посмотреть",
                 keyboard=kbd)
