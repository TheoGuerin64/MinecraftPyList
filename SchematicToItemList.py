def getItemListFromNbt(file):
    from nbtlib import load

    #Get schematic infos
    nbtFileRoot = load(file).root
    palette = nbtFileRoot['palette']
    pos = nbtFileRoot["blocks"]

    #Get blocks
    blocks = {}

    for i in range(len(palette)):
        blocks[i] = str(palette[i]["Name"]).replace('"','').replace("minecraft:","").replace("_"," ").title()

    #Get number of blocks
    block_list = {}

    for i in range(len(pos)):
        if blocks[int(pos[i]['state'])].title() in block_list:
            block_list[blocks[int(pos[i]['state'])]] += 1
        else:
            block_list[blocks[int(pos[i]['state'])]] = 1

    return block_list

def getItemListFromTextFile(file):
    with open(file, "r") as file:
        fileText = file.read()

        itemList = {}

        for item in fileText.split("\n"):
            itemSep = item.split(":")
            itemList[itemSep[0]] = int(itemSep[1])

        return itemList
