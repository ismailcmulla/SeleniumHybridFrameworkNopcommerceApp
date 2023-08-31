import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")   ## .\\ represents the current working directory cwd

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

