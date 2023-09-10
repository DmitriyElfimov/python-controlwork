import json
import datetime



class NoteBook:

    def __init__(self, path: str = 'notes.json'):
        self.note: dict = {}
        self.not_changed = {}
        self.path = path


    def get(self, index: int | None = None):
        if index:
            return self.note.get(index)
        return self.note

    def open_file(self):
        try:
            with open (self.path, 'r', encoding='UTF-8') as file:
                self.note = json.load(file)
                self.not_changed = self.note.copy()
            return True
        except:
            return False


    def save_file(self):
        try:
            with open(self.path, 'w', encoding='UTF-8') as file:
                json.dump(self.note, file, ensure_ascii=False, indent=4)
            return True
        except:
            return False


    def search(self, word: str) -> dict[int:dict[str,str,str]]:
        result = {}
        for index, note in self.note.items():
            if word.lower() in ' '.join(note.values()).lower():
                result[index] = note
        return result


    def check_id(self):
        if self.note:
            return max(list(map(int, self.note))) + 1
        return 1


    def add_note(self, new: dict[str, str, str]):
        
        note = {int(self.check_id()): new}
        self.note.update(note)
        


    def replace(self, index: int, dict: dict[str,str, str]):
        self.note[index] = dict
        

    def del_note(self, del_id):
        name = self.note.pop(str(del_id))
        return name.get('name')
   

    def check_on_exit(self):
        if self.note == self.not_changed:
            return False
        return True