def pytest_addoption(parser):
    parser.addoption(
        "-H", "--headless", action="store_true", default=False, help="run in headless mode"
    )
