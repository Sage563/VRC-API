import json
import os
import time as times

class utills():
    def __init__(self ,json="VRC.json"):
        self.json =json
        self.value =None
        

    def startup_files(self):
        file ="""{
    "name": "VRC",
    "version": "1.0.0",
    "description": "A JSON file for VRC configuration",
    "VRC": [
        {}
    ],
    "settings": [
        {
            "counter": {
                "counter": -1
            }
            
        }
    ]
}"""
        val = True if os.path.exists(self.json) else False
        if val == False:
            with open(self.json, "w") as f:
                f.write(file)
        else:
            pass
    def create_person(self, name,recorder):
        with open(self.json,"r") as f:
            data = json.load(f)
            f.close()
        data["VRC"].append({name : recorder})

        with open(self.json ,"w")as f:
            json.dump(data ,f)
    def countdown(self ,time):
        for i in range(time):
            times.sleep(1)
            print(i)
                
