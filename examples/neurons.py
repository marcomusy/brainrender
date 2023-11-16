from pathlib import Path

from morphapi.api.mouselight import MouseLightAPI
from myterial import orange
from rich import print

from brainrender import Scene
from brainrender.actors import Neuron, make_neurons

print(f"[{orange}]Running example: {Path(__file__).name}")

# Create a brainrender scene
scene = Scene(title="neurons")

# Add a neuron from file
scene.add(Neuron("data/neuron1.swc"))

# Download neurons data with morphapi
mlapi = MouseLightAPI()
neurons_metadata = mlapi.fetch_neurons_metadata(
    filterby="soma", filter_regions=["MOs"]
)

to_add = [neurons_metadata[47], neurons_metadata[51]]
neurons = mlapi.download_neurons(to_add)
neurons = scene.add(*make_neurons(*neurons, neurite_radius=12))

# Render!
scene.render()
