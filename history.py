import pickle
import os

HISTORY_FILE = "his.pkl"


class History:
    version = 1.0
    def __init__(self) -> None:
        self.watched = []

    def add_watched(self,name):
        if name not in self.watched:
            self.watched.append(name)
            self.watched = self.watched[-5:]
    
    def save(self):
        file = open(HISTORY_FILE, "wb")
        pickle.dump(self,file) 
        file.close()
    
    def display(self):
        if len(self.watched):
            print("Previously searched:")
            for watch in self.watched:
                print("\t"+watch)


def get_history():
    if os.path.isfile(HISTORY_FILE):
        file = open(HISTORY_FILE, "rb")
        history = pickle.load(file)
        file.close()
        if history.version == History.version:
            return history
        else:
            print("History version has changed, refreshing history")
            return History()
    else:
        return History()



