import os
import csv
import shutil

def set_files_in_dir(root_dir, prefix):
    files = os.listdir(root_dir)
    for file in files:
        path = os.path.join(root_dir, file)
        folder_list.append(path)

def set_files_list(root_dir):
    files = os.listdir(root_dir)
    for file in files:
        wav_list.append(file)

folder_list = []
root_dir = "dataset"
violence_flag = 1
violence_class = ['notviolence', 'violence']

set_files_in_dir(root_dir, "")
print(folder_list)

f = open('pock.csv', 'w', encoding='utf-8')
wr = csv.writer(f)
wr.writerow(['name', "classID", 'class', 'fold'])
for folder in folder_list:
    wav_list = []
    set_files_list(folder)
    wav_length = len(wav_list)
    #count = 0
    folder_name = folder.split('_')

    if folder_name[-1] == 'violence':
        violence_flag = 1
        vi_class = violence_class[1]

    else:
        violence_flag = 0
        vi_class = violence_class[0]

    for wav in wav_list:
        '''
        if count >= train_length:
            fold = '12'
        else:
            fold = '11'
        count += 1
        '''
        fold = '12' if folder_name[0] == 'dataset/test' else '11'

        try:
            move_file_name = os.path.join(folder, wav)
            shutil.move(move_file_name, 'UrbanSound8K/audio/fold{}'.format(fold))
            wr.writerow([wav, violence_flag, vi_class, fold])

        except FileExistsError:
            continue

print('finish')

f.close()