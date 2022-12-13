class Logger:
    def __init__(self,  file_name) -> None:
        self.file_name = file_name
        f = open(file_name, 'w')
        f.close()

    def error(self, title, description):
        with open(self.file_name, 'a') as file:
            file.write('ERROR: ' + title + '-' + description + '\n')

    def info(self, title, description):
        with open(self.file_name, 'a') as file:
            file.write('INFO: ' + title + '-' + description + '\n')
