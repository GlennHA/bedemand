import PySimpleGUI
import pyautogui
import time
import pyperclip


class Element:
    def __init__(self, name: str, tabs: int = 1):
        self.name = name
        self.tabs = tabs
        self.btn = PySimpleGUI.Button(button_text="x", key=lambda: pasteText(self))


def pasteText(element: Element) -> None:
    pyautogui.hotkey("alt", "tab")
    pyperclip.copy(element.btn.get_text())
    pyautogui.hotkey("ctrl", "v")


def getText(elements: list[Element]) -> None:
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.5)
    for element in elements:
        pyautogui.press(['tab'], presses=element.tabs)
        pyautogui.hotkey("ctrl", "c")
        s = pyperclip.paste()
        if "cpr" in element.name:
            s = s.replace('-', '')
        element.btn.update(text=s)


def nulstil(elements: list[Element]) -> None:
    for element in elements:
        element.btn.update(text='')


def main():
    kunde = [Element("Kunde cpr"),
             Element("Kunde fornavn", tabs=2),
             Element("Kunde efternavn"),
             Element("Kunde email"),
             Element("Kunde telefon"),
             Element("Kunde adresse"),
             Element("Kunde postnummer"),
             Element("Kunde by")]

    afdoede = [Element("Afdøde cpr"),
               Element("Afdøde fornavn", tabs=4),
               Element("Afdøde efternavn"),
               Element("Afdøde adresse", tabs=2),
               Element("Afdøde postnummer"),
               Element("Afdøde by"),
               Element("Afdøde død dato", tabs=2)]

    elements = []
    elements.extend([[PySimpleGUI.Button("Hent kunde", key=lambda: getText(kunde)),
                      PySimpleGUI.Button("Hent afdøde", key=lambda: getText(afdoede)),
                      PySimpleGUI.Button("Nulstil", key=lambda: nulstil(kunde + afdoede))]])
    elements.extend([[PySimpleGUI.HorizontalSeparator(color='dark blue')]])
    elements.extend([[PySimpleGUI.Text(element.name, size=18), element.btn] for element in kunde])
    elements.extend([[PySimpleGUI.HorizontalSeparator(color='dark blue')]])
    elements.extend([[PySimpleGUI.Text(element.name, size=18), element.btn] for element in afdoede])

    window = PySimpleGUI.Window(title="Hej Nette", layout=elements, keep_on_top=True)

    while True:
        event, _ = window.read() or (None, None)  # if None return tuple of None
        if event == PySimpleGUI.WIN_CLOSED:
            break
        elif callable(event):
            event()

    window.close()


if __name__ == "__main__":
    main()
