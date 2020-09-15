import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.uix.popup import Popup
from kivy.uix.behaviors import ButtonBehavior

class GameScreen(GridLayout):
    count = 1
    Nought = "Nought.png"
    Cross = "Cross.png"
    Default = "Default.png"
    btn_dict = {}
    winner = ''
    win_dict = { '0': [], '1': []}
    win_cons = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
                    ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
                    ['1', '5', '9'], ['3', '5', '7']]
    btn_1 = ObjectProperty(None)
    btn_2 = ObjectProperty(None)
    btn_3 = ObjectProperty(None)
    btn_4 = ObjectProperty(None)
    btn_5 = ObjectProperty(None)
    btn_6 = ObjectProperty(None)
    btn_7 = ObjectProperty(None)
    btn_8 = ObjectProperty(None)
    btn_9 = ObjectProperty(None)

    def ToggleUser(self):
        if self.count == 1:
            self.count = self.count * -1
        else:
            self.count = self.count * -1

    def ButtonVerify(self, btn):
        if btn in self.btn_dict:
            return True
        else:
            return False

    def Pressed(self, btn):
        if btn not in self.btn_dict:
            self.btn_dict[btn] = ""
            print(self.btn_dict[btn])
        else:
            pass
        self.Winning_Conditions()


    def Down(self, btn):
        btn.state = 'down'
        return btn.state

    # Image functions:

    def DefaultImage(self):
        return self.Default

    def NoughtsImage(self):
        return self.Nought

    def CrossesImage(self):
        return self.Cross

    def ChangeImage(self, btn):
        if not self.ButtonVerify(btn):
            if self.count == 1:
                self.btn_dict[btn] = self.NoughtsImage()
                self.win_dict['0'].append(btn.text)
                self.ToggleUser()
                return self.btn_dict[btn]
            elif self.count == -1:
                self.btn_dict[btn] = self.CrossesImage()
                self.win_dict['1'].append(btn.text)
                self.ToggleUser()
                return self.btn_dict[btn]
            else:
                return self.DefaultImage()
        else:
            return self.btn_dict[btn]

    # Winning Conditions:

    def Noughts_Win(self):
        for con in self.win_cons:
            if(all(x in self.win_dict['0'] for x in con)):
                return True
        return False

    def Crosses_Win(self):
        for con in self.win_cons:
            if(all(x in self.win_dict['1'] for x in con)):
                return True
        return False

    def Winning_Conditions(self):
        if self.Noughts_Win():
            self.winner = 'Noughts'
            self.show_popup(P1)
        elif self.Crosses_Win():
            self.winner = 'Crosses'
            self.show_popup(P2)
        elif len(self.btn_dict) == 9:
            self.show_popup(P3)
        else:
            return False

    # Popups:

    def show_popup(self, classname):
        show = classname() # Create a new instance of the P class

        popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None), size=(400,400))
        # Create the popup window

        popupWindow.open() # show the popup


class P1(FloatLayout):
    winner = 'Noughts'

class P2(FloatLayout):
    winner = 'Crosses'

class P3(FloatLayout):
    pass

class game(App):
    def build(self):
        return GameScreen()

if __name__=='__main__':
    game().run()
