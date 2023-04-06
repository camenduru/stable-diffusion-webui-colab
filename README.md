## 🦒 Install the WebUI Colab to Google Drive

| Colab Page | Function
| --- | --- |
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/drive/install.ipynb) | One Time Install & Update
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/drive/run.ipynb) | Run
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camenduru/stable-diffusion-webui-colab/blob/drive/add.ipynb) | Add Model

## Tutorials
Stable Diffusion WebUI Colab With Google Drive: https://www.youtube.com/watch?v=njW64feGMzI

🚨 Important for 15G Free Google Drive Users: 

If you want to use more models, you can download your model into Colab, which has an empty 50GB space. 

Download models into `/content/models` WebUI automaticly will find your models under `/content/models` and `/content/drive/MyDrive/stable-diffusion-webui-colab/stable-diffusion-webui/models/Stable-diffusion`

![Screenshot 2023-03-20 133516](https://user-images.githubusercontent.com/54370274/226315414-2dcc8308-c15f-4a96-8d75-507e46d5b1bc.png)

```py
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/andite/pastel-mix/resolve/main/pastelmix-fp16.ckpt -d /content/models -o pastelmix-fp16.ckpt
!aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt -d /content/models -o pastelmix-fp16.vae.pt
```

You can also free up more space by deleting the default model in your drive.

![Screenshot 2023-02-24 140908](https://user-images.githubusercontent.com/54370274/221165025-706b6385-8cb2-4fe1-9334-2762013b9dce.png)

If you don't plan to use ControlNet models, you can also free up space by deleting them. (thanks to twitter@muadoyoki ❤)

![Screenshot 2023-02-24 141259](https://user-images.githubusercontent.com/54370274/221165764-b4db7c3c-0cc9-4976-a922-395bb72a002d.png)
