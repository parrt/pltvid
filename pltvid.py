import matplotlib.pyplot as plt
import random
import PIL
import os

class Capture:
    def __init__(self, dpi=300, save_frames=False):
        self.frame = 0
        self.dpi = dpi
        self.save_frames = save_frames
        self.frame_filename = f"frame-{int(random.randrange(10000, 99999))}"
        self.frame_format = 'png'

    def snap(self, n=1):  # save one or more frames of current picture
        for i in range(n):
            self.frame += 1
            plt.savefig(
                f"/tmp/{self.frame_filename}-{self.frame:05d}.{self.frame_format}",
                bbox_inches=0, pad_inches=0, dpi=self.dpi)
        plt.close()

    def save(self, filename, duration=100, loop=0):
        images = [PIL.Image.open(image) for image in
                  [f"/tmp/{self.frame_filename}-{i:05d}.{self.frame_format}"
                   for i in range(1, self.frame + 1)]]
        if not filename.endswith(".gif"):
            raise ValueError(f"Can only save movies as GIFs: {filename}")
        images[0].save(filename,
                       save_all=True,
                       append_images=images,
                       duration=duration,
                       loop=loop)
        if not self.save_frames:
            # remove temp files
            for image in [f"/tmp/{self.frame_filename}-{i:05d}.{self.frame_format}" for i
                          in range(1, self.frame + 1)]:
                os.remove(image)