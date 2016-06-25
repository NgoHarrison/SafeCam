import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (640, 480)
	camera.start_preview()
	time.sleep(5)	

	while True:
		print "Saving Image..."
		camera.capture('/tmp/raw.jpg')
		time.sleep(3)
		
	camera.stop_preview()
