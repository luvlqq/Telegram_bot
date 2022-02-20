import glob
import random

def pic_floder():
    print(glob.glob('*.jpg')) #['IMG_7599.JPG','IMG_7600.JPG']
    print(random.choice(glob.glob('./images/*')))
