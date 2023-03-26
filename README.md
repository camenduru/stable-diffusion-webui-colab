## 🦒 Training Colabs (GPU)

| Colab Page | Function
| --- | --- |
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/training/simple_dreambooth_trainer.ipynb) | Simple DreamBooth Trainer
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/training/simple_lora_trainer.ipynb) | Simple LoRA Trainer
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/training/advanced_trainer.ipynb) | Advanced Trainer 🚦WIP🚦

### How To Use Simple DreamBooth Trainer

- https://www.youtube.com/watch?v=5dK1altO4Qw
- Find someone famous who looks like you in the stable diffusion universe (use: https://starbyface.com to find and https://rom1504.github.io/clip-retrieval to search)
- I will try to train a Stable Diffusion model for the streamer Hachubby. 
- I will use Park Min-young as a reference, but the prompt keyword will be 'parkminyoung'
- Create a new drive folder MyDrive/AI/training/parkminyoung, crop photos (512x512) with https://www.birme.net, then add photos
- Set instance_prompt: parkminyoung, click play button
- Convert diffusers to original stable diffusion (parkminyoung.ckpt) and use with your favorite WebUI
- If you want, you can send the model to Hugging Face

### How To Use Simple LoRA Trainer

 - https://www.youtube.com/watch?v=bt0tEVgiAf4

## 🦒 Community [@kohya-ss](https://github.com/kohya-ss) ❤ Training Colabs (GPU)
 
| Colab Page | Function | Author | Readme Page
| --- | --- | --- | --- |
[![Open in GitHub](https://user-images.githubusercontent.com/54370274/227776188-a9e140f7-a8c6-4e41-adbb-02c71b71ae80.svg)](https://github.com/Linaqruf/kohya-trainer) | Trainer Colabs | [@Linaqruf](https://github.com/Linaqruf) |  https://github.com/Linaqruf/kohya-trainer
[![Open in GitHub](https://user-images.githubusercontent.com/54370274/227776188-a9e140f7-a8c6-4e41-adbb-02c71b71ae80.svg)](https://github.com/ddPn08/kohya-sd-scripts-webui) | Web UI extension and standalone colab | [@ddPn08](https://github.com/ddPn08) | https://github.com/ddPn08/kohya-sd-scripts-webui
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hollowstrawberry/kohya-colab/blob/main/Dataset_Maker.ipynb) | Dataset Maker | [@Hollowstrawberry](https://github.com/hollowstrawberry) | https://github.com/hollowstrawberry/kohya-colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hollowstrawberry/kohya-colab/blob/main/Lora_Trainer.ipynb) | Lora Trainer | [@Hollowstrawberry](https://github.com/hollowstrawberry) | https://github.com/hollowstrawberry/kohya-colab
 
### Licenses
https://github.com/kohya-ss/sd-scripts/blob/main/LICENSE.md <br />
https://github.com/huggingface/diffusers/blob/main/LICENSE <br />
