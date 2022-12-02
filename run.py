import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("../stable-diffusion-v1-5", torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to("cuda")

prompt = "intricate steampunk portrait of a person as king, smooth, sharp focus"
image = pipe(prompt).images[0]
image.save("filename.png")