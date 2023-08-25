from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from Utility import config_file_utility

prop=config_file_utility.load_properties_file()

def getWebDriverInstance(webdriver_type):
    if webdriver_type == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif webdriver_type == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif webdriver_type == "chrome":
        driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif webdriver_type == "browserstack":
        options = ChromeOptions()
        options.browser_version = prop.get('BrowserStack', 'browser_version')
        options.platform_name = prop.get('BrowserStack', 'platform_name')
        bs_options = {}
        bs_options["project"] = prop.get('BrowserStack', 'project')
        bs_options["buildName"] = prop.get('BrowserStack', 'buildName')
        bs_options["w3c"] = prop.get('BrowserStack', 'w3c')
        options.set_capability('bs:options', bs_options)

        BTuserName=prop.get('BrowserStack', 'bs_username')
        BTpassword=prop.get('BrowserStack', 'bs_key')
        url = "https://" + BTuserName + ":" + BTpassword + "@hub.browserstack.com/wd/hub"
        driver = webdriver.Remote(command_executor=url,options=options,)


    elif webdriver_type == "lambdatest":
        options = ChromeOptions()
        options.browser_version = prop.get('LambdaTest', 'browser_version')
        options.platform_name = prop.get('LambdaTest', 'platform_name')
        lt_options = {}
        lt_options["project"] = prop.get('LambdaTest', 'project')
        lt_options["w3c"] = prop.get('LambdaTest', 'w3c')
        lt_options["plugin"] = prop.get('LambdaTest', 'plugin')
        options.set_capability('LT:Options', lt_options)
        LTuserName = prop.get('LambdaTest', 'lt_username')
        LTpassword = prop.get('LambdaTest', 'lt_key')
        gridUrl = prop.get('LambdaTest', 'gridUrl')
        url = "https://" + LTuserName + ":" + LTpassword + "@" + gridUrl
        driver = webdriver.Remote(command_executor=url, options=options, )
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    return driver
