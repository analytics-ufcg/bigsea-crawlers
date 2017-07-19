import sys
import os
import pycurl
from StringIO import StringIO
from datetime import datetime
import Constants

if len(sys.argv) < 2:
    print "Error: You must specify the output filepath!"
    print "Your command should be something like: "
    print "python %s <output_absolute_filepath>" % (sys.argv[0])
    sys.exit(1)
elif not os.path.exists(sys.argv[1]):
    print "Error: output_filepath doesn't exist! You must specify a valid one!"
    sys.exit(1)

current_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
output_filepath = sys.argv[1]

buffer = StringIO()
c = pycurl.Curl()

c.setopt(c.URL, Constants.berlim_url)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()

with open(output_filepath + "/" + current_time, 'w') as the_file:
    the_file.write(body)