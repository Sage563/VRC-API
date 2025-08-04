# VRC-API

Welcome to the VRC-API project! This project is a voice recording and analysis tool that helps you manage voice recordings, detect synthetic voices, and compare recorded samples. It includes functionalities such as initializing configuration files, recording audio, incrementing counters, and more.

## Overview

The project integrates several Python modules. Click on each file below to jump to its detailed description:

- [req.py](#reqpy)
- [utills.py](#utillspy)
- [add_num.py](#add_numpy)
- [recorder.py](#recorderpy)
- [isai.py](#isaipy)
- [API.py](#apipy)
- [example.py](#examplepy)

Below is the file system layout of the project:

```
VRC-API/
├── API.py
├── README.md
├── VRC.json
├── add_num.py
├── isai.py
├── recorder.py
├── req.py
└── utills.py
```

## File Descriptions and Functions

### req.py
<a id="reqpy"></a>

This module ensures that all required Python packages are installed.

- **spinner(message, stop_event)**  
  Displays a spinning cursor animation while a task is in progress.
  
- **progress_bar(package, stop_event, bar_length=30)**  
  Displays a progress bar animation for package installation.
  
- **install_and_import(package_name, import_name=None)**  
  Checks if a package is installed; if not, installs it using pip while showing an animated indicator.
  
- **used()**  
  Iterates through a predefined list of packages and calls `install_and_import` for each.

### utills.py
<a id="utillspy"></a>

Provides utility functions for managing configuration files and basic operations.

- **class utills**  
  A class to handle the JSON configuration file (`VRC.json`).
  
  - **__init__(self, json="VRC.json")**  
    Initializes the instance with the JSON file path.
    
  - **startup_files(self)**  
    Checks if the configuration file exists; if not, creates one with a default template.
    
  - **create_person(self, name, recorder)**  
    Reads the configuration, then adds a new entry (with the given name and associated audio file) under the "VRC" key.
    
  - **countdown(self, time)**  
    Provides a simple countdown timer before recording audio.

### add_num.py
<a id="add_numpy"></a>

Handles incrementing a counter in the configuration file.

- **plus()**  
  Opens `VRC.json`, looks for the "counter" inside "settings", increments its value, writes the updated JSON back to the file, and returns the new counter value.  
  This ensures that each recorded file can have a unique identifier.

### recorder.py
<a id="recorderpy"></a>

Handles recording audio from the microphone and saving it as an MP3 file.

- **recorder(duration=7, filename="89.mp3", sample_rate=44100, channels=1)**  
  Records audio for a set duration, encodes it to MP3 using the `lameenc` encoder, and saves it to the specified file.  
  Steps include capturing PCM data, encoding it to MP3, and then writing the output file.

### isai.py
<a id="isaipy"></a>

Detects synthetic voices using an AI transformer model.

- **isai(audio_path: str, threshold: float = 0.5) -> bool**  
  Loads the audio using torchaudio, resamples if needed, and processes it through a pre-loaded model pipeline to determine if the voice is synthetic.  
  Returns `True` if the score meets or exceeds the threshold and the label indicates a synthetic voice; otherwise, returns `False`.

### API.py
<a id="apipy"></a>

Provides functionality to compare two audio files both in voice characteristics and transcriptions.

- **resource_path(relative_path)**  
  Helps in locating resources (useful when packaged with PyInstaller).
  
- **load_mp3(file_path)**  
  Loads an MP3 file, ensuring it has the right sample rate and returns a mono numpy array of the waveform.
  
- **transcribe(file_path)**  
  Uses the Faster Whisper model to transcribe the audio file into text.
  
- **texts_similar(a, b, threshold=0.85)**  
  Compares two strings and returns `True` if their similarity exceeds the threshold.
  
- **main(file1, file2, voice_threshold=0.7, text_threshold=0.85)**  
  Compares two audio files by:
  - Extracting their audio embeddings for voice similarity.
  - Transcribing them into text.
  - Comparing both the voice similarity and the transcribed texts.
  Returns `True` if both criteria meet their respective thresholds.

### example.py
<a id="examplepy"></a>

A complete script that demonstrates the project workflow by utilizing all modules above.

- **main()**  
  Orchestrates the following steps:
  - Installing required packages via `req.py`.
  - Initializing the configuration file with `utills.py`.
  - Incrementing counters using `add_num.py` to generate unique filenames.
  - Recording two audio samples using `recorder.py`.
  - Detecting synthetic voice in the recordings with `isai.py`.
  - Comparing the recordings using `API.py`.
  - Finally, adding a new person record into the config via `utills.py`.

## How to Use

1. **Clone the Repository**

   Open a terminal and run:

```sh
   git clone https://github.com/Sage563/VRC-API.git
   cd VRC-API
```

2. **Run the Example Script**

   To see everything in action, simply run:

```sh
   python example.py
```

This will:
   - Install necessary packages.
   - Initialize the configuration file (`VRC.json`).
   - Increment a counter and create unique filenames.
   - Record two audio samples.
   - Check if the recordings are synthetic.
   - Compare the recordings for similarity.
   - Finally, add a new person record to the configuration file.

3. **Use the Modules Individually**

   - Use **utills.py** to manage the configuration file.
   - Call **recorder.recorder()** whenever you need to capture a new audio sample.
   - Check if a sample is synthetic by calling **isai.isai()**.
   - Compare audio files by leveraging **API.main()**.
   - Use **add_num.plus()** to get and update unique identifiers for your recordings.

## Contributing

Contributions and feedback are welcome. If you have ideas or improvements, please create a pull request or open an issue.

## License

This project is open source. See the LICENSE file for more information.

## Author

Developed by [Sage563](https://github.com/Sage563)