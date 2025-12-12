from typing import Optional
from frontend.jinja_templates import templates

class ItemBrowserObjectButton:
    def __init__(self,
                 on_click_url: str,
                 name: str = "Unnamed item browser button",
                 hx_target: str = "this"
                 ):
        self.name: str = name
        self.on_click_url: str = on_click_url
        self.hx_target: str = on_click_url
        self.on_click_url: str = on_click_url
        self.hx_target: str = hx_target

class ItemBrowserObject:
    def __init__(self,
                 title: str = "No title provided",
                 on_click_url: Optional[str] = None,
                 ):
        self.title: str = title
        self.on_click_url: Optional[str] = on_click_url

class ItemBrowser:
    def __init__(self,
                 name: str = "Unnamed item browser",
                 refresh_url: Optional[str] = None,
                 toolbar_buttons: Optional[list[ItemBrowserObjectButton]] = [],
                 objects: Optional[list[ItemBrowserObject]] = [],
                 ):
        self.name: str = name

        self.refresh_url: str = refresh_url
        self.toolbar_buttons: list[ItemBrowserObjectButton] = toolbar_buttons

        self.objects: list[ItemBrowserObject] = objects

    def render(self):
        return templates.TeplateResponse("apps/elements/object_browser.j2", {"browser" : self})
