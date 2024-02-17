import GUI.Vedio
import GUI.first_page


class Controller():
    def __init__(self):
        pass

    def show_login(self):
        self.first_page = GUI.first_page.MainWindow()
        self.first_page.switch_window1.connect(self.show_main)
        self.first_page.switch_window2.connect(self.show_window_two)
        # self.first_page.switch_window2.connect(self.show_window_two)
        self.first_page.show()

    def show_main(self):
        self.window = GUI.Vedio.CameraPage()
        # self.window.switch_window.connect(self.show_window_two)
        self.first_page.close()
        self.window.show()


    def show_window_two(self):
        self.window_two = GUI.Vedio.VedioPage()
        self.first_page.close()
        self.window_two.show()