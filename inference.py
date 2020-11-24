import torch
import os

from run import infer_main

all_file_path = [] #여기에다가 경로를 다 담은다음에 for문을 돌림.
predict_result = []

def infer_set_files_list(root_dir):
    files = os.listdir(root_dir)
    for file in files:
        file = os.path.join('testset', file)
        all_file_path.append(file)

def cls_infer():
    infer_set_files_list('testset')#디렉토리 안에 있는 파일 목록을 다 all_file_path에다가 저장해줌.
    print(all_file_path)
    check_path = 'saved_cv/0727_083149/checkpoints/model_best.pth'  # chechpoint경로

    checkpoint = torch.load(check_path)
    config = checkpoint['config']
    cls = 0
    file_list_length = len(all_file_path)
    count = 0


    for file_path in all_file_path:
        answer = []
        label, conf = infer_main(file_path, config, checkpoint)
        cls = 1 if label == 'violence' else 0
        answer.append(file_path)
        answer.append(cls)
        predict_result.append(answer)
        if cls == 0:
            count += 1
    print(file_list_length)
    print(count/file_list_length*100)
    return predict_result

cls_infer()
