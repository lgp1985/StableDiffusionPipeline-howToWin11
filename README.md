# StableDiffusionPipeline in Windows 11
This will guide in a simple steps how to run your StableDiffusionPipeline in Windows 11.

## Hardware Requirements
- nVidia GPU with 8GB+ of VRAM
- CPU supporting Virtualization technology

> Assure you have latest GPU drivers

# Installation

```PowerShell
wsl --install
winget install 9PDXGNCFSCZV # Ubuntu on msstore
winget install Microsoft.VisualStudioCode
```

Go to [Visual Studio Code WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) and click **Install**.


# Setup environment

## Create an account
First create an account on https://huggingface.co/runwayml/stable-diffusion-v1-5 and click on **Agree and access repository**

## Then on WSL Ubuntu
```shell
# adding source for packages: libcudnn8 libcudnn8-dev
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"

# install all required packages on Ubuntu
sudo apt-get update
sudo apt-get -y install git-lfs python3 python3-pip libcudnn8 libcudnn8-dev cuda

# the repository is around 32GB so it'll take a considerable ammount of time to clone
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
pip install --upgrade diffusers[torch] transformers
```
> During clone `git lfs` will require you to enter your _username_ and _password_ of huggingface.co a couple times.

On _Visual Studio Code_ connected to _Ubuntu_ you'll need to have extension `ms-python.python` installed.

# Run your own
You're ready now to run an attemp, assure your path to `stable-diffusion-v1-5` is correct relatively to your repo. Change the `prompt` to whatever suites your will. Assure you have specified `filename.png` the code will overwrite **without** confirmation.

 ```Python
import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("../stable-diffusion-v1-5", torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to("cuda")

prompt = "intricate steampunk portrait of a person as king, smooth, sharp focus"
image = pipe(prompt).images[0]
image.save("filename.png")
 ```
