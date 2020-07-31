'''try:
    input1 = input('Please enter a number : ')
    input2 = input('Please enter one more number : ')
    c = int(input1) + int(input2)
    print(c)
except:
    print('Your input is incorrect, please enter correct data')

finally:
    print('This code i want to execute always at the end')'''

from configparser import ConfigParser

# created object of configparser calss
config = ConfigParser()

# to read data from config file
config.read('./Config.cfg')

print(config.get('Section1','username'))