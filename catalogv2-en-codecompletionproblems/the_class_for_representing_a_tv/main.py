#Step 1: Define the class
class TV2 :
        #Step 1.1: Initialize the state of the TV
        def __init__(self):
                self.__on = False
                self.__volume_level = 1
        #Step 1.2: Define the methods to change the on/off state of the TV
        def turn_on(self) :
                self.__on = True
        def turn_off(self) :
                self.__on = False
        #Step 1.3: Define the methods to change the volume level of the TV
        def set_volume(self, new_volume_level) :
                if self.__on and new_volume_level >= 1 and new_volume_level <= 7 :
                        self.__volume_level = new_volume_level
        def volume_up(self) :
                if self.__on and self.__volume_level < 7 :
                        self.__volume_level += 1
        def volume_down(self) :
                if self.__on and self.__volume_level > 1 :
                        self.__volume_level -= 1
        #Step 4: Define the methods to get the current state of the TV
        def get_volume_level(self) :
                return self.__volume_level
        def is_on(self) :
                return self.__on
#Step 2: Test the class
tv1 = TV2()
tv1.turn_on()
tv1.set_volume(4)
tv1.set_volume(-1)
tv1.volume_down()
tv2 = TV2()
tv2.turn_on()
tv2.volume_up()
print("tv1's volume level is " + str(tv1.get_volume_level()))
print("tv2's volume level is " + str(tv2.get_volume_level()))
