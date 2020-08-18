from selenium.webdriver import Chrome

# all, feature(context, feature), scenario(context, scenario), tag(context, tag)
def before_scenario(context,scenario):
    path = '../chromedriver.exe'
    context.driver = Chrome(executable_path = path)

def after_scenario(context,scenario):
    context.driver.close()

# Generate xml report
# behave -f allure_behave.formatter:AllureFormatter -o C:\Users\Ivan\Desktop\ironhack\selenium\SeleniumPython\sections\BDDAutomation