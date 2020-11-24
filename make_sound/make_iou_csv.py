import csv
import numpy as np

def make_g_list(g_csv):
    gf = open(g_csv, 'r', encoding='utf-8-sig')
    g_lines = csv.reader(gf)

    name_list = []
    start_list = []
    end_list = []

    for i in g_lines:
        if i[0] != 'name':
            name_list.append(i[0])
            start_list.append(i[1])
            end_list.append(i[2])

    gf.close()
    return name_list, start_list, end_list

def make_list(g_csv):
    gf = open(g_csv, 'r', encoding='utf-8-sig')
    g_lines = csv.reader(gf)

    name_list = []
    iou_list = []

    for i in g_lines:
        if i[0] != 'name':
            name_list.append(i[0])
            iou_list.append(i[3])
    gf.close()
    return name_list, iou_list

def cal_iou(iou_list):
    p = np.sort(iou_list)
    iou = (p[2] - p[1]) / (p[3] - p[0])
    return iou

def make_score_csv(g_csv, p_csv, record_csv):
    name_list, start_list, end_list = make_g_list(g_csv)
    pf = open(p_csv, 'r', encoding='utf-8-sig')
    rec_f = open(record_csv, 'w', encoding='utf-8')
    p_lines = csv.reader(pf)
    wr = csv.writer(rec_f)

    wr.writerow(['name', 'start', 'end', 'iou'])
    for p_line in p_lines:
        if p_line[0] != 'name':
            for i in range(len(name_list)):
                if p_line[0] == name_list[i]:
                    p1, p2, p3, p4 = int(p_line[1]), int(p_line[2]), int(start_list[i]), int(end_list[i])
                    if p1 > p4  or p2 < p3:
                        iou = 0
                    else:
                        temp = [p1, p2, p3, p4]
                        iou = cal_iou(temp)
                    wr.writerow([p_line[0], p_line[1], p_line[2], iou])
                    break
    rec_f.close()
    pf.close()

def sum_iou(record_csv, iou_sum_scv):
    name_list, iou_list = make_list(record_csv)
    rec_f = open(iou_sum_scv, 'w', encoding='utf-8')
    wr = csv.writer(rec_f)
    score_temp = 0
    file_length = len(name_list) - 1
    for i in range(file_length):
        score_temp += float(iou_list[i])
        if i == file_length - 1:
            if name_list[i] != name_list[i + 1]:
                wr.writerow([name_list[i], score_temp])
                wr.writerow([name_list[i + 1], iou_list[i + 1]])

            else:
                score_temp += float(iou_list[i + 1])
                wr.writerow([name_list[i], score_temp])

        else:
            if name_list[i] != name_list[i + 1]:
                wr.writerow([name_list[i], score_temp])
                score_temp = 0
    rec_f.close()



#g_csv = 'g_csv.csv'             # 정답 csv 파일
#p_csv = 'p_csv.csv'             # 예측해서 나온 csv 파일
#record_csv = 'score_csv.csv'    # record될 파일 이름
iou_sum_scv = 'iou_list.csv'    # 파일들의 iou값들의 합이 담길 파일 이름 설정
#make_score_csv(g_csv, p_csv, record_csv)
#sum_iou(record_csv, iou_sum_scv)

def total_sum(iou_sum_scv):
    pf = open(iou_sum_scv, 'r', encoding='utf-8')
    p_lines = csv.reader(pf)
    temp = 0
    for line in p_lines:
        temp += float(line[1])
    print(temp)
    return temp

total_sum(iou_sum_scv)