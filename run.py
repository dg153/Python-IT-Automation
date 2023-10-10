#!/usr/bin/env python3
import os
import requests
#Specify the file location
dirname = "/data/feedback"

#Open the file and loop within

for filename in os.listdir(dirname):
    """Check the file has .txt extension. Check stackoverflow "How can I check the extension of a file" """
    data_dict = {}
    if filename.endswith(".txt"):
        with open(os.path.join(dirname,filename)) as files:
    #Data is listes in order of title, name, date and feedback
            data = files.readlines()
            title = data[0].strip()
            name = data[1].strip()
            date = data[2].strip()
            feedback= data[3].strip()
            data_dict = {"title": title, "name": name, "date": date, "feedback":feedback}
            #print(data_dict)
            response = requests.post("http://34.67.59.188/feedback/",data=data_dict)
            """if response.ok != True:
                raise Exception("POST Request Failed! Status code: {} || File: {}".format(response.status_code, filename))
            print("Feedback Addition is Successfull!") """
            print(response.request.body)
            print(response.status_code)

