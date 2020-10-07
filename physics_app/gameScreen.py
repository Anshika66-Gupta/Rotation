from MyImports import *

class Ground(Widget):
    def __init__(self, **kwargs):
        super(Ground, self).__init__(**kwargs)
        self.pos = (0, 0)
        self.size = (Window.width, 20)

class Platform(Widget):
    def __init__(self, **kwargs):
        super(Platform, self).__init__(**kwargs)
        self.pos = (Window.width * (2.3 / 3.0), 20)
        self.size = (20, 20)

class Arrow(Widget):
    def __init__(self, **kwargs):
        super(Arrow, self).__init__(**kwargs)
        self._points = ()

    @property
    def points(self):
        return self._points

class ProjectileGame(FloatLayout):
    ground = ObjectProperty(None)
    ball = ObjectProperty(None)
    platform = ObjectProperty(None) 
    arrow = ObjectProperty(None)
    line_instruction = Instruction()
    line_instruction_group = InstructionGroup()
    draw_trajectory = False

    def save_pos_if_ball_touched(self, *args):
        pos = args[1].pos
        if self.ball.collide_point(*pos):
            self.ball.touch_pos = pos

    def show_arrow_if_ball_was_touched(self, *touch):
        ball_touched_at = self.ball.touch_pos
        if ball_touched_at:
            self.draw_arrow(ball_touched_at, touch, self.ball.centre)

    def draw_arrow(self, ball_touched_at, touch, ball_centre):
        app = App.get_running_app()
        present_touch = touch[1].pos
        touch_vector = Vector(*present_touch) - Vector(*ball_touched_at)
        touch_vector_inversed = touch_vector.inverse()
        arrow_length_vector = unit_vector(touch_vector_inversed.norm(), touch_vector_inversed.argument())
        self.ball.velocity_unit_vector = arrow_length_vector
        arrow_ending_vector = arrow_length_vector + ball_centre
        game = app.screen_manager.current_screen.projectileGame
        line_points = (ball_centre, arrow_ending_vector.values)
        self.line_instruction = Line(points=line_points, group='arrows')
        self.arrow.canvas.clear()
        if not game.draw_trajectory:
            self.arrow.canvas.add(self.line_instruction)
        self.ball.dummy_gravity_factor = 0
        if game.draw_trajectory:
            ball_trajectory_points = []
            next_pos = self.ball.calculate_new_pos(ball_centre)
            while not game.ball.check_if_collision_occured(next_pos):
                next_pos = self.ball.calculate_new_pos(next_pos)
                ball_trajectory_points.append(next_pos)
            with self.arrow.canvas:
                    for point in ball_trajectory_points:
                    	Ellipse(pos=point, size=(2, 2))

    def remove_arrow_and_kick_if_ball_was_touched(self, ground, platform, app, *touch):
        self.ball.touch_pos = ()
        self.arrow.canvas.clear()
        self.ball.store_ball_position(ground, platform, app, touch)
        self.ball.move_the_ball(ground, platform, app, touch)
