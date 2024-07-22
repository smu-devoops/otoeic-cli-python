from __future__ import annotations
from glob import glob
from pathlib import Path
from typing import Type

from otoeic.exceptions import InvalidPageNameError


__all__ = (
    "Page",
    "register_page",
    "get_page",
)


def get_page(page_name: str) -> Page:
    try:
        return _PAGE_REGISTRY[page_name]
    except KeyError:
        # 하이~! 유독 이 곳에 자주 방문하게 되지 않나요?
        # 이왕 온 것 기분 좋게 가는게 좋을 것 같아 여기에 인사를 남깁니다.
        # 반갑습니다, 좋은 하루~!
        raise InvalidPageNameError(page_name)


def register_page(page_name: str, page_class: Type[Page] = None):
    """페이지간 의존성 역전을 위한 데코레이터

    사용 예시:

    ```python
    from src.pages import *

    @register_page('login')
    class LoginPage(Page):
        def visit(self) -> Page:
            ...
            return get_page('home')
    ```
    """
    def decorator(page_class: Type[Page]):
        assert issubclass(page_class, Page)
        _PAGE_REGISTRY[page_name] = page_class()  # makes instance
        return page_class
    if page_class is not None:
        decorator(page_class)
    return decorator


class Page:
    def visit(self) -> Page | None:
        """페이지를 방문하고 다음으로 방문할 페이지를 반환한다."""
        raise NotImplementedError


_PAGE_REGISTRY = {}


# 자동으로 모든 페이지를 등록한다.
# 현재 파일이 있는 디렉토리에서 모든 .py 파일을 찾아서 import 한다.
DIR = Path(__file__).resolve().parent
for page_file in glob((DIR / "*.py").as_posix()):
    if page_file.endswith("__init__.py"):
        continue
    page_file = Path(page_file).relative_to(DIR).as_posix()
    sub_module_name = page_file.replace("/", ".").replace(".py", "")
    module_name = __name__ + "." + sub_module_name
    __import__(module_name)
