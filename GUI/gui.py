class GUI(object):
    """This is the main class for the GUI of the RoadSense site machine"""

    @staticmethod
    def help():
        print("""
RoadSense help. July 17, 2017.

v   -   Start the private vehicle detection algorithm.
c   -   Start the commercial vehicle detection algorithm.
p   -   Start the pedestrian detection algorithm.

s   -   Stop all detection algorithms.
r   -   Restart application.

h   -   Print help.

        """)

    @staticmethod
    def disclaimer():
        print("""
///////////////////////////////////////////////////////////////////////////////////
  This program is delivered under the Trend Antenna Continental program (C) 2017.
              ____                 _ ____
             |  _ \ ___   __ _  __| / ___|  ___ _ __  ___  ___
             | |_) / _ \ / _` |/ _` \___ \ / _ \ '_ \/ __|/ _ \\
             |  _ < (_) | (_| | (_| |___) |  __/ | | \__ \  __/
             |_| \_\___/ \__,_|\__,_|____/ \___|_| |_|___/\___|
                       Field Machine Software V1.0

//////////////////////////////////////////////////////////////////////////////////
        """)
