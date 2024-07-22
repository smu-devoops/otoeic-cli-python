from textwrap import dedent


class ServiceException(Exception):
    """Base class for exceptions in this module."""
    pass


class InvalidPageNameError(ServiceException):
    """Raised when a page name is not registered."""

    def __init__(self, page_name: str):
        self.page_name = page_name
        super().__init__(dedent(f"""
            --------------------------------
            다음의 이름으로 등록된 페이지가 없습니다:
            '{page_name}'
            --------------------------------
            혹시 페이지를 등록하는 것을 잊지 않으셨나요?
            페이지 등록 방법 예시:
            --------------------------------
            from src.pages import *

            @register_page('{page_name}')
            class {page_name.capitalize()}Page(Page):
                def visit(self) -> Page:
                    ...
                    return get_page('home')

            --------------------------------
        """))


class UnauthorizedException(ServiceException):
    """Raised when a user is not authorized to perform an action."""

    def __init__(self):
        super().__init__(f"이 작업을 수행하기 위한 권한이 없습니다. 로그인 여부를 확인하세요.")


class AuthenticationFailedException(ServiceException):
    """Raised when a user fails to authenticate."""

    def __init__(self, username: str):
        super().__init__(f"사용자명 '{username}' 에 대한 인증이 실패했습니다.")
