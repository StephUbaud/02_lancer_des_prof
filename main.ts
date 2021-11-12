input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(nb_9 / nb_exp * 100)
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    nb_exp += 1
    if (value == 9) {
        nb_9 += 1
    }
    
    basic.showNumber(value, 0)
    serial.writeValue(name, value)
})
let nb_exp = 0
let nb_9 = 0
radio.setGroup(1)
nb_9 = 0
nb_exp += 0
