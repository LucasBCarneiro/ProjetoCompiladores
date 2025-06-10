# Remove comentarios
def remove_comments(source):
    text = ''
    i = 0
    open_aspas = False

    while i < len(source):
        if source[i] == '"':
            open_aspas = not open_aspas
        if source[i] == '/' and not open_aspas and source[i + 1] in('/', '*'):
            if source[i + 1] == "*":
                i += 2
                while i < len(source):
                    if source[i] == '*' and source[i + 1] == '/':
                        i += 2
                        break
                    else:
                        i += 1
            elif source[i + 1] == '/':
                i += 2
                while i < len(source):
                    if source[i] == '\n':
                        break
                    else:
                        i += 1
        else:
            text += source[i]
        i += 1

    return text
