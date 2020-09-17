import os
import argparse

from textgenrnn import textgenrnn
from .utils import generate_meme, correct_spelling
from .meme_template import MemeTemplate


class Memegen():
    def __init__(self, template: MemeTemplate, temperature: int = 0.5):
        self.template = template
        self.temperature = temperature
        self.model = textgenrnn(weights_path=f"models/{template.value}/weights.hdf5")

    def predict(self):
        while True:
            sample = self.model.generate(
                n=1,
                return_as_list=True,
                temperature=self.temperature)[0]
            segments = [w.strip() for w in sample[:-1].split(";")]

            # Make sure both the top and bottom parts were generated
            if len(segments) != 2:
                continue

            top, bottom = segments

            # Generate and return a meme image
            return generate_meme(top, bottom, self.template.value), top, bottom
