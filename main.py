def on_button_pressed_a():
    basic.show_number(nb_9 / nb_exp * 100)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_value(name, value):
    global nb_exp, nb_9
    nb_exp += 1
    if value == 9:
        nb_9 += 1
    basic.show_number(value, 0)
    serial.write_value(name, value)
radio.on_received_value(on_received_value)

nb_exp = 0
nb_9 = 0
radio.set_group(1)
nb_9 = 0
nb_exp += 0