from otoeic import (
    __version__,
    __author__,
    __description__,
)
from otoeic.pages import *


@register_page('landing')
class LandingPage(Page):
    def visit(self) -> Page | None:
        print('=' * 64)
        print('오토익(OToeic)에 오신 것을 환영합니다!')
        print()
        print('{}'.format(__description__))
        print()
        print('Ver. {}'.format(__version__))
        print('By {}'.format(', '.join(__author__)))
        print('=' * 64)
        return get_page('login')
