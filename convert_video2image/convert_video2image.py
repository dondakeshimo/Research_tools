import ffmpeg
import glob
import os


def main():
    video_path = glob.glob("./videos/*.mpg")

    for v_path in video_path:
        no_ext = v_path.replace(".mpg", "")
        no_ext = no_ext.split("/")[-1]

        if os.path.isdir(no_ext):
            continue
        else:
            os.mkdir(no_ext)

        out_path = "{}/image%03d.png".format(no_ext)
        stream = ffmpeg.input(v_path)
        stream = ffmpeg.output(stream, out_path, r=5)
        ffmpeg.run(stream)


if __name__ == "__main__":
    main()
