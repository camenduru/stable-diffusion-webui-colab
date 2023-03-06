## 🦒 Training Colabs (GPU)

| Colab Page | Function
| --- | --- |
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/training/train_dreambooth_standalone.ipynb) | Train DreamBooth Standalone
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/training/train_lora_standalone.ipynb) | Train LoRA Standalone

### How To Use Train DreamBooth Standalone

- https://www.youtube.com/watch?v=5dK1altO4Qw
- Find someone famous who looks like you in the stable diffusion universe (use: https://starbyface.com to find and https://rom1504.github.io/clip-retrieval to search)
- I will try to train a Stable Diffusion model for the streamer Hachubby. 
- I will use Park Min-young as a reference, but the prompt keyword will be 'parkminyoung'
- Create a new drive folder MyDrive/AI/training/parkminyoung, crop photos (512x512) with https://www.birme.net, then add photos
- Set instance_prompt: parkminyoung, click play button
- Convert diffusers to original stable diffusion (parkminyoung.ckpt) and use with your favorite WebUI
- If you want, you can send the model to Hugging Face

### Licenses
https://github.com/kohya-ss/sd-scripts/blob/main/LICENSE.md <br />
https://github.com/huggingface/diffusers/blob/main/LICENSE <br />