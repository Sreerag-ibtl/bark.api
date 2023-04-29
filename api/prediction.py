"""Implement prediction endpoint.

Implement prediction endpoint.

Usage:
    from api.prediction implement <attribute>

"""

from typing import Dict

from _io import TextIOWrapper
from bark import SAMPLE_RATE, generate_audio, preload_models
from fastapi import FastAPI
from numpy.typing import NDArray
from scipy.io.wavfile import write

from api.create_audio_base_64 import create_audio_base_64
from api.create_unique_filename import create_unique_filename
from api.remove_file import remove_file

app: FastAPI = FastAPI()

# Load models.
preload_models()


@app.get("/predict/")
def predict(prompt: str) -> Dict[str, str]:  # dead: disable
    """Run prediction.

    Run prediction.

    Arguments:
        prompt: Prompt.

    Returns:
        URL to audio file.

    """
    # Generate audio.
    audio: NDArray = generate_audio(prompt)

    # Create unique file name to avoid conflicts.
    filename: str = create_unique_filename(prompt)

    # Write to a filename to load as base64.
    write(filename, SAMPLE_RATE, audio)

    # Open file in read mode.
    audio_file: TextIOWrapper = open(filename, "rb")

    # Create base64 string.
    audio_base_64: str = create_audio_base_64(audio_file)

    # Close file after usage.
    audio_file.close()

    # Remove file to clean up environment.
    remove_file(filename)
    return {"status": "Ok", "audio_base_64": audio_base_64}
