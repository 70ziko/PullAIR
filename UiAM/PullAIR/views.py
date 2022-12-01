from django.shortcuts import render
from django.http import HttpResponse
import json
import certifi
import pycurl
from io import BytesIO

def getAQ():
    # Creating a buffer as the cURL is not allocating a buffer for the network response
    buffer = BytesIO()
    c = pycurl.Curl()

    #initializing the request URL
    c.setopt(c.URL, 'https://api.waqi.info/feed/here/?token=d67b0b88305231aad7f5a6cce8e43da5d312411c')

    #setting options for cURL transfer  
    c.setopt(c.WRITEDATA, buffer)

    #setting the file name holding the certificates
    c.setopt(c.CAINFO, certifi.where())

    # perform file transfer
    c.perform()

    #Ending the session and freeing the resources
    c.close()

    aqicn = buffer.getvalue()
    return aqicn

# create a function
def geeks_view(request):
    return HttpResponse(getAQ())