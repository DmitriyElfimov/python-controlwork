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
                view.show_contacts(pb.contact, text.empty_book)
            case 4:
                new = view.add_contact()
                pb.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = pb.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                repl_id = int(view.replace_contact())
                new = view.add_contact()
                pb.replace(repl_id, new)
                view.print_message(text.repl_successful(new.get('name')))
            case 7:
                del_id = view.del_contact()
                name = pb.del_contact(del_id)
                view.print_message(text.del_successful(name))
            case 8:
                if pb.check_on_exit():
                    answer = view.view_input(text.change_confirm)
                    if answer != 'n':
                        pb.save_file()
                view.print_message(text.exit_file)
                break