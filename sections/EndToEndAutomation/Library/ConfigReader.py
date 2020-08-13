import configparser

def readConfigData(section, Key):
    config = configparser.ConfigParser()
    config.read('./ConfigurationFiles/Config.cfg')
    return config.get(section,Key)



def fetchElementLocators(section, Key):
    config = configparser.ConfigParser()
    config.read('./ConfigurationFiles/Elements.cfg')
    return config.get(section,Key)
    