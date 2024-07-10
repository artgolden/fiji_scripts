# @ File (label='Choose image to expand canvas') image_path
# @ File (label='Choose an output directory', style='directory') output_dir
# @ Integer (label='How to rotate the image?', style="slider", min=-90, max=180, stepSize=90, value=90) rotation_angle


""" A script to rotate image around Y axis. Applicable to a folder with batch processing."""

import os
from ij import IJ, WindowManager
from ij.io import FileSaver


def save_tiff_simple(image, path):
    if os.path.exists(path):
        os.remove(path)
    fs = FileSaver(image)
    fs.saveAsTiff(path)


image_path = image_path.getAbsolutePath()
output_file_path = os.path.join(
    output_dir.getAbsolutePath(), os.path.basename(image_path)
)


imp = IJ.openImage(image_path)
IJ.run(imp, "TransformJ Turn", "z-angle=0 y-angle=%i x-angle=0" % rotation_angle)
imgOut = WindowManager.getCurrentImage()
save_tiff_simple(imgOut, output_file_path)
imgOut.close()
