import pytest


@pytest.fixture(scope="function")
def driver_get(request):
    from selenium import webdriver
    # web_driver = webdriver.Chrome(executable_path='lib\chromedriver.exe')
    # web_driver = webdriver.Firefox(executable_path='lib\geckodriver.exe')
    # web_driver = webdriver.Ie(executable_path='lib\IEDriverServer.exe')
    web_driver = webdriver.Ie(executable_path='lib\IEDriverServer32.exe')
    # session = request.node
    # for item in session.items:
    #     cls = item.getparent(pytest.Class)
    #     setattr(cls.obj, "driver", web_driver)
    cls = request.node.getparent(pytest.Class)
    setattr(cls.obj, "driver", web_driver)
    yield
    web_driver.close()