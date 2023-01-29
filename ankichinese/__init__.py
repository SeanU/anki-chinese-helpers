"""Add-on package initialization"""

from anki import hooks
import aqt
from aqt import mw
from aqt.utils import showInfo, qconnect
from aqt import qt


def onGeneratePinyin(browser: aqt.browser.Browser) -> None:
    noteids = browser.selectedNotes()

    # show a message box
    showInfo(f"Selected {len(noteids)} notes.")


def getNotesMenu(browser: aqt.browser.Browser) -> qt.QMenu:
    menus = [a.menu() for a in browser.menuBar().actions() if a.menu()]

    for menu in menus:
        if menu.title() == "&Notes":
            return menu


def setupMenu(browser: aqt.browser.Browser) -> None:
    action = qt.QAction("Generate Pinyin", browser)
    qconnect(action.triggered, lambda: onGeneratePinyin(browser))
    if notes := getNotesMenu(browser):
        notes.addSeparator()
        notes.addAction(action)


hooks.addHook("browser.setupMenus", setupMenu)
