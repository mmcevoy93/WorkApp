from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.base import EventLoop
from Reader import Staff
from Reader import Duties
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.textinput import TextInput
import os


def title_screen():
    def go_to_task(instance):
        titlecard.clear_widgets(children=None)
        duties(Duties("maintenance.csv"), instance.text.split(' ')[0].lower())

    def go_to_addstaff(instance):
        titlecard.clear_widgets(children=None)
        add_staff_to_file(Staff('staff.csv'))

    def go_to_locker(instance):
        titlecard.clear_widgets(children=None)
        lockers()
    def hook_keyboard(window, key, *largs):
        if key == 27:
            exit()
    EventLoop.window.bind(on_keyboard=hook_keyboard)

    intro = AnchorLayout(anchor_x='center', anchor_y='top',size_hint=(1,0.3))
    title = Label(text="Welcome Please pick an option",
                  halign="center",
                  valign="center",
                  size_hint=(1,1))
    intro.add_widget(title)

    taskbuttons = BoxLayout(padding = [50,50,50,50], spacing = 20,orientation='vertical')
    daily = Button(text="Daily Maintenance",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    daily.bind(on_press=go_to_task)

    weekly = Button(text="Weekly Maintenance",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    weekly.bind(on_press=go_to_task)

    assigned = Button(text="Assigned Checklists",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    lockers1 = Button(text="Locker Entries",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    lockers1.bind(on_press=go_to_locker)

    add_staff = Button(text="Add Staff Member",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    add_staff.bind(on_press=go_to_addstaff)
    taskbuttons.add_widget(daily)
    taskbuttons.add_widget(weekly)
    taskbuttons.add_widget(assigned)
    taskbuttons.add_widget(lockers1)
    taskbuttons.add_widget(add_staff)
    titlecard = BoxLayout(orientation='vertical')
    titlecard.add_widget(intro)
    titlecard.add_widget(taskbuttons)



    runTouchApp(titlecard)

def lockers():
    def go_to_names(instance):
        #This tells where the screen to go next
        lockercard.clear_widgets(children=None)
        names(Staff('staff.csv'),3)
        pass

    def hook_keyboard(window, key, *largs):
        if key == 27:
            lockercard.clear_widgets(children=None)
            title_screen()
    EventLoop.window.bind(on_keyboard=hook_keyboard)

    page = AnchorLayout(anchor_x='center', anchor_y='top',size_hint=(1,0.3))
    title = Label(text="Where is the locker located?\n3 points per locker",
                  halign="center",
                  valign="center",
                  size_hint=(1,1))
    page.add_widget(title)

    lockerbuttons = BoxLayout(padding = [50,50,50,50], spacing = 20,orientation='vertical')
    menWet = Button(text="Men's Wet Change Room",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    menWet.bind(on_release=go_to_names)
    womenWet = Button(text="Women's Wet Change Room",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))

    womenWet.bind(on_press=go_to_names)
    menDry = Button(text="Men's Dry Change Room",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    menDry.bind(on_press=go_to_names)
    womenDry = Button(text="Women's Dry Change Room",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    womenDry.bind(on_press=go_to_names)
    lobby = Button(text="Front Desk",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    lobby.bind(on_press=go_to_names)
    fieldhouse = Button(text="Fieldhouse",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    fieldhouse.bind(on_press=go_to_names)
    gym = Button(text="Gym",
                halign="center",
                valign="center",
                size_hint=(1, 0.3))
    gym.bind(on_press=go_to_names)
    lockerbuttons.add_widget(menWet)
    lockerbuttons.add_widget(menDry)
    lockerbuttons.add_widget(womenWet)
    lockerbuttons.add_widget(womenDry)
    lockerbuttons.add_widget(lobby)
    lockerbuttons.add_widget(gym)

    lockercard = BoxLayout(orientation='vertical')
    lockercard.add_widget(page)
    lockercard.add_widget(lockerbuttons)
    runTouchApp(lockercard)

def duties(info, type):

    def go_to_names(instance):
        #This tells where the screen to go next
        layout.clear_widgets(children=None)
        names(Staff('staff.csv'), instance.text.split("\n")[2])
        pass
    def hook_keyboard(window, key, *largs):
        if key == 27:
            layout.clear_widgets(children=None)
            title_screen()
    EventLoop.window.bind(on_keyboard=hook_keyboard)

    layout = GridLayout(cols=1, spacing=20,padding = [10,10,10,10], size_hint_y=None)
    # Make sure the height is such that there is something to scroll.
    layout.bind(minimum_height=layout.setter('height'))
    color = [0.26, 0.71, 0.42,1]
    green = [0.26, 0.71, 0.42,1]
    red = [1.74,0,0.01, 1]
    for key in info.tasks:
        if info.tasks[key][0] == type:
            btn = Button(text=key+"\n\n"+info.tasks[key][1]+"\npoints",
                         text_size=(1000,None),
                         size_hint_y=None,
                         halign="center",
                         height=400,
                         background_color=color)
            btn.bind(on_press=go_to_names)
            layout.add_widget(btn)


    root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
    root.add_widget(layout)
    runTouchApp(root)

def add_staff_to_file(info):

    def displayname(instance):
        if((not staff_name.text) or (not staff_position.text) or (not staff_points.text)):
            pass
        else:
            topbottom.clear_widgets()
            info.add_staff(staff_name.text, staff_position.text, instance.text, staff_points.text)
            title_screen()
    def hook_keyboard(window, key, *largs):
        if key == 27:
            topbottom.clear_widgets()
            title_screen()
    EventLoop.window.bind(on_keyboard=hook_keyboard)

    topbottom = BoxLayout(orientation='vertical')

    top_layout = GridLayout(cols = 2,
                        spacing = 20,
                        padding = [10, 10, 10, 10])
    lbl1 = Label(text="Staff name")
    staff_name = TextInput(multiline=False,
                           input_filter=None)


    lbl2 = Label(text="Position")
    staff_position = TextInput(multiline=False,
                             input_filter=None)

    lbl3 = Label(text="Initial points")
    staff_points = TextInput(multiline=False,
                             input_filter="int")

    top_layout.add_widget(lbl1)
    top_layout.add_widget(staff_name)
    top_layout.add_widget(lbl2)
    top_layout.add_widget(staff_position)
    top_layout.add_widget(lbl3)
    top_layout.add_widget(staff_points)

    bottom_layout = GridLayout(cols = 5,
                        spacing = 20,
                        padding = [10, 10, 10, 10])
    slytherin = Button(text="Slytherin")
    slytherin.bind(on_press=displayname)
    gryffindor = Button(text="Gryffindor")
    gryffindor.bind(on_press=displayname)
    hufflepuff = Button(text="Hufflepuff")
    hufflepuff.bind(on_press=displayname)
    ravenclaw = Button(text="Ravenclaw")
    ravenclaw.bind(on_press=displayname)
    oof = Button(text="Out of Facility")
    ravenclaw.bind(on_press=displayname)

    bottom_layout.add_widget(slytherin)
    bottom_layout.add_widget(gryffindor)
    bottom_layout.add_widget(hufflepuff)
    bottom_layout.add_widget(ravenclaw)
    bottom_layout.add_widget(oof)


    topbottom.add_widget(top_layout)
    topbottom.add_widget(bottom_layout)

    runTouchApp(topbottom)

def names(info, points):
    def hook_keyboard(window, key, *largs):
        if key == 27:
            layout.clear_widgets(children=None)
            title_screen()
    EventLoop.window.bind(on_keyboard=hook_keyboard)

    def points_added(instance):
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
    grey = [2.2, 2.2, 2.2, 1]
    for key, value in sorted(info.staff.items(), key=lambda e: int(e[1][2]), reverse=True):
        color = [1, 1, 1, 1]
        if info.staff[key][1]=="Slytherin": color = green
        if info.staff[key][1]=="Hufflepuff": color = yellow
        if info.staff[key][1]=="Ravenclaw": color = blue
        if info.staff[key][1]=="Gryffindor": color = red
        if info.staff[key][1]=="Out of Facility": color = grey

        btn = Button(text=key + "\n" + info.staff[key][0]+"\n" + info.staff[key][1] + "\n" + info.staff[key][2],
                     size_hint_y=None,
                     halign="center",
                     height=400,
                     background_color=color)
        btn.bind(on_press=points_added)
        layout.add_widget(btn)

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
    #add_staff_to_file(m)
