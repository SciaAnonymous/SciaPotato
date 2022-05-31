from pycocotools.coco import COCO
import numpy as np
import os
import matplotlib.pyplot as plt
import sys


if __name__ == '__main__':

    dataset_type = sys.argv[1] if len(sys.argv) > 1 else 'potato'

    annFile = f'./data/{dataset_type}/annotations/instances_train2017.json'
    img_root = f'./data/{dataset_type}/train2017'
    draw_bbox = dataset_type == 'grape'


    coco = COCO(annFile)

    catIds = []
    imgIds = coco.getImgIds(catIds=catIds)
    img = coco.loadImgs(imgIds[np.random.randint(0, len(imgIds))])[0]

    img_fname = img['file_name']

    I = plt.imread(os.path.join(img_root, img_fname))
    plt.imshow(I)

    annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
    anns = coco.loadAnns(annIds)
    coco.showAnns(anns,
                  draw_bbox=draw_bbox
                  )

    plt.axis('off')
    # plt.savefig("a.png", bbox_inches='tight')

    plt.show()

    # annFile = '/Users/px/Downloads/potato_dataset/annotations/instances_train2017.json'
    # coco = COCO(annFile)
    # img_names = [i['file_name'] for i in coco.imgs.values()]
    # path_root = '/Users/px/Downloads/potato_dataset/train2017'
    # for i in os.listdir(path_root):
    #     if i not in img_names:
    #         os.remove(os.path.join(path_root, i))