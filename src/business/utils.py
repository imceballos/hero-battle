def format_message(message):
    if message['name'] == "attack":
        return f"{message['action']['sender']} {message['name']} to {message['action']['receiver']} ({message['action']['damage']})"
    elif message['name'] == 'eliminated':
        return f"{message['action']['receiver']} {message['name']}"
    return  f"{message['name']} {message['action']['sender']}"