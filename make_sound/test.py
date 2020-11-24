import librosa
import numpy as np
import csv

# 파일 자르는 함수
def right_shift_wav(wav_file_name, i, shift_time, root_dir, org_wav_dir):
    y, sr = librosa.load(org_wav_dir+wav_file_name, sr=16000)
    cut_time = len(y)*(40-(shift_time * (i+1))) / 40
    y1 = y[:round(cut_time)]
    y2 = y[round(cut_time):]
    outputWav = np.hstack((y2, y1))
    librosa.output.write_wav(root_dir+wav_file_name+'_right_shift{}.wav'.format(str(i).zfill(4)), outputWav, sr)
    return wav_file_name+'_right_shift{}.wav'.format(str(i).zfill(4))

def left_shift_wav(wav_file_name, i, shift_time, root_dir, org_wav_dir):
    y, sr = librosa.load(org_wav_dir+wav_file_name, sr=16000)
    cut_time = len(y)*shift_time*(i+1) / 40
    y1 = y[:round(cut_time)]
    y2 = y[round(cut_time):]
    outputWav = np.hstack((y2, y1))
    librosa.output.write_wav(root_dir+wav_file_name+'_left_shift{}.wav'.format(str(i).zfill(4)), outputWav, sr)
    return wav_file_name+'_left_shift{}.wav'.format(str(i).zfill(4))

def shift_and_makeCSV():
    csv_name = 't2_res_9999.csv'
    re_csv_file = 'final_csv.csv'
    f = open(csv_name, 'r', encoding='utf-8')
    re_f = open(re_csv_file, 'w', encoding='utf-8')
    lines = csv.reader(f)
    wr = csv.writer(re_f)

    shift_time = 2
    org_wav_dir = 'wav_file/' # 원래 있던 파일 경로
    root_dir = 're_wav/' # 새로운 파일 경로 민재꺼랑 합칠때는 원래 경로 넣어주면 될듯
    print('---------------shift start-------------------')
    for line in lines:
        print(line)
        shift_r_time = (40 - int(line[2]))//shift_time
        shitr_l_time = int(line[1])//shift_time
        wr.writerow([line[0], line[1], line[2]])

        if shift_r_time > 0:
            for i in range(shift_r_time - 1):
                file_name = right_shift_wav(line[0], i, shift_time, root_dir, org_wav_dir)
                start_time = int(line[1]) + (2*(i+1))
                end_time = int(line[2]) + (2*(i+1))
                wr.writerow([file_name, start_time, end_time])
            print('shift_r finish')

        if shitr_l_time > 0:
            for i in range(shitr_l_time - 1):
                file_name = left_shift_wav(line[0], i, shift_time, root_dir, org_wav_dir)
                start_time = int(line[1]) - (2*(i+1))
                end_time = int(line[2]) - (2*(i+1))
                wr.writerow([file_name, start_time, end_time])
            print('shift_l finish')

    re_f.close()
    f.close()

#민재꺼 여기다 넣어서 csv 파일
shift_and_makeCSV()