def format_message(message):
    if message['name'] == "attack":
        return f"{message['action']['sender']} {message['name']} to {message['action']['receiver']} ({format_damage(message['action']['damage'])})"
    elif message['name'] == 'eliminated':
        return f"{message['action']['receiver']} {message['name']}"
    return f"{message['name']} {message['action']['sender']}"

def format_damage(damage):
    float_number = float(damage)
    truncated_number = "{:.2f}".format(float_number)
    return str(truncated_number)