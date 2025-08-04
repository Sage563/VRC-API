import req
req.used()
import utills
import add_num
import API
import isai
import recorder
import os
import time

def main():
    print("Let's get everything set up. Installing necessary packages...")
    config_file = "VRC.json"
    utils_obj = utills.utills(config_file)
    utils_obj.startup_files()
    print(f"Config file '{config_file}' is ready.")

    new_counter = add_num.plus()
    print("The counter has been incremented. New value:", new_counter)

    
    audio_file = str(new_counter) +".mp3"
    utils_obj.countdown(4)
    print("Recording a short audio sample. Please speak after the prompt...")
    time.sleep(2)
    recorder.recorder(filename=audio_file)
    print(f"Your recording was saved as '{audio_file}'.")
    synthetic = isai.isai(audio_file)

    new_counter = add_num.plus()

    audio_files = str(new_counter) +".mp3"
    utils_obj.countdown(4)
    print("Recording a short audio sample. Please speak after the prompt...")
    time.sleep(2)
    recorder.recorder(filename=audio_files)
    print(f"Your recording was saved as '{audio_files}'.")
    synthetic = isai.isai(audio_files)


    print("The synthetic voice detector returned:", synthetic)
    match = API.main(audio_file, audio_files)
    print("The API check for voice & transcription match gave the result:", match)
    if match ==False:
        exit(1)

    username ="TESTING!@#"
    print(f"Creating Person with Username {username} , recording {audio_file}")
    utils_obj.create_person(username ,audio_file)

if __name__ == "__main__":
    main()