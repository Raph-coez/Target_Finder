import io
import socket
import struct
import time
from getImage import*
import os





cam = cv2.VideoCapture(0)
count = 1
while count < 10:
    ret, image = cam.read()
    if cv2.waitKey(1500) &0xFF == ord('q'):
        break
    copy_image = numpy.copy(image)
    image_name = 'images/image_' + str(count) + '.jpeg'
    mp.imsave(image_name, copy_image)
    count += 1

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()
client_socket.connect(('192.168.2.225', 8200))

# Make a file-like object out of the connection
connection = client_socket.makefile('wb')
try:
    
   
    # Note the start time and construct a stream to hold image data
    # temporarily (we could write it directly to connection but in this
    # case we want to find out the size of each capture first to keep
    # our protocol simple)
    start = time.time()
    stream = io.BytesIO()
    for filename in os.listdir("images"):
        with open(os.path.join("images", filename), 'r') as f:        
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            # Rewind the stream and send the image data over the wire
            stream.seek(0)
            connection.write(stream.read())
            # If we've been capturing for more than 30 seconds, quit
            if time.time() - start > 30:
                break
            # Reset the stream for the next capture
            stream.seek(0)
            stream.truncate()
        # Write a length of zero to the stream to signal we're done
        connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()