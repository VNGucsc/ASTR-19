class animal:
    arm_length = 5.0
    leg_length = 5.0
    eye_num = 2
    tail = True
    furry = True

    def __init__(self, arm, leg, eye, tail, furry):
        self.arm = arm
        self.leg = leg
        self.eye = eye
        self. tail = tail
        self.furry = furry
    
    def print_animal(self):
        print(f"Arm length: {self.arm_length}\nLeg length: {self.leg_length}\nEye count: {self.eye_num}\nDoes it have a tail? {self.tail}\nIs it furry? {self.furry}")
