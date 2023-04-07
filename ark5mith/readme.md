Configuration and Customization 
======


---
Fork the config from https://github.com/ark5mith/sd-configs
****
Notebooks

|  Link | Function or Name | Readme Page
| --- | --- | --- | 
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ark5mith/stable-diffusion-webui-colab/blob/community/ark5mith/INSTALL-UPDATE_ConfigDrive_Colab_Kaggle.ipynb) | ConfigDrive Install/Update | [Readme](https://colab.research.google.com/github/ark5mith/stable-diffusion-webui-colab/blob/community/ark5mith/INSTALL-UPDATE_ConfigDrive_Colab_Kaggle.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ark5mith/stable-diffusion-webui-colab/blob/community/ark5mith/RUN_ConfigDrive_Colab_Kaggle.ipynb) | ConfigDrive Run | [Readme](https://github.com/ark5mith/stable-diffusion-webui-colab/blob/community/ark5mith/readme.md)
[![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/roykent/stablediffusionwebui-configured) | ConfigKaggle | [Readme](https://github.com/ark5mith/stable-diffusion-webui-colab/blob/community/ark5mith/readme.md)

****

This is customized notebook from [Camenduru Drive colab notebook](https://github.com/camenduru/stable-diffusion-webui-colab/tree/drive)

With main feature is config files working in both kaggle and colab
---

Store style and edit in git, use in colab and kaggle
---
<img width="431" alt="image" src="https://user-images.githubusercontent.com/115693126/230573582-acc8593e-c9ad-48bf-a44c-3d0dfd3056b5.png"> Imagine never using style in colab <img width="185" alt="image" src="https://user-images.githubusercontent.com/115693126/230579988-79aa8f9c-68f2-491f-9888-af6da5d58297.png">


Store webui config and edit in git, unlock the limitation and adjust default prompt, setting, sliders.
---
<img width="461" alt="image" src="https://user-images.githubusercontent.com/115693126/230573714-3d14411f-d5fc-40d8-b2fe-e0584e22969f.png">

***COLAB GOOGLE DRIVE SPECIFIC FEATURE***
===

Give some extension a try just by pasting link, then use install/update notebook
---
<img width="930" alt="image" src="https://user-images.githubusercontent.com/115693126/230574006-2ba4919d-b23f-4c58-910e-7629af156e2a.png">


However model you want, create custom name, paste the link, then use install/update notebook
---
<img width="305" alt="image" src="https://user-images.githubusercontent.com/115693126/230573411-5f80c2a3-30b7-4a43-a376-72e76b3c6e2a.png">



Running the Install/Update Colab Notebook [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ark5mith/stable-diffusion-webui-colab/blob/community/ark5mith/INSTALL-UPDATE_ConfigDrive_Colab_Kaggle.ipynb)
---

1. This cell is for downloading models. 
You put the model name then the links. 
Write one model for one line so you can ignore it using `#` easily.
If you have already downloaded the model into Google Drive, you don't need to add them here. 
It will be available until you delete them from Google Drive.


<img width="919" alt="image" src="https://user-images.githubusercontent.com/115693126/230466122-e393b018-ff19-43af-a9d7-0abd62898816.png">

2. This cell is for downloading and updating extensions. Just put the links accordingly.

<img width="761" alt="image" src="https://user-images.githubusercontent.com/115693126/230468937-614553d1-0f94-457d-a6ed-3dfc71808860.png">

3. This cell setup installation directory. You can use `/content/drive/MyDrive` or anything else. The form below that is not necessary to fill or edit.

<img width="713" alt="image" src="https://user-images.githubusercontent.com/115693126/230469143-be57f1b3-70b4-4ef4-b471-920e0ebe5320.png">

4. This is Definition cell. Leave as it is. 

<img width="395" alt="image" src="https://user-images.githubusercontent.com/115693126/230469469-e2edf195-55cd-4299-ac2c-ee0725e9e69a.png">

5. This is Dependencies cell. That checkboxes is a gimmick because regardless what you pick, it will assume you do it wrong and fact check.

<img width="251" alt="image" src="https://user-images.githubusercontent.com/115693126/230469792-17b442d0-16d6-4864-8790-75a260b62556.png">

6. This is the final cell, Install. You don't need GPU for this. You can start Run All since step 4 LMAO

<img width="143" alt="image" src="https://user-images.githubusercontent.com/115693126/230469943-eaaa105e-55e9-44b8-805c-a3febb91b0f0.png">

To disable GPU, go to Runtime>Change runtime type and select none

<img width="464" alt="image" src="https://user-images.githubusercontent.com/115693126/230470172-9c9e79e1-bdb5-4802-90b6-18360504a4de.png">


****

Running the Run Colab Notebook [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ark5mith/stable-diffusion-webui-colab/blob/community/ark5mith/RUN_ConfigDrive_Colab_Kaggle.ipynb)
---

1. There are a lot of configuration that is pretty self explanatory

<img width="518" alt="image" src="https://user-images.githubusercontent.com/115693126/230470693-ed0e03ca-e0c7-467d-baf2-4128e3fd89fd.png">

2. Arguments. Have some debates. I don't know what clip use is but NIKE. Actually it is blue because it have link. Also have text based form.

<img width="628" alt="image" src="https://user-images.githubusercontent.com/115693126/230471349-21135a22-649a-4ece-b44b-e9f89cf172d3.png">
<img width="219" alt="image" src="https://user-images.githubusercontent.com/115693126/230473432-7991a644-55ce-465a-a0a2-c4c78e5784a6.png">

<img width="661" alt="image" src="https://user-images.githubusercontent.com/115693126/230471705-0bfe23f4-d907-4895-9e0b-a556703984ad.png">

3. ngrok tunnel. Automatically disabled if no token/files found even when enabled. Cool right.

<img width="475" alt="image" src="https://user-images.githubusercontent.com/115693126/230471824-797ab4d8-87dc-413b-b24c-f2186749e1db.png">

4. enable `share_link` is to get tunnel from gradio. Even if disabled, auth still run in other tunnel. Basically you want to lock the public link(s). Create new passsword and username, otherwise default password is `password` and default username is `username`

<img width="859" alt="image" src="https://user-images.githubusercontent.com/115693126/230472039-a15b1aa3-8c8d-48d5-993c-04a32ab0c929.png">

5. This sounds cool but honestly i don't know

<img width="818" alt="image" src="https://user-images.githubusercontent.com/115693126/230472553-ba0c865c-a581-4b04-a58e-6895be09345f.png">

7. Nothing to do here. Yes the number skipped, i'm not sleepy. It's like when tied, you pick the lowest rank.

<img width="413" alt="image" src="https://user-images.githubusercontent.com/115693126/230472991-c6f8f53e-e244-4bc3-a65b-76e36273b78f.png">

8. Stop scrolling. You can run all since step 4

<img width="636" alt="image" src="https://user-images.githubusercontent.com/115693126/230473116-bfa033b6-0584-49c4-bfa8-010dda3adc59.png">




Big thanks to Camenduru 💌 for always up to date and reliable colab

Thanks to [ChatGPT](https://chat.openai.com/chat) for providing 24/7 assistance. You can look how dependent i'm in [using ChatGPT](https://sharegpt.com/c/Z8KX0c4)

Special thanks ✌ [ddPn08](https://github.com/ddpn08/) and [viyiviyi](https://github.com/viyiviyi) for their inspiring notebook

Now into Kaggle


****

Running the *compute limit reached so i need alternative* Notebook [![Open In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code/roykent/stablediffusionwebui-configured)
---
0. Make sure to copy and edit my notebook or camenduru one to gain the exact same environment (noticeable in input)

<img width="250" alt="image" src="https://user-images.githubusercontent.com/115693126/230475435-d487b4ac-7e52-430e-8f97-9733a651cd29.png">

0.5  If you are first time using kaggle, you need to verify with phone number to gain GPU access. Don't forget to enable INTERNET. Keep environment as `Pin to Original` to avoid broken codes. GPU P100 is notably faster than T4, as the notebook unable to utilize dual GPU.

<img width="242" alt="image" src="https://user-images.githubusercontent.com/115693126/230475482-84104841-3681-4429-b946-172f2e2670b1.png">

1.  Edit the config. Use `/kaggle` for more space. Use `/kaggle/working` for persistency (meaning you will regain the installed stuff when you launch the notebook again, but loading is slow and storage is small). Edit the git link with your fork link.

<img width="496" alt="image" src="https://user-images.githubusercontent.com/115693126/230473863-9832c22b-3fcd-40be-9dc5-9b7071435db6.png">

2. You can add extension in this part of notebook

<img width="830" alt="image" src="https://user-images.githubusercontent.com/115693126/230476240-de47141a-1c2b-46dd-9c34-3618ef8a907c.png">

3. Models. Remove `#` to download other models i prepared. 

<img width="831" alt="image" src="https://user-images.githubusercontent.com/115693126/230476351-0bba38a7-afce-40d7-bbd0-7f8f79812816.png">

4. Ready and run all


***
[Configuring Stable Diffusion WEBUI](https://github.com/ark5mith/sd-configs)

Go to dist folder in your fork and edit any file 

<img width="567" alt="image" src="https://user-images.githubusercontent.com/115693126/230477213-80faf581-0d43-4ca1-8843-6b3542962d5e.png">

Edit styles in `style.csv`. Style Name- Prompt - Negative Prompt

<img width="924" alt="image" src="https://user-images.githubusercontent.com/115693126/230477488-30121fe2-a811-4417-9328-6483a27533dc.png">

Edit default WebUI in `sd-config.json`. Like default prompt, step, size, sampling, etc. Unlock step and modify slider limits. Change default language if you install language extension. Anything. Stop wasting time inputing numbers and playing slider!

<img width="383" alt="image" src="https://user-images.githubusercontent.com/115693126/230477745-955b5d94-76f0-4ad2-a905-e372c49a8dfb.png">

Edit default Settings tab of WebUI in `config.json`. Stop reloading WebUI to configure setting each time you run a notebook, less time wasted!
<img width="674" alt="image" src="https://user-images.githubusercontent.com/115693126/230577066-4f827926-2f25-4e11-bb41-175498aad11a.png">


---
