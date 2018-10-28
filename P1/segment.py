import sys
from PIL import Image, ImageStat
import numpy as np
from scipy import misc, spatial

def eu(pix1, sea_mean, lake_mean, veg_mean, buildup_mean):
    sea_es = spatial.distance.euclidean(pix1, sea_mean)
    lake_es = spatial.distance.euclidean(pix1, lake_mean)
    veg_es = spatial.distance.euclidean(pix1, veg_mean)
    build_es = spatial.distance.euclidean(pix1, buildup_mean)
    devs = [sea_es, lake_es, veg_es, build_es]
    i = devs.index(min(devs))
    if i == 0:
        return 0
    if i == 1:
        return 75
    if i == 2:
        return 128
    if i == 3:
        return 255

def man(pix1, sea_mean, lake_mean, veg_mean, buildup_mean):
    sea_es = spatial.distance.cityblock(pix1, sea_mean)
    lake_es = spatial.distance.cityblock(pix1, lake_mean)
    veg_es = spatial.distance.cityblock(pix1, veg_mean)
    build_es = spatial.distance.cityblock(pix1, buildup_mean)
    devs = [sea_es, lake_es, veg_es, build_es]
    i = devs.index(min(devs))
    if i == 0:
        return 0
    if i == 1:
        return 75
    if i == 2:
        return 128
    if i == 3:
        return 255

if __name__ == '__main__':
    np.set_printoptions(threshold=np.inf)
    im_mat = misc.imread('mumbai.png')
    classes = ['sea', 'lake', 'builtup', 'vegetation']
    pixcount = np.zeros(3)
    mean = np.zeros(3)
    for imname in ['sea1.png', 'sea2.png', 'sea3.png']:
        im = Image.open(imname)
        stat = ImageStat.Stat(im)
        pixcount = pixcount + stat.count
        mean = mean + stat.sum
    mean = mean / pixcount
    sea_mean = np.int16(mean)
    pixcount = np.zeros(3)
    mean = np.zeros(3)
    for imname in ['vegetation1.png', 'vegetation2.png', 'vegetation3.png', 'vegetation4.png']:
        im = Image.open(imname)
        stat = ImageStat.Stat(im)
        pixcount = pixcount + stat.count
        mean = mean + stat.sum
    mean = mean / pixcount
    veg_mean = np.int16(mean)
    im = Image.open('builtup.png')
    stat = ImageStat.Stat(im)
    buildup_mean = np.int16(stat.mean)
    im = Image.open('lake.png')
    stat = ImageStat.Stat(im)
    lake_mean =np.int16(stat.mean)
    if sys.argv[1] == 'eu':
        out_mat = np.apply_along_axis(lambda x : eu(np.int16(x), sea_mean, lake_mean, veg_mean, buildup_mean), 2, im_mat)
        out = Image.fromarray(np.uint8(out_mat))
        out.save('segmented_eu.png')
    elif sys.argv[1] == 'man':
        out_mat = np.apply_along_axis(lambda x: man(np.int16(x), sea_mean, lake_mean, veg_mean, buildup_mean), 2, im_mat)
        out = Image.fromarray(np.uint8(out_mat))
        out.save('segmented_man.png')
    else:
        print('Unknown option')
