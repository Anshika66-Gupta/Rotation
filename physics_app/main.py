from MyImports import *

class GameScreen(Screen):
    projectileGame = ObjectProperty(None)

class FormulaScreen(Screen):
    pass

class PhysicsApp(App):

    screen_manager = None

    def build(self):
        print ('++++++', self.root)
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(GameScreen(name='gamescreen'))
        self.screen_manager.add_widget(FormulaScreen(name='formulascreen'))
        return self.screen_manager

    def change_screen(self, screen, *args, **kwargs):
        self.screen_manager.current = screen
        if self.screen_manager.current is not 'gamescreen':
            self.root.get_screen('gamescreen').projectileGame.ball.pos = (50, 100)
            Clock.schedule_once(partial(self.change_screen, 'gamescreen'), 2)


if __name__ == "__main__":
    app = PhysicsApp().run()
