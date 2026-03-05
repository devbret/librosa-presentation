# Librosa Presentation Code

![Screenshot of the primary chart UI.](https://hosting.photobucket.com/bbcfb0d4-be20-44a0-94dc-65bff8947cf2/c50b15f6-4ce6-42b3-b18e-3baf5ae98e1d.png)

This repo demonstrates how to extract audio features from `.wav` and `.mp3` files using the [Librosa](https://librosa.org/) Python library and visualize the results with a D3.js radar chart in the browser.

## Project Structure

Below is a simple outline of how this project is structured.

```
├── audio/
│ ├── info.txt
│ ├── demo.wav
│ ├── demo.mp3
│ └── ...
├── audio-workflow-example/
│ ├── app.py
│ └── index.html
├── feature-extraction-example/
│ └── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Purpose

The purpose of this repo is to highlight how Librosa can be used to:

- Extract meaningful audio features

- Structure the results for multi-track comparison

- Export the data as JSON

- Visualize the results with an interactive radar chart using D3.js

## Scripts

This project includes two Python scripts which demonstrate how to analyze audio files using Librosa. Each script extracts key audio features and outputs structured data for further analysis and visualization.

### `audio-workflow-example/app.py`

- Loads all `.mp3` and `.wav` files in the `../audio/` directory

- Extracts:
  - Tempo (BPM)

  - Average beat time

  - Average chroma intensity

  - Average MFCC value

- Saves the result in `audio_feature_summary.json` for visualization

### `audio-workflow-example/index.html`

- Uses D3.js to load and visualize `audio_feature_summary.json` as a radar chart

- Each polygon represents one audio file

- The chart compares the four normalized features across multiple files

### `feature-extraction-example/app.py`

- A simplified version of the workflow

- Also extracts features but omits beat timing

- Good for quick tests or demonstrations

## Usage Instructions

What follows are the required setup instructions for using this program:

1. Clone the repo from GitHub by entering the following command into a Linux terminal:

```
git clone git@github.com:devbret/librosa-presentation.git
```

2. Open/enter the newly created repo directory:

```
cd librosa-presentation
```

3. Create a virtual environment:

```
python3 -m venv venv
```

4. Activate the virtual environment:

```
source venv/bin/activate
```

5. Install the needed packages:

```
pip install -r requirements.txt
```

6. Place `.wav` and/or `.mp3` audio files inside the `audio/` directory.

7. Run the feature extraction script:

```
python3 audio-workflow-example/app.py
```

8. Open `audio-workflow-example/index.html` in your browser to view the radar chart.

## Acknowledgments

- [Librosa](https://librosa.org/) for audio analysis

- [D3.js](https://d3js.org/) for interactive data visualization

- Example audio files provided under open licenses

## License

This project is open source and freely available for use.
