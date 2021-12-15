from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.title("QR Code Generator & Scanner")
window.geometry("1152x700")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    487.0,
    700.0,
    fill="#C4C4C4",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    243.0,
    350.0,
    image=image_image_1
)

canvas.create_text(
    715.0,
    65.0,
    anchor="nw",
    text="QR CODE",
    fill="#591E22",
    font=("Roboto Bold", 50 * -1)
)

canvas.create_text(
    740.0,
    617.0,
    anchor="nw",
    text="Made by Kumar Anurag",
    fill="#000000",
    font=("Roboto Bold", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    818.5,
    223.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E8E5E5",
    highlightthickness=0
)
entry_1.place(
    x=603.0,
    y=182.0+30,
    width=431.0,
    height=50.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    818.5,
    406.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#E8E5E5",
    highlightthickness=0
)
entry_2.place(
    x=603.0-3,
    y=365.0+40,
    width=431.0,
    height=40.0
)

canvas.create_text(
    598.0,
    191.0,
    anchor="nw",
    text="Content to Encrypt",
    fill="#591E22",
    font=("Roboto Bold", 15 * -1)
)

canvas.create_text(
    598.0,
    374.0,
    anchor="nw",
    text="Scanned Content",
    fill="#591E22",
    font=("Roboto Bold", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=738.0,
    y=286.0,
    width=161.0,
    height=49.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=738.0,
    y=469.0,
    width=161.0,
    height=49.0
)
window.resizable(False, False)
window.mainloop()
