import text
from datetime import date

def menu():
    print(text.main_menu[0])
    for i in range(1, len(text.main_menu)):
        print(f'\t{i}. {text.main_menu[i]}')
    while True:
        select = input(text.select_menu)
        if select.isdigit() and 0 < int(select) < int(len(text.main_menu)):
            return int(select)
        print(text.input_error)

def show_notes(book: dict[int:dict[str,str, str]], message):
    if book:
        max_name = []
        max_note = []
        max_date = []
        
        for note in book.values():
            max_name.append(len(note.get('name')))
            max_note.append(len(note.get('note')))
            
            
        size_name = max(max_name)
        size_note = max(max_note)
        
        print('\n' + '='*(size_name + size_note + 17))
        for index, note in book.items():
            print(f'{index:>3}. {note.get("name"):<{size_name}} {note.get("note"):<{size_note}} {note.get("date")}')
        print('='*(size_name + size_note + 17) + '\n')
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