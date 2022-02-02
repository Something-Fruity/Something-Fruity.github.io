"""Set up the chrome webdriver to be used in the behave tests"""
import threading

from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from flaskr.app import create_app


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")


# pylint: disable=unused-argument
def before_scenario(context, scenario):
    """Initialize the web driver, server and app"""
    context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
    context.server.set_app(create_app(config='config.TestConfig'))
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    context.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_scenario(context, scenario):
    """Tear down the browser and server"""
    context.browser.quit()
    context.server.shutdown()
    context.pa_app.join()
