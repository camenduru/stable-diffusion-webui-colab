## 🦒 Training Colab GPU

| Colab Page | Function
| --- | --- |
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/training/train.ipynb) | Train DreamBooth & (LoRA 🚦WIP🚦)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/training/train_dreambooth_standalone.ipynb) | Train DreamBooth Standalone

## How To Use
- Find someone famous looks like you in the stable diffusion universe (find with: https://starbyface.com) (search with: https://rom1504.github.io/clip-retrieval)
- Example I will try train streamer jinnytty
- I will use Park Min-young but the prompt keyword will be `parkminyoung`
- Create a new drive folder `MyDrive/AI/training/parkminyoung` crop photos (512x512) with https://www.birme.net then add photos
- Go to the Diffusers tab and click on `Train DreamBooth`
- Go to the Diffusers Test tab and test your model using the `parkminyoung person drawing` template `instance_prompt class_prompt your_prompt`
- Go to the Convert DreamBooth tab and click on `Convert Diffusers to Original Stable Diffusion`
- If you want to send it to HuggingFace, use the HuggingFace tab `Push File to 🤗 Hugging Face`

## Licenses
https://github.com/huggingface/diffusers/blob/main/LICENSE
