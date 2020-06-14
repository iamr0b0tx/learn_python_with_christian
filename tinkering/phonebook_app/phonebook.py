import json

class Phonebook:
    ''' A data structure to help manage names and phone numbers '''

    def __init__(self, backup_file_path='backup_file.json'):
        # the backup filepath
        self.BACKUP_FILE_PATH = backup_file_path

        # create the colections to store contacts in 
        self.contacts = {}

        # try to restore previous contacts
        self.restore()

    def backup(self):
        file_object = open(self.BACKUP_FILE_PATH, 'w')
        json.dump(self.contacts, file_object)
        file_object.close()

    def restore(self):
        ''' restore the contacts saved initially if backup file exists '''
        try:
            file_object = open(self.BACKUP_FILE_PATH, 'r')
            self.contacts.update(json.load(file_object))
            file_object.close()
        except FileNotFoundError:
            print('No backup file Available!')
