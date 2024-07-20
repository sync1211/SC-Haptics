#from pynput.keyboard import Key, Listener
import win32api
from Vehicles.Ships.Modes.ShipMode import ShipMode
from tactPython.bhaptics import better_haptic_player as haptics_player
import time
import pygame

import utils
from Vehicles.Ships.FighterShip import FighterShip

######################### user changeable variables #########################

# Below all buttons that are used per joystick keyboard and mouse


# The values below represents the joystick number as it's seen by your system. 0 is the first joystick, 1 second joystick, etc
# If you have additional joysticks installed these values might change
JOY1 = 0
JOY2 = 1 #if you only want to use one joystick set this value the same as the above. You might need to change the throttle axis below as well.

JOY1_SHOOT1 = 0 # shooting primary gun
JOY1_SHOOT2 = 2 # shooting second gun
JOY2_BOOST =  3 # boost button
JOY2_AXIS_X = 1 # X Axis
JOY2_AXIS_Y = 0 # Y Axis
JOY2_AXIS_Y = 0 # Y Axis
JOY2_AXIS_TWIST = 2 # Twist Axis

#TODO: Replace with pyinput
MOUSE_LEFT = 0x01 # this hexa represents the left mouse button
MOUSE_RIGHT = 0x02 # this hexa represents the right mouse button
MOUSE_MIDDLE = 0x03 # this hexa represents the right mouse button
KEY_1 = 0x31 # this hexa represents the key 1
KEY_2 = 0x32 # this hexa represents the key 2
KEY_3 = 0x33 # this hexa represents the key 3
KEY_R = 0x52 # this hexa represents the key r
KEY_F = 0x46 # this hexa represents the key f
KEY_0 = 0x30 # this hexa represents the key 0
KEY_9 = 0x39 # this hexa represents the key 9
KEY_8 = 0x38 # this hexa represents the key 8

# all key codes available here: https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes


######################### END OF user changeable variables #########################

# don't modify anything after this line unless you know what you are doing :)


pygame.init()

JOYSTICK1 = pygame.joystick.Joystick(JOY1)
JOYSTICK1.init()

JOYSTICK2 = pygame.joystick.Joystick(JOY2)
JOYSTICK2.init()


print("Initializing...")
haptics_player.initialize()
print("bHaptics Player Initialized!")

INTERVAL = 40

def map_range(value, low1, high1, low2, high2):
    newval = low2 + (high2 - low2) * (value - low1) / (high1 - low1)
    return newval


def haptics_loop(update_delay: int = 100, mouse_m_hold_duration: int = 1000):
    haptics_enabled = True
    in_ship = True

    ship = FighterShip()
    #TODO: add player haptics

    mouse_m_hold = 0

    last_scm_mode = ShipMode.WEAPON
    last_nav_mode = ShipMode.QUANTUM

    while True:
        pygame.event.get()

        # Calculate throttle intensity
        joystick_x = JOYSTICK2.get_axis(JOY2_AXIS_X)
        joystick_y = JOYSTICK2.get_axis(JOY2_AXIS_Y)
        joystick_twist = JOYSTICK2.get_axis(JOY2_AXIS_TWIST)

        joystick_movement = max(abs(joystick_x), abs(joystick_y), abs(joystick_twist))
        throttle_intensity = int(map_range(joystick_movement, 0, 1, 10, 60))

        if throttle_intensity > 0 and JOYSTICK2.get_button(JOY2_BOOST):
            throttle_intensity = throttle_intensity + 25
        
        key_weapon1 = JOYSTICK1.get_button(JOY1_SHOOT1)
        key_weapon2 = JOYSTICK1.get_button(JOY1_SHOOT2)

        # Get key states
        #keystate_mouse_1 = win32api.GetKeyState(MOUSE_LEFT)
        #keystate_mouse_2 = win32api.GetKeyState(MOUSE_RIGHT)
        keystate_mouse_3 = win32api.GetKeyState(MOUSE_MIDDLE)
        # keystate_1 = win32api.GetKeyState(KEY_1)
        # keystate_2 = win32api.GetKeyState(KEY_2)
        keystate_8 = win32api.GetKeyState(KEY_8)
        # keystate_r = win32api.GetKeyState(KEY_R)
        # keystate_f = win32api.GetKeyState(KEY_F)
        keystate_0 = win32api.GetKeyState(KEY_0)
        keystate_9 = win32api.GetKeyState(KEY_9)

        #print(keypresstime)
        if keystate_9:
            haptics_enabled = False

        if keystate_0:
            haptics_enabled = True

        if not haptics_enabled:
            continue

        # Ship engine
        ship.throttle = throttle_intensity

        if keystate_8:
            ship.engine_active = not ship.engine_active
            
        # Ship Weapons
        if ship.currentMode != ShipMode.QUANTUM or ship.currentMode != ShipMode.FLIGHT:
            if ship.currentMode == ShipMode.MISSILE:
                ship.firing_missile = key_weapon1
            else:
                ship.firing1 = key_weapon1

            ship.firing2 = key_weapon2
        else:
            #TODO: implement me!
            pass

        # Ship modes
        if keystate_mouse_3:
            mouse_m_hold += update_delay

        elif mouse_m_hold >= mouse_m_hold_duration: # Long press -> Mode switch (SCM / NAV)
            if ship.currentMode == ShipMode.WEAPON or ship.currentMode == ShipMode.MISSILE:
                last_scm_mode = ship.currentMode
                ship.currentMode = last_nav_mode
                print("Switched to NAV")
            else:
                last_nav_mode = ship.currentMode
                ship.currentMode = last_scm_mode
                print("Switched to SCM")

        elif mouse_m_hold > 0: # Short press -> (Weapon / Missile) / (Flight / Quantum)

            if ship.currentMode == ShipMode.WEAPON:
                ship.currentMode = ShipMode.MISSILE
                print("Mode: Missiles")
            elif ship.currentMode == ShipMode.MISSILE:
                ship.currentMode = ShipMode.WEAPON
                print("Mode: Weapons")
            elif ship.currentMode == ShipMode.FLIGHT:
                ship.currentMode = ShipMode.QUANTUM
                print("Mode: Quantum")
            elif ship.currentMode == ShipMode.QUANTUM:
                ship.currentMode = ShipMode.FLIGHT
                print("Mode: Flight")

            mouse_m_hold = 0
        else:
            mouse_m_hold = 0         
        
        pattern = {"front": [], "back": []}

        if in_ship:
            utils._merge_patterns(pattern, ship.GetHapticsPattern())
        else:
            #utils._merge_patterns(pattern, player.GetHapticsPattern())
            pass

        haptics_player.submit_dot("frontFrame", "VestFront", pattern["front"], update_delay + 10)
        haptics_player.submit_dot("backFrame", "VestBack", pattern["back"], update_delay + 10)

        time.sleep(update_delay / 1000)

if __name__ == "__main__":
    haptics_loop(INTERVAL)