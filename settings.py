class Settings():
    # store all the setting class in alien_invasion

    def __init__(self):
        #initiatize game setting
        #screen set
        self.screen_width = 600
        self.screen_height = 500
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 2.2
        self.ship_limit = 3
        
        self.bullet_speed_factor = 3
        self.bullet_width = 2
        self.bullet_height = 6
        self.bullet_color = 60,60,60
        self.bullets_allowed = 4

        #alien setting    
        self.alien_speed_factor = 3
        self.fleet_drop_speed = 20
        #fleet_direction : 1:right shift -1:left shift
        self.fleet_direction = 1
