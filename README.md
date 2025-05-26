# Librosa Presentation Code

This repo demonstrates how to extract audio features from `.wav` and `.mp3` files using the [Librosa](https://librosa.org/) Python library and visualize the results with a D3.js radar chart in the browser.

## Project Structure

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

Highlights how Librosa can be used to:

- Extract meaningful audio features

- Structure the results for multi-track comparison

- Export the data as JSON

- Visualize the results with an interactive radar chart using D3.js

## Scripts

This project includes two Python scripts that demonstrate how to analyze audio files using Librosa. Each script extracts key audio features and outputs structured data for further analysis or visualization.

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

## Usage

1. Clone the repo from GitHub:

```
git clone git@github.com:devbret/librosa-presentation.git

cd librosa-presentation
```

2. Create a virtual environment and install dependencies using:

```
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

3. Place `.wav` and/or `.mp3` audio files inside the `audio/` directory.

4. Run the feature extraction script:

```
python3 audio-workflow-example/app.py
```

5. Open `audio-workflow-example/index.html` in your browser to view the radar chart.

## Acknowledgments

- [Librosa](https://librosa.org/) for audio analysis

- [D3.js](https://d3js.org/) for interactive data visualization

- Example audio files provided under open licenses

## License

This project is open source and freely available for use.
