import base64
import vertexai

from vertexai.generative_models import GenerationConfig, GenerativeModel, Part

# TODO(developer): Update and un-comment below line
# PROJECT_ID = "your-project-id"
vertexai.init(project=777, location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")

# Load example image from local storage

# Generation Config
config = GenerationConfig(
    max_output_tokens=2048, temperature=0.4, top_p=1, top_k=32
)

# Generate text
response = model.generate_content(
    [ "what is this image?"], generation_config=config
)
print(response.text)
# Example response:
# That's a lovely overhead shot of a rustic still life featuring blueberry scones.
# Here's a breakdown of what's in the image:
# * **Blueberry Scones:** Several freshly baked blueberry scones are arranged on
# a piece of parchment paper. They appear to be homemade and slightly crumbly.
# ...