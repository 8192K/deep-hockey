import cv2
from empatches import EMPatches

pano_img = cv2.imread('arena.jpg')
pano_height = pano_img.shape[0]
new_img = cv2.imread('/mnt/data/videos/sampling/excerpt/eck_evn_per1_0088.jpg')
print(pano_height)

# Use the EMPatches lib to extract overlapping images. This works perfectly fine. 
# img_patches is a list of np.array, usable in OpenCV
emp = EMPatches()
img_patches, _ = emp.extract_patches(pano_img, pano_height, overlap=0.4)

img_patches.append(new_img)

stitcher = cv2.Stitcher_create()
status, output = stitcher.stitch(img_patches)
# Returns status 0 and output is the original panorama perfectly stitched.
# The new image was ignored.

cv2.imwrite('arena_stitched.jpg', output)
