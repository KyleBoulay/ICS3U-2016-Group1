# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This scene shows the main menu.

from scene import *

import time
import ui

from stats_scene import *
from credits_scene import *
from shop_scene import *
from help_scene import *
from game_scene import *
from settings_scene import *

class MainMenuScene(Scene):
    def setup(self):
        self.run_label_down = False
        self.help_label_down = False
        self.settings_label_down = False
        self.shop_label_down = False
        self.stats_label_down = False
        self.credits_label_down = False
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        # this method is called, when user moves to this scene
        
        # add MT blue background color
        self.background = SpriteNode('./assets/sprites/background.JPG', 
                                     position = self.size / 2,
                                     parent = self,
                                     scale = 1.25)
                                     
        self.smoke_run = SpriteNode('shp:BlackSmoke18', 
                                     position = self.size / 2,
                                     parent = self,
                                     scale = 1.25)
        
        self.run_label = LabelNode(text = 'Run',
                                     font=('Markerfelt-Wide', 50),
                                     parent = self,
                                     position = self.size / 2,
                                     color = 'grey')
                                     
        self.smoke_shop = SpriteNode('shp:BlackSmoke16', 
                                     position = (self.size_of_screen_x - 85, self.size_of_screen_y - 100),
                                     parent = self,
                                     scale = 1.25)
        
        self.shop_label = LabelNode(text = 'Shop',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (self.size_of_screen_x - 100, self.size_of_screen_y - 100),
                                     color = 'grey')
        
        self.smoke_credits = SpriteNode('shp:BlackSmoke13', 
                                     position = (100, 100),
                                     parent = self,
                                     scale = 1.25)
        
        self.credits_label = LabelNode(text = 'Credits',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (100, 100),
                                     color = 'grey')
        self.smoke_help = SpriteNode('shp:BlackSmoke10', 
                                     position = (300, 100),
                                     parent = self,
                                     scale = 1.25)
        
        self.help_label = LabelNode(text = 'Help',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (300, 100),
                                     color = 'grey')
                                     
        self.smoke_stats = SpriteNode('shp:BlackSmoke15', 
                                     position = (self.size_of_screen_x - 85, self.size_of_screen_y - 300),
                                     parent = self,
                                     scale = 1.25)
        
        self.stats_label = LabelNode(text = 'Stats',
                                     font=('Markerfelt-Wide', 40),
                                     parent = self,
                                     position = (self.size_of_screen_x - 100, self.size_of_screen_y - 300),
                                     color = 'grey')
                                     
        self.smoke_settings = SpriteNode('shp:BlackSmoke19', 
                                     position = (100, self.size_of_screen_y - 200),
                                     parent = self,
                                     scale = 1.25)
                                     
        self.settings_label = SpriteNode('iow:gear_b_256', 
                                     position = (100, self.size_of_screen_y - 200),
                                     parent = self,
                                     scale = 0.3,
                                     color = 'grey')
                                     
                                     
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        if self.stats_label.frame.contains_point(touch.location):
            self.stats_label_down = True
            self.stats_label.font = ('Markerfelt-Wide',45)
            self.start_time = time.time()
            self.present_modal_scene(StatsScene())
        if self.shop_label.frame.contains_point(touch.location):
            self.shop_label_down = True
            self.shop_label.font = ('Markerfelt-Wide',45)
            self.start_time = time.time()
            self.present_modal_scene(ShopScene())
        if self.settings_label.frame.contains_point(touch.location):
            self.settings_label_down = True
            self.settings_label.scale = 0.4
            self.start_time = time.time()
            self.present_modal_scene(SettingsScene())
        if self.run_label.frame.contains_point(touch.location):
            self.run_label_down = True
            self.run_label.font = ('Markerfelt-Wide',60)
            self.start_time = time.time()
            self.present_modal_scene(GameScene())
        if self.credits_label.frame.contains_point(touch.location):
            self.credits_label_down = True
            self.credits_label.font = ('Markerfelt-Wide',45)
            self.start_time = time.time()
            self.present_modal_scene(CreditsScene())
        if self.help_label.frame.contains_point(touch.location):
            self.help_label_down = True
            self.help_label.font = ('Markerfelt-Wide',45)
            self.start_time = time.time()
            self.present_modal_scene(HelpScene())
        
        
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        pass
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
    
