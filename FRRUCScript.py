import os
import re


def correctNameFile(file, dirs):
    if file.endswith(("mkv", "mp4", "mkv", "flv", "wmv", "avi", "mpg", "mpeg", "mp3", "avi", "dat")):
        name, extension = os.path.splitext(file)
        result = re.sub("[\(\[].*?[\)\]]", "", name).strip()
        episode_number = [int(s) for s in result.split() if s.isdigit()]
        if len(episode_number) == 1:
            episode_number = episode_number[0]
        else:
            episode_number = "Movie"
        name = ' '.join(i for i in result.split() if i.isalpha())
        result = "{} - {}{}".format(name, episode_number, extension)
        print(result)
        # os.rename(file, result)
        os.rename(os.path.join(dirs, file), os.path.join(dirs, result))


path = "."
for subdir, dirs, files in os.walk(path):
    for file in files:
        correctNameFile(file, subdir)
