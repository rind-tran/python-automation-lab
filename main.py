# import modules
import os
from os.path import splitext, exists, join
from shutil import move


# variables
source_dir = "C:\\Users\\Adm\\Downloads"
image_dest_dir = "D:\\Downloads\\image"
video_dest_dir = "D:\\Downloads\\video"
audio_dest_dir = "D:\\Downloads\\audio"
document_dest_dir = "D:\\Downloads\\document"
compress_dest_dir = "D:\\Downloads\\compress"
other_dest_dir = "D:\\Downloads\\other"
image_extensions = (".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico")
video_extensions = (".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd")
audio_extensions = (".m4a", ".flac", "mp3", ".wav", ".wma", ".aac")
document_extensions = (".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx")
compress_extensions = (".zip", ".tar", ".gz", ".rar")


def move_file(path, new_path, file_name):
    # variable to store source = path/filename
    source = join(path, file_name)
    # Check if file name exit and rename it
    count = 1
    while exists(f"{new_path}/{file_name}"):
        root, ext = splitext(file_name)
        file_name = f"{root}str({count}){ext}"
        count += 1
    # variable to store source = path/filename
    dest = join(new_path, file_name)
    # Move file
    move(source, dest)


def check_type(file_name):
    if file_name.endswith(image_extensions):
        return image_dest_dir
    elif file_name.endswith(video_extensions):
        return video_dest_dir
    elif file_name.endswith(audio_extensions):
        return audio_dest_dir
    elif file_name.endswith(document_extensions):
        return document_dest_dir
    elif file_name.endswith(compress_extensions):
        return compress_dest_dir
    else:
        return other_dest_dir


def main():
    # Check file type
    with os.scandir(source_dir) as entries:
        for entry in entries:
            file_name = entry.name
            dest_dir = check_type(file_name)
            move_file(source_dir, dest_dir, file_name)


if __name__ == "__main__":
    main()
