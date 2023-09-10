import text
import view
import model


def start():
    pb = model.NoteBook()
    while True:
        select = view.menu()
        match select:
            case 1:
                if pb.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if pb.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_notes(pb.note, text.empty_book)

            case 5:
                new = view.add_note()
                pb.add_note(new)
                view.print_message(text.add_successful(new.get('name')))
            case 6:
                word = view.search_word()
                result = pb.search(word)
                view.show_notes(result, text.empty_search(word))
            case 7:
                repl_id = int(view.replace_note())
                new = view.add_note()
                pb.replace(repl_id, new)
                view.print_message(text.repl_successful(new.get('name')))
            case 8:
                del_id = view.del_note()
                name = pb.del_note(del_id)
                view.print_message(text.del_successful(name))
            case 9:
                if pb.check_on_exit():
                    answer = view.view_input(text.change_confirm)
                    if answer != 'n':
                        pb.save_file()
                view.print_message(text.exit_file)
                break