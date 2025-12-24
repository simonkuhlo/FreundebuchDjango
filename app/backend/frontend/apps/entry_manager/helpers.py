from frontend.utils.item_browser import ItemBrowser, ItemBrowserObjectButton, ItemBrowserObject
from crud.crud_entry import handler as entry_crud


def get_entry_browser() -> ItemBrowser:
    browser: ItemBrowser = ItemBrowser(
        name="Entry browser",
        refresh_url="/admin/entry_manager/browser",
        toolbar_buttons=[
            ItemBrowserObjectButton(
                on_click_url="/admin/entry_manager/browser/create_collection",
                name="+ New Entry",
                hx_target="closest .browser_frame",
                hx_swap="outerHTML"
            )
        ]
    )
    entries = entry_crud.list()
    browser.objects = []
    for entry in entries:
        browser.objects.append(
            ItemBrowserObject(
                title=f"{entry.id}",
                on_click_url=f"/admin/entry_manager/editor/{entry.id}",
            )
        )
    return browser