class ObstacleDetector:

    def __init__(self):
        self.safe_distance = 3

    def detect(self, distance):

        if distance < self.safe_distance:
            print("Obstacle Detected")
            print("Changing Flight Path")
        else:
            print("Path Clear")


if __name__ == "__main__":
    detector = ObstacleDetector()
    detector.detect(2)
