"""
Main launcher for the autonomous drone project.
"""

from drone_control import DroneController
from obstacle_detection import ObstacleDetector

def main():
    drone = DroneController()
    detector = ObstacleDetector()

    drone.arm()
    drone.takeoff(10)

    detector.detect(5)

    print("Mission Started")

if __name__ == "__main__":
    main()
