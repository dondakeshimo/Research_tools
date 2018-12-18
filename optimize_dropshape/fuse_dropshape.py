from PIL import Image


sim_drop = Image.open("sim_dropshape.png")
real_drop = Image.open("real_drop_images/image0001.png")
sim_drop.size
real_drop.size
sim_drop
sim_drop.getpixel((100, 100))
252
216


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result


sim_drop_mergin = add_margin(sim_drop, 108, 126, 108, 126, (255, 255, 255))
sim_drop_mergin.getpixel((1, 1))
real_drop.getpixel((1, 1))
real_drop.putalpha(256)
real_drop.getpixel((1, 1))
Image.blend(sim_drop_mergin, real_drop, 0.5)
