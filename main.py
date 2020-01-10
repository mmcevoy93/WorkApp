from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from Reader import Staff

def names(info):

    def callback1(instance):
        #This tells where the screen to go next
        name = instance.text
        layout.clear_widgets(children=None)
        foobar(info, name.split("\n")[0])

    layout = GridLayout(cols=2, spacing=20,padding = [10,10,10,10], size_hint_y=None)
    # Make sure the height is such that there is something to scroll.
    layout.bind(minimum_height=layout.setter('height'))

    green = [0.26, 0.71, 0.42,1]
    blue = [0.34, 0.47, 0.91, 1]
    red = [1.74,0,0.01, 1]
    yellow = [2.36, 1.85, 0.57, 1]
    for key, value in sorted(info.staff.items(), key=lambda e: int(e[1][2]), reverse=True):
        color = [1, 1, 1, 1]
        if info.staff[key][1]=="Slytherin": color = green
        if info.staff[key][1]=="Hufflepuff": color = yellow
        if info.staff[key][1]=="Ravenclaw": color = blue
        if info.staff[key][1]=="Gryffindor": color = red

        btn = Button(text=key + "\n" + info.staff[key][0]+"\n" + info.staff[key][1] + "\n" + info.staff[key][2],
                     size_hint_y=None,
                     halign="center",
                     height=80,
                     background_color=color)
        btn.bind(on_press=callback1)
        layout.add_widget(btn)
    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    root.add_widget(layout)
    runTouchApp(root)

def foobar(info, name):

    def callback1(instance):
        layout.clear_widgets(children=None)
        names(info)

    layout = GridLayout(cols=1,
                        spacing=20,padding = [10,10,10,10],
                        size_hint_y=None)
    btn = Button(text="Hello " + name + "\nYou have " + info.staff[name][2] + " points",
                 halign="center",)
    btn.bind(on_press=callback1)
    layout.add_widget(btn)

    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    root.add_widget(layout)
    runTouchApp(root)


if __name__ == '__main__':
    m = Staff('staff.csv')
    names(m)
