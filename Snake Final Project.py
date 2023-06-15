import random
import arcade

window_width = 600
window_length = 800
map_width = 6000
map_length = 8000
coin_size = 0.1
coin_amt = 5000
snake_size = 0.03
start_x_coordinate = 500
start_y_coordinate = 500
wall_size = 0.25
times_2_amt = 100
times_5_amt = 20
speedup_amt = 50
invincible_amt = 30
power_size = 0.25


class Times_2(arcade.Sprite):
    def update(self):
        self.center_y -= 0
class Times_5(arcade.Sprite):
    def update(self):
        self.center_y -= 0
class Speedup(arcade.Sprite):
    def update(self):
        self.center_y -= 0
class Self_invincible(arcade.Sprite):
    def update(self):
        self.center_y -= 0
class Coin(arcade.Sprite):

    def update(self):
        self.center_y -= 0



class Snake(arcade.Sprite):
    def update(self):
        self.center_y += 0
        self.center_x += 0

class Game(arcade.Window):
    def __init__(self, width, height, name):

        super().__init__(width, height, name)

        arcade.set_background_color(arcade.color.ASH_GREY)
        self.camera_for_sprites = arcade.Camera(window_length, window_width)
        self.camera_for_gui = arcade.Camera(window_length, window_width)
        self.speed = 10
        self.point = 0
        self.multiple = 1
        self.point_change = 0
        self.growth_factor = 3
        self.snake_dx = 1
        self.snake_dy = 0
        self.snake_length = 5


    def setup(self):

      self.snake_list = arcade.SpriteList()
      self.body_list = arcade.SpriteList()
      self.body_dummy_list = arcade.SpriteList()
      self.coin_list = arcade.SpriteList()
      self.wall_list = arcade.SpriteList()
      self.times_2_list = arcade.SpriteList()
      self.times_5_list = arcade.SpriteList()
      self.invincible_list = arcade.SpriteList()
      self.speedup_list = arcade.SpriteList()
      self.player = arcade.Sprite("Snake.png", snake_size)
      self.player.center_x = start_x_coordinate
      self.player.center_y = start_y_coordinate
      self.glob = 0
      self.player_prev_pos_x = []
      self.player_prev_pos_y = []
      for i in range(self.snake_length):
          self.player_prev_pos_x.append(start_x_coordinate)
          self.player_prev_pos_y.append(start_y_coordinate)
      self.wall_hit_list = []
      self.self_hit_list = []
      self.snake_list.append(self.player)
      self.times_2_bool = 0
      self.times_5_bool = 0
      self.speedup_bool = 0
      self.invincible_bool = 0
      self.times_2_glob = 0
      self.times_5_glob = 0
      self.speedup_glob = 0
      self.invincible_glob = 0
      self.physics_engine_list = []
      self.coin_sound_player = None
      self.coin_sound = arcade.load_sound(":resources:sounds/coin5.wav")
      self.power_sound = arcade.load_sound(":resources:sounds/coin3.wav")
      self.power_sound_player = None


      for i in range(self.snake_length - 1):
          self.snake = Snake("Snake.png", snake_size)
          self.snake.center_x = start_x_coordinate
          self.snake.center_y = start_y_coordinate
          self.body_list.append(self.snake)

      for i in range(coin_amt):
          coin = Coin("coin_01.png", coin_size)
          coin.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
          coin.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
          self.coin_list.append(coin)

      for i in range(times_2_amt):
          times_2 = Times_2("times_2.png", power_size)
          times_2.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
          times_2.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
          self.times_2_list.append(times_2)

      for i in range(times_5_amt):
          times_5 = Times_5("times_5.png", power_size)
          times_5.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
          times_5.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
          self.times_5_list.append(times_5)

      for i in range(speedup_amt):
          speedup = Times_5("speedup.png", power_size)
          speedup.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
          speedup.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
          self.speedup_list.append(speedup)

      for i in range(invincible_amt):
          self_invincible = Times_5("self_invincible.png", power_size)
          self_invincible.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
          self_invincible.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
          self.invincible_list.append(self_invincible)


      for i in range (round(map_length / (128 * wall_size))):
          wall = arcade.Sprite("sandHalf_mid.png", wall_size)
          wall.center_x = map_length * (-0.5) + ((128 * wall_size) * i)
          wall.center_y = map_width * (0.5)
          self.wall_list.append(wall)

      for i in range (round(map_length / (128 * wall_size))):
          wall = arcade.Sprite("sandHalf_mid.png", wall_size)
          wall.center_x = map_length * (-0.5) + ((128 * wall_size) * i)
          wall.center_y = map_width * (-0.5)
          self.wall_list.append(wall)

      for i in range(round(map_width / (128 * wall_size))):
          wall = arcade.Sprite("sandHalf_mid_vert.png", wall_size)
          wall.center_x = map_length * (-0.5)
          wall.center_y = map_width * (-0.5) + ((128 * wall_size) * i)
          self.wall_list.append(wall)
      for i in range(round(map_width / (128 * wall_size))):
          wall = arcade.Sprite("sandHalf_mid_vert.png", wall_size)
          wall.center_x = map_length * (0.5)
          wall.center_y = map_width * (-0.5) + ((128 * wall_size) * i)
          self.wall_list.append(wall)

      self.physics_engine1 = arcade.PhysicsEngineSimple(self.player, self.wall_list)
      for snake in self.body_list:
          self.physics_engine_list.append(arcade.PhysicsEngineSimple(snake, self.wall_list))



    def on_draw(self):
        arcade.start_render()
        self.camera_for_sprites.use()
        self.coin_list.draw()
        self.snake_list.draw()
        self.times_2_list.draw()
        self.times_5_list.draw()
        self.speedup_list.draw()
        self.invincible_list.draw()
        self.body_list.draw()
        self.wall_list.draw()
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.point}", 10, 20, arcade.color.WHITE, 14)
        if ((len(self.wall_hit_list) > 0 or (len(self.self_hit_list) > 0 and self.invincible_bool == 0)) and self.glob > 100):
            self.snake_dx = 0
            self.snake_dy = 0
            arcade.draw_lrtb_rectangle_filled(0, window_length, window_width, 0, arcade.color.AIR_SUPERIORITY_BLUE)
            arcade.draw_text(f"Game Over", 240, 400, arcade.color.WHITE, 50)
            arcade.draw_text(f"You Got " + str(self.point) + " points", 150, 150, arcade.color.WHITE, 50)
            arcade.finish_render()


    def on_key_press(self, key, modifiers):
            if key == arcade.key.UP:
                self.snake_dx = 0
                self.snake_dy = 1

            elif key == arcade.key.DOWN:
                self.snake_dx = 0
                self.snake_dy = -1

            elif key == arcade.key.RIGHT:
                self.snake_dx = 1
                self.snake_dy = 0

            elif key == arcade.key.LEFT:
                self.snake_dx = -1
                self.snake_dy = 0



    def update(self, delta_time):
        self.physics_engine1.update()
        for engine in self.physics_engine_list:
            engine.update()

        i = -1
        self.player.center_x += self.snake_dx * self.speed
        self.player.center_y += self.snake_dy * self.speed
        for self.snake in self.body_list:

            self.snake.center_x = self.player_prev_pos_x[i]
            self.snake.center_y = self.player_prev_pos_y[i]

            i -= 1
        self.player_prev_pos_x.append(self.player_prev_pos_x[-1] + self.snake_dx * self.speed)
        self.player_prev_pos_y.append(self.player_prev_pos_y[-1] + self.snake_dy * self.speed)
        CAMERA_SPEED = 1
        lower_left_corner = (self.player.center_x - self.width / 2,
                             self.player.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)


        self.coin_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)

        for coin in hit_list:
            if not self.coin_sound_player or not self.coin_sound_player.playing:
                self.coin_sound_player = arcade.play_sound(self.coin_sound)
            coin.remove_from_sprite_lists()
        for i in range(len(hit_list)):
            coin = Coin("coin_01.png", coin_size)
            coin.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
            coin.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
            self.coin_list.append(coin)

        self.point_change = len(hit_list) * self.multiple
        self.point += self.point_change

        self.snake_length += self.point_change * self.growth_factor
        for i in range(self.point_change * self.growth_factor):
            self.snake = Snake("Snake.png", snake_size)
            self.snake.center_x = start_x_coordinate
            self.snake.center_y = start_y_coordinate
            self.body_list.append(self.snake)
            self.body_dummy_list.append(self.snake)
        for i in range(self.point_change * self.growth_factor):
            self.player_prev_pos_x.insert(0, start_x_coordinate)
            self.player_prev_pos_y.insert(0, start_y_coordinate)
        self.wall_hit_list = arcade.check_for_collision_with_list(self.player, self.wall_list)


        self.self_hit_list = arcade.check_for_collision_with_list(self.player, self.body_dummy_list)
        self.glob += 1

        times_2_obtain = arcade.check_for_collision_with_list(self.player, self.times_2_list)
        for times_2 in times_2_obtain:
            if not self.power_sound_player or not self.power_sound_player.playing:
                self.power_sound_player = arcade.play_sound(self.power_sound)
            self.times_2_bool = 1
            times_2.remove_from_sprite_lists()
        for i in range(len(times_2_obtain)):
            times_2 = Times_2("times_2.png", power_size)
            times_2.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
            times_2.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
            self.coin_list.append(times_2)

        times_5_obtain = arcade.check_for_collision_with_list(self.player, self.times_5_list)
        for times_5 in times_5_obtain:
            if not self.power_sound_player or not self.power_sound_player.playing:
                self.power_sound_player = arcade.play_sound(self.power_sound)
            self.times_5_bool = 1
            times_5.remove_from_sprite_lists()
        for i in range(len(times_5_obtain)):
            if not self.power_sound_player or not self.power_sound_player.playing:
                self.power_sound_player = arcade.play_sound(self.power_sound)
            times_5 = Times_5("times_5.png", power_size)
            times_5.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
            times_5.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
            self.coin_list.append(times_5)

        invincible_obtain = arcade.check_for_collision_with_list(self.player, self.invincible_list)
        for self_invincible in invincible_obtain:
            if not self.power_sound_player or not self.power_sound_player.playing:
                self.power_sound_player = arcade.play_sound(self.power_sound)
            self.invincible_bool = 1
            self_invincible.remove_from_sprite_lists()
        for i in range(len(invincible_obtain)):
            self_invincible = Self_invincible("self_invincible.png", power_size)
            self_invincible.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
            self_invincible.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
            self.coin_list.append(self_invincible)

        speedup_obtain = arcade.check_for_collision_with_list(self.player, self.speedup_list)
        for speedup in speedup_obtain:
            if not self.power_sound_player or not self.power_sound_player.playing:
                self.power_sound_player = arcade.play_sound(self.power_sound)
            self.speedup_bool = 1
            speedup.remove_from_sprite_lists()
        for i in range(len(speedup_obtain)):
            speedup = Speedup("speedup.png", power_size)
            speedup.center_x = random.randrange(round((map_length / -2) + 20), round((map_length / 2) - 20))
            speedup.center_y = random.randrange(round((map_width / -2) + 20), round((map_width / 2) - 20))
            self.coin_list.append(speedup)



        if self.times_5_bool == 1 and (self.glob - self.times_5_glob) < 600:
            self.multiple = 5
        elif self.times_2_bool == 1 and (self.glob - self.times_2_glob) < 500:
            self.multiple = 2
        else:
            self.multiple = 1
        if self.speedup_bool == 1 and (self.glob - self.speedup_glob) < 700:
            self.speed = 15
        else:
            self.speed = 10
        if  self.invincible_bool == 1 and not (self.glob - self.speedup_glob) < 500:
            self.invincible_bool = 0

def main():
    window = Game(window_length, window_width, "Game")
    window.setup()
    arcade.run()

main()







