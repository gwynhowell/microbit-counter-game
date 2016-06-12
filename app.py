""" a simple game for the bbc microbit computer.

    a random number of leds are shown.
    the aim of the game is to press the a button once for each led and
    press the b button to submit your answer.
"""

from microbit import display, sleep, button_a, button_b
import random

NUM_LEDS = 25

def get_coords(num):
    """ returns a tuple representing the x, y coordinates of a microbit led

        Args:
            num: int representing the led assuming they are numbered as below:

            0  1  2  3  4
            5  6  7  8  9
            10 11 12 13 14
            15 16 17 18 19
            20 21 22 23 24

        Returns:
            tuple of ints representing the x, y coordinate
    """

    # assert the input is within the valid range ...
    assert num >= 0 and num < NUM_LEDS, 'Num out of range'

    # canclulate the coords ...
    x = num % 5
    y = (num - x) / 5

    # return the result ...
    return (int(x), int(y))

def get_button_presses():
    """ returns how many times button_a is
        pressed until button_b is pressed
    """

    # getting the count now resets the counter
    num = button_a.get_presses()

    # sleep until button_b is pressed ...
    while not button_b.is_pressed():
        sleep(100)

    # get the count again to get the number of
    # button_a presses since the last call
    num = button_a.get_presses()

    # return the result ...
    return num

def main():
    """ entry point to the app """

    # loop forever
    while True:
        # generate a random number to represent the number of leds to show ...
        num = random.randint(0, 10)

        # clear the display from the previous game ...
        display.clear()

        # a list to keep track of which leds have been used ...
        used = []

        # loop 'num' times ...
        for i in range(num):
            # generate a random number to represent which led to show ...
            led = random.randint(0, NUM_LEDS-1)

            # if the led has already been used,
            # generate another random number ...
            while led in used:
                led = random.randint(0, NUM_LEDS-1)
            used.append(led)

            # get the coords for the led to show ...
            x, y = get_coords(led)

            # show the led ...
            display.set_pixel(x, y, 9)

        # get the answer from the user ...
        input_num = get_button_presses()

        # if the answer is correct, display WIN otherwise LOSE ...
        if num == input_num:
            display.scroll("WIN!")
        else:
            display.scroll("LOSE!")

main()
