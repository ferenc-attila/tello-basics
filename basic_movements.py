from djitellopy import Tello
import cv2

width = 1024
height = 768
is_real_flight = True

# Connect to the Tello

drone = Tello()
drone.connect()

drone.for_back_velocity = 0
drone.left_right_velocity = 0
drone.up_down_velocity = 0
drone.yaw_velocity = 0
drone.speed = 0

print(drone.get_battery())

drone.streamoff()
drone.streamon()

while True:

    frame_read = drone.get_frame_read()
    my_frame = frame_read.frame
    drone_stream = cv2.resize(my_frame, (height, width))

    if is_real_flight & drone.get_battery() >= 30:
        drone.takeoff()
        drone.move_up(200)
        drone.move_forward(200)
        drone.rotate_clockwise(90)
        drone.move_forward(100)
        drone.rotate_clockwise(90)
        drone.move_forward(200)
        drone.rotate_clockwise(90)
        drone.move_forward(100)
        drone.land()
        break

    cv2.imshow('result', drone_stream)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.land()
        break
