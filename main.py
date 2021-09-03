import os
import json
import pygame


def play(music_file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(music_file_path)
    pygame.mixer.music.play()


def n_or_c():
    print("Type 'n' for noisy and 'c' for clear")
    value = input()
    while value not in ("n", "c"):
        print("n or c")
        value = input()
    if value == 'n':
        value = 'Noisy'
    else:
        value = 'Clear'
    return value


def checking(file_path):
    file_list = os.listdir(file_path)
    names = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(file_path, f)) and f.lower().endswith(".mp3")
    ]
    final_dic = {}
    for file in names:
        print(f'Now playing: {file}')
        play(file_path + "/" + file)
        final_dic[file] = n_or_c()
    return final_dic


def create_json_from_dictionary(dictionary):
    with open("result.json", "w") as outfile:
        json.dump(dictionary, outfile)
    print("File Generated")


if __name__ == '__main__':
    # C:\Users\blablaUser\mySmallMusicFolder
    print("Please input your sound files directory path: ")
    path = input()
    data = checking(path)
    create_json_from_dictionary(data)
