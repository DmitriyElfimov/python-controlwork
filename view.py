import text


def menu():
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    while True:
        select = input(text.select_menu)
        if select.isdigit() and 0 < int(select) < int(len(text.main_menu)):
            return int(select)
        print(text.input_error)

def show_notes(book: dict[int:dict[str,str]], message):
    if book:
        max_name = []
        max_phone = []
        max_comment = []
        for note in book.values():
            max_name.append(len(note.get('name')))
            max_phone.append(len(note.get('phone')))
            max_comment.append(len(note.get('comment')))
        size_name = max(max_name)
        size_phone = max(max_phone)
        size_comment = max(max_comment)
        print('\n' + '='*(size_name + size_phone + size_comment + 7))
        for index, note in book.items():
            print(f'{index:>3}. {note.get("name"):<{size_name}} {note.get("phone"):<{size_phone}} {note.get("comment"):<{size_comment}}')
        print('='*(size_name + size_phone + size_comment + 7) + '\n')
    else:
        print(message)

def print_message(message: str):
    print('\n' + '='*len(message))
    print(message)
    print('='*len(message) + '\n')


def add_note():
    new = {}
    for key, value in text.new_note.items():
        new[key] = input(value)
    return new

def search_word() -> str:
    return input(text.search_word)

def del_note():
    return input(text.del_id)

def replace_note():
    return input(text.repl_id)

def view_input(message):
    return input(message)