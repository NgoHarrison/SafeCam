import time
import cv2
from twilio.rest import TwilioRestClient

accountSid = "AC51365a670d38f32fb1bc163bf0f300fc"
authToken = "8cf63b9fd2d05385cabfb175b94dab1b"

print "Starting Recognition"
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:
	image = cv2.imread("/var/www/html/raw.jpg")
	
	print "Loading Image..."
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor = 1.1,
		minNeighbors = 5,
		minSize = (30, 30),
		flags = cv2.CASCADE_SCALE_IMAGE
	)
	
	print "Finding Faces & Saving..."
	print len(faces)
	for (x, y, w, h) in faces:
		print "Found Face..."
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
	cv2.imwrite("/var/www/html/detected.jpg", image)
	
	if len(faces) > 0:
		client = TwilioRestClient(accountSid, authToken)
		
		message = client.messages.create(body="Alert from Safe Cam",
						to="+13474595013",
						from_="+13473219540",
						MediaUrl="http://192.241.244.189/html/detected.jpg"
			)
		print message.sid
		time.sleep(30)
		

	print "Done"
	time.sleep(1)
