def handle_keys(user_input):
    # Get the keyboard pressed character
    # Pega o caracter pressionado no teclado
    key_char = user_input.char

    # Movement keys (Vim keys to move diagonaly)
    # Teclas de movimentação (teclas Vim para movimentação diagonal)
    if user_input.key == 'UP' or key_char == 'k':
        return {'move': (0, -1)}
    elif user_input.key == 'DOWN' or key_char == 'j':
        return {'move': (0, 1)}
    elif user_input.key == 'LEFT' or key_char == 'h':
        return {'move': (-1, 0)}
    elif user_input.key == 'RIGHT' or key_char == 'l':
        return {'move': (1, 0)}
    elif key_char == 'y':
        return {'move': (-1, -1)}
    elif key_char == 'u':
        return {'move': (1, -1)}
    elif key_char == 'b':
        return {'move': (-1, 1)}
    elif key_char == 'n':
        return {'move': (1, 1)}

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt + Enter: toggle full screen
        # Alt + Enter: modo tela cheia
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exit the game
        # Sai do jogo
        return {'exit': True}

    # No key was pressed
    # Nenhuma tecla foi pressionada
    return {}
