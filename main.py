from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
import math
import random

class FlappyNeonWidget(Widget):
    def __init__(self, **kwargs):
        super(FlappyNeonWidget, self).__init__(**kwargs)
        
        self.animation_time = 0.0
        self.game_initialized = False
        
        # Bird settings
        self.bird_x = 150
        self.bird_y = 300
        self.bird_vy = 0.0
        self.bird_radius = 16
        
        # --- FLEXIBLE LONG TAIL PROPERTIES ---
        self.tail_history = []
        self.max_tail_segments = 25  
        
        # Smooth controls tuning
        self.gravity = -0.45        
        self.flap_strength = 7.0    
        self.is_pressing = False    
        
        # Pipes engine structural data
        self.pipes = []
        self.pipe_width = 70
        self.pipe_gap = 240         
        self.base_pipe_speed = 3.8 
        self.spawn_timer = 0
        self.last_gap_y = None      
        
        # Game State properties
        self.score = 0
        self.game_over = False
        
        # Initialize primary master logic execution loop
        Clock.schedule_interval(self.update_game, 1/60.0)

    def init_game_metrics(self):
        curr_h = self.height if self.height > 100 else Window.height
        
        self.bird_y = curr_h / 2
        self.bird_vy = 0
        self.pipes = []
        self.spawn_timer = 0
        self.score = 0
        self.game_over = False
        self.last_gap_y = curr_h / 2 - (self.pipe_gap / 2)
        
        # Reset tail positions with clean tracking coordinates
        self.tail_history = []
        for _ in range(self.max_tail_segments):
            self.tail_history.append((self.bird_x, self.bird_y))
            
        self.game_initialized = True

    def spawn_pipe(self):
        curr_w = self.width if self.width > 100 else Window.width
        curr_h = self.height if self.height > 100 else Window.height
        
        min_y = 60
        max_y = curr_h - 60 - self.pipe_gap
        
        if self.last_gap_y is not None:
            low_bound = max(min_y, self.last_gap_y - 180)
            high_bound = min(max_y, self.last_gap_y + 180)
            gap_y = random.uniform(low_bound, high_bound)
        else:
            gap_y = random.uniform(min_y, max_y)
            
        self.last_gap_y = gap_y
        
        self.pipes.append({
            'x': curr_w,
            'gap_y': gap_y,
            'passed': False
        })

    def on_touch_down(self, touch):
        if self.game_over:
            self.init_game_metrics()
        else:
            self.is_pressing = True
        return True

    def on_touch_up(self, touch):
        self.is_pressing = False
        return True

    def update_game(self, dt):
        self.animation_time += dt
        
        curr_w = self.width if self.width > 100 else Window.width
        curr_h = self.height if self.height > 100 else Window.height
        
        # Lazy Initialization Guard: Wait until screen dimensions pass Kivy's boot defaults
        if not self.game_initialized:
            if curr_w > 100 and curr_h > 100:
                self.init_game_metrics()
            return

        if not self.game_over:
            # Dynamic scaling physics parameters
            current_pipe_speed = self.base_pipe_speed + (self.score * 0.3)
            current_spawn_interval = 100 + (self.score * 5)

            # --- CONTINUOUS FLYING PHYSICS ---
            if self.is_pressing:
                self.bird_vy = min(8.5, self.bird_vy + self.flap_strength * dt * 60)
            else:
                self.bird_vy += self.gravity
                
            self.bird_y += self.bird_vy
            
            # --- TAIL POSITION HISTORY ENGINE ---
            self.tail_history.append((self.bird_x, self.bird_y))
            if len(self.tail_history) > self.max_tail_segments:
                self.tail_history.pop(0)
                
            # Shift the tail backwards dynamically relative to the pipe scrolling speed
            for idx in range(len(self.tail_history)):
                tx, ty = self.tail_history[idx]
                self.tail_history[idx] = (tx - current_pipe_speed, ty)
            
            # --- PIPE GENERATION TIMERS ---
            self.spawn_timer += 1
            if self.spawn_timer >= current_spawn_interval:
                self.spawn_pipe()
                self.spawn_timer = 0
                
            # --- UPDATE OBSTACLES TRAJECTORY ---
            rem_pipes = []
            for pipe in self.pipes:
                pipe['x'] -= current_pipe_speed
                
                if not pipe['passed'] and pipe['x'] + self.pipe_width < self.bird_x:
                    pipe['passed'] = True
                    self.score += 1
                    
                bird_left = self.bird_x - self.bird_radius
                bird_right = self.bird_x + self.bird_radius
                
                if pipe['x'] < bird_right and pipe['x'] + self.pipe_width > bird_left:
                    if self.bird_y + self.bird_radius > pipe['gap_y'] + self.pipe_gap or \
                       self.bird_y - self.bird_radius < pipe['gap_y']:
                        self.game_over = True
                        self.is_pressing = False
                        
                if pipe['x'] + self.pipe_width > 0:
                    rem_pipes.append(pipe)
            self.pipes = rem_pipes
            
            if self.bird_y - self.bird_radius < 0 or self.bird_y + self.bird_radius > curr_h:
                self.game_over = True
                self.is_pressing = False

        # --- GRAPHICS CANVAS GENERATION PASSES ---
        self.canvas.clear()
        
        with self.canvas:
            # 1. Cosmic Gradient Background
            r1 = (math.sin(self.animation_time * 0.2) + 1) / 2 * 0.1
            g1 = (math.cos(self.animation_time * 0.3) + 1) / 2 * 0.05
            b1 = (math.sin(self.animation_time * 0.4) + 1) / 2 * 0.2
            
            r2 = (math.cos(self.animation_time * 0.3) + 1) / 2 * 0.05
            g2 = (math.sin(self.animation_time * 0.2) + 1) / 2 * 0.15
            b2 = (math.cos(self.animation_time * 0.5) + 1) / 2 * 0.1

            slices = 12
            slice_w = curr_w / slices if curr_w > 0 else 30
            for s in range(slices):
                t = s / float(slices)
                Color(r1*(1-t) + r2*t, g1*(1-t) + g2*t, b1*(1-t) + b2*t, 1.0)
                Rectangle(pos=(self.x + (s * slice_w), self.y), size=(slice_w + 2, curr_h))

            # 2. Render Neon Pillars
            for pipe in self.pipes:
                top_y = pipe['gap_y'] + self.pipe_gap
                top_h = curr_h - top_y
                bot_y = 0
                bot_h = pipe['gap_y']
                
                for pass_idx in range(2):
                    if pass_idx == 0:
                        Color(1.0, 0.0, 0.4, 0.25)
                        lw = 6
                    else:
                        Color(1.0, 1.0, 1.0, 0.95)
                        lw = 2
                    
                    Line(rectangle=(pipe['x'], top_y, self.pipe_width, top_h), width=lw)
                    Line(rectangle=(pipe['x'], bot_y, self.pipe_width, bot_h), width=lw)

            # 3. RENDER FLEXIBLE GLOWING LONG TAIL
            if len(self.tail_history) > 1:
                # Synchronize neon spectrum colors to the cyber-bird body
                tr = (math.sin(self.animation_time * 4) + 1) / 2 * 0.3 + 0.7
                tg = (math.sin(self.animation_time * 4 + 2) + 1) / 2 * 0.5 + 0.5
                tb = 0.2
                
                # Draw discrete connected line fragments that progressively shrink and fade out
                for idx in range(len(self.tail_history) - 1):
                    progress = idx / float(len(self.tail_history) - 1)
                    
                    pt1 = self.tail_history[idx]
                    pt2 = self.tail_history[idx + 1]
                    
                    # Outer blur neon glow pass
                    Color(tr, tg, tb, progress * 0.35)
                    Line(points=[pt1[0], pt1[1], pt2[0], pt2[1]], width=progress * 8.5)
                    
                    # Core high-intensity inner core center line
                    Color(1.0, 1.0, 1.0, progress * 0.9)
                    Line(points=[pt1[0], pt1[1], pt2[0], pt2[1]], width=progress * 2.5)

            # 4. Render Player Cyber-Bird Elements
            sr = (math.sin(self.animation_time * 4) + 1) / 2 * 0.3 + 0.7
            sg = (math.sin(self.animation_time * 4 + 2) + 1) / 2 * 0.5 + 0.5
            sb = 0.2
            
            Color(sr, sg, sb, 0.4)
            Line(ellipse=(self.bird_x - 22, self.bird_y - 22, 44, 44), width=0, close=True)
            
            Color(1.0, 1.0, 1.0, 0.95)
            Line(ellipse=(self.bird_x - 14, self.bird_y - 14, 28, 28), width=0, close=True)
            
            eye_offset_y = max(-5, min(5, self.bird_vy * 0.8))
            Color(0.0, 0.0, 0.0, 1.0)
            Line(ellipse=(self.bird_x + 4, self.bird_y + 3 + eye_offset_y, 4, 4), width=0, close=True)

            # 5. Score Display Panel Matrix
            Color(1.0, 1.0, 1.0, 0.8)
            for score_idx in range(self.score):
                bx = 30 + (score_idx * 14)
                by = curr_h - 40
                Rectangle(pos=(bx, by), size=(8, 16))
                
            if self.game_over:
                Color(1.0, 0.0, 0.0, 0.5)
                Line(rectangle=(curr_w/2 - 100, curr_h/2 - 30, 200, 60), width=3)

class NeonFlappyBirdApp(App):
    def build(self):
        return FlappyNeonWidget()

if __name__ == '__main__':
    NeonFlappyBirdApp().run()
