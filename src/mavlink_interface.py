"""
MAVLink Communication Interface
"""

class MAVLinkConnection:

    def connect(self):
        print("Connecting to Pixhawk...")

    def heartbeat(self):
        print("Heartbeat Received")


if __name__ == "__main__":
    mav = MAVLinkConnection()
    mav.connect()
    mav.heartbeat()
