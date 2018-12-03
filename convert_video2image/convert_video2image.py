import ffmpeg
import glob
import os


def make_out_dir_name(video_path):
    out_dir = video_path.replace(".mpg", "")
    print(out_dir)
    out_dir = video_path.replace("¥¥", "/")
    print(out_dir)
    out_dir = out_dir.split("/")[-1]
    print(out_dir)
    out_dir = "./images/" + out_dir
    print(out_dir)

    return out_dir


def convert_video2image(v_path, out_dir):
    out_path = "{}/image%04d.png".format(out_dir)
    stream = ffmpeg.input(v_path)
    stream = ffmpeg.output(stream, out_path, r=5, vf="scale=684:504")
    ffmpeg.run(stream)


def main():
    video_path = glob.glob("./videos/*.mpg")

    for v_path in video_path:
        out_dir = make_out_dir_name(v_path)

        if os.path.isdir(out_dir):
            continue
        else:
            os.mkdir(out_dir)

        convert_video2image(v_path, out_dir)


if __name__ == "__main__":
    main()
