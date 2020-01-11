from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from Reader import Staff
from Reader import Duties
from kivy.uix.tabbedpanel import TabbedPanel
import os


def title_screen():
    def go_to_daily(instance):
        titlecard.clear_widgets(children=None)
        duties(Duties("maintenance.csv"))

    intro = AnchorLayout(anchor_x='center', anchor_y='top',size_hint=(1,0.3))
    title = Label(text="Welcome Please pick an option",
                  halign="center",
                  valign="center",
                  size_hint=(1,1))
    intro.add_widget(title)

    taskbuttons = BoxLayout(padding = [50,50,50,50], spacing = 20)
    daily = Button(text="Daily Maintenance",
                halign="center",
                valign="center",
                size_hint=(0.3,1))
    daily.bind(on_press=go_to_daily)

    weekly = Button(text="Weekly Maintenance",
                halign="center",
                valign="center",
                size_hint=(0.3,1))
    assigned = Button(text="Assigned Checklists",
                halign="center",
                valign="center",
                size_hint=(0.3,1))
    lockers = Button(text="Locker Entries",
                halign="center",
                valign="center",
                size_hint=(0.3,1))
    taskbuttons.add_widget(daily)
    taskbuttons.add_widget(weekly)
    taskbuttons.add_widget(assigned)
    taskbuttons.add_widget(lockers)

    titlecard = BoxLayout(orientation='vertical')

    titlecard.add_widget(intro)
    titlecard.add_widget(taskbuttons)
    runTouchApp(titlecard)


def duties(info):

    def go_to_names(instance):
        #This tells where the screen to go next
        layout.clear_widgets(children=None)
        names(Staff('staff.csv'), instance.text.split("\n")[2])
        pass

    layout = GridLayout(cols=4, spacing=20,padding = [10,10,10,10], size_hint_y=None)
    # Make sure the height is such that there is something to scroll.
    layout.bind(minimum_height=layout.setter('height'))
    for key in info.tasks:
        color = [0.26, 0.71, 0.42,1]
        btn = Button(text=key+"\n\n"+info.tasks[key][1]+"\npoints",
                     text_size=(layout.width, None),
                     size_hint_y=None,
                     halign="center",
                     height=400,
                     background_color=color)
        btn.bind(on_press=go_to_names)
        layout.add_widget(btn)


    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    root.add_widget(layout)
    runTouchApp(root)



def names(info, points):

    def callback1(instance):
        #This tells where the screen to go next
        name = instance.text
        layout.clear_widgets(children=None)
        info.add_points(name.split("\n")[0], int(points))
        title_screen()

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
                     height=400,
                     background_color=color)
        btn.bind(on_press=callback1)
        layout.add_widget(btn)
    add_staff = Button(text="Add a Staff Member",
                       size_hint_y=None,
                       halign="center",
                       height=400,
                       background_color=[1, 1, 1, 1])
    add_staff.bind(on_press=callback1)
    layout.add_widget(add_staff)
    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    root.add_widget(layout)
    runTouchApp(root)

def foobar(info, name):

    def callback1(instance):
        layout.clear_widgets(children=None)
        duties(Duties('maintenance.csv'))

    layout = AnchorLayout(padding = [50,50,50,50], anchor_x='center', anchor_y='center')
    btn = Button(text="Hello " + name + "\nYou have " + info.staff[name][2] + " points",
                 halign="center")

    btn.bind(on_press=callback1)
    layout.add_widget(btn)

    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    root.add_widget(layout)
    runTouchApp(root)


if __name__ == '__main__':
    #/storage/emulated/0/kivy/
    #in final version store saved data there and reference it to that location
    m = Staff('staff.csv')
    #names(m)
    n = Duties('maintenance.csv')
    #duties(n)
    title_screen()
