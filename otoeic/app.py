from otoeic.pages import get_page


class Application:
    def run(self):
        page = get_page('landing')
        while page is not None:
            page = page.visit()
