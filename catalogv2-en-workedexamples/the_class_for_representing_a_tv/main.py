#Step 1: Define the class
class TV1 :
        #Step 1.1: Initialize the state of the TV
        def __init__(self):
                self.__on = False
                self.__channel = 1
        #Step 1.2: Define the methods to change the on/off state of the TV
        def turn_on(self) :
                self.__on = True
        def turn_off(self) :
                self.__on = False
        #Step 1.3: Define the methods to change the channel of the TV
        def set_channel(self, new_channel) :
                if self.__on and new_channel >= 1 and new_channel <= 120 :
                        self.__channel = new_channel
        def channel_up(self) :
                if self.__on and self.__channel < 120 :
                        self.__channel += 1
        def channel_down(self) :
                if self.__on and self.__channel > 1 :
                        self.__channel -= 1
        #Step 1.4: Define the methods to get the current state of the TV
        def get_channel(self) :
                return self.__channel
        def is_on(self) :
                return self.__on
#Step 2: Test the class
tv1 = TV1()
tv1.turn_on()
tv1.set_channel(30)
tv2 = TV1()
tv2.turn_on()
tv2.channel_up()
tv2.channel_up()
tv2.channel_down()
print("tv1's channel is " + str(tv1.get_channel()))
print("tv2's channel is " + str(tv2.get_channel()))
