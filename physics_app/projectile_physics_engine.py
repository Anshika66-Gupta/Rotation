from MyImports import *

class Ball(Widget):
    def __init__(self, **kwargs):
        super(Ball, self).__init__(**kwargs)
        self.pos = (50, 100)
        self.size = (50, 50)
        self.touched_at = None
        self.velocity_unit_vector = Vector(0, 0)
        self.dummy_gravity_factor = 0

    @property
    def centre(self):
        half_size = tuple(x/2.0 for x in self.size)
        return tuple(sum(y) for y in zip(self.pos, half_size))

    def store_ball_position(self, ground, platform, *args):
        self.start_time = time()

    def is_ball_touched(self, ground, platform, *args):
        pos = args[1].pos
        return self.collide_point(*pos)

        
    def move_the_ball(self, ground, platform, app, *args, **event):
        Clock.schedule_interval(partial(self.move_ball_if_possible, ground, platform, app, event), INTERVAL)

    def move_ball_if_possible(self, ground, platform, app, *args):
        self.pos = self.calculate_new_pos()
        game = app.root.current_screen.projectileGame
        collision_occured = self.check_if_collision_occured()
        if collision_occured:
            Clock.schedule_once(partial(app.change_screen, 'formulascreen'), 2)
            game.draw_trajectory = True
            self.start_time = None
            self.velocity_unit_vector = Vector(0, 0)
        return not collision_occured

    def check_if_collision_occured(self, dummy_wid=None):
        app = App.get_running_app()
        game = app.root.current_screen.projectileGame
        if dummy_wid is None:
            return self.collide_widget(game.ground) or self.collide_widget(game.platform)
        else:
            return (game.ground.collide_point(*dummy_wid) or game.platform.collide_point(*dummy_wid))

    def calculate_new_pos(self, starting_pos=None):
        pos = starting_pos if starting_pos is not None else self.pos
        delta = tuple(x[0] * x[1] for x in zip(self.velocity_unit_vector, DELTA))
        return tuple(sum(x) for x in zip(pos, delta, self.gravity()))

    def gravity(self):
        try:
            return (0, G_FACTOR * (time() - self.start_time))
        except:
            self.dummy_gravity_factor = self.dummy_gravity_factor - TIME_DELTA
            return (0, self.dummy_gravity_factor)
