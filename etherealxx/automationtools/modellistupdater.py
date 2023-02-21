import os
from time import sleep

curdir = os.path.realpath(__file__)
maindir = os.path.abspath(os.path.join(curdir, "../../"))
ipynbpath = os.path.join(maindir, "etherportal.ipynb")

print("wait a few seconds...")
sleep(1)
print()

models = []
# Open the markdown file for reading
with open(ipynbpath, "r", encoding='UTF-8') as file:
    lines = file.readlines()

# Find the line that contains "## Model Comparison (NSFW)"
for index, line in enumerate(lines):
    if '"if Model_to_download==' in line.strip():
        #strippedline = line.strip().lstrip("\"if Model_to_download=='").rstrip("':\\n\",")
        #strippedmodel = line.strip().strip("\"").rstrip("':\\n\",").lstrip("\"if Model_to_download==").strip("'")
        strippedmodel = line.strip().replace("\"if Model_to_download=='", "").replace("':\\n\",", "")
        print(strippedmodel)
        models.append(strippedmodel)

print()

thestring = "Model_to_download="
count = 0
for item in models:
    if count==0:
        thestring += f'"{item}" #@param [ "{item}"'
        count +=1
    else:
        thestring += f', "{item}"'

thestring += ']'
print(thestring)
    #Model_to_download="Anythingv3" #@param [ "Anythingv3", "Eimis", "EvtV3", "ACertain", "ElysiumV3", "Wlop-any", "WaifuDiffusion-Vae", "LeafMix", "Abyss7thLayer", "Healys", "LigneClaire", "KriboMix", "InizioSkinjob", "PantyStocking", "WaifuBodyBlenderMix", "StuffyMix", "AbyssOrangeMix2", "BerryMix", "Systemy-CSR", "ElyOrangeMix", "AnyTwamMix", "DarkberryMix", "Grapefruit", "Mitsudoue"]