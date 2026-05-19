# Librosa Presentation Code

![Screenshot of the primary chart UI.](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/c50b15f6-4ce6-42b3-b18e-3baf5ae98e1d.png)

Extracts audio features from `.wav` and `.mp3` files, exporting them as JSON and visualizing track comparisons with a radar chart.

## Overview

Analyzes audio files placed in the `audio` directory and extracts key characteristics such as tempo, average beat time, chroma intensity and MFCC values. The extracted data is saved as structured JSON, making it useful for comparing multiple audio tracks in a D3 visualization.

The main workflow centers on `audio-workflow-example/app.py`, which processes the audio files and prepares the data for `index.html`, where D3.js displays the results as a radar chart. Each audio file is represented as a polygon, allowing users to visually compare audio features across tracks.

## Set Up Instructions

Below are the required software programs and instructions for using this application on a Linux machine.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository: `git clone git@github.com:devbret/librosa-presentation.git`

4. Navigate to the repo's directory: `cd librosa-presentation`

5. Create a virtual environment: `python3 -m venv venv`

6. Activate your virtual environment: `source venv/bin/activate`

7. Install the needed dependencies: `pip install -r requirements.txt`

8. Place `.wav` and/or `.mp3` files inside the `audio` directory.

9. Run the feature extraction script: `python3 audio-workflow-example/app.py`

10. Open another terminal

11. Navigate to the repo's subdirectory: `cd librosa-presentation/audio-workflow-example`

12. Launch a local `HTTP` server: `python3 -m http.server`

13. Open the local app in your browser: `http://localhost:8000`

14. When finished exploring, stop the `HTTP` server: `CTRL + C`

15. Exit the virtual environment: `deactivate`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Extract meaningful audio features from `.wav` and `.mp3` files using Librosa

- Convert audio analysis results into structured JSON for later reuse

- Compare multiple audio tracks through a D3 radar chart

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
