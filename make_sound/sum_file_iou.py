import csv

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


def sum_iou(score_csv, iou_sum_scv):
    name_list, iou_list = make_list(score_csv)
    rec_f = open(iou_sum_scv, 'w', encoding='utf-8')
    wr = csv.writer(rec_f)
    score_temp = 0
    file_length = len(name_list)-1
    for i in range(file_length):
        score_temp += float(iou_list[i])
        if i == file_length - 1:
            if name_list[i] != name_list[i+1]:
                wr.writerow([name_list[i], score_temp])
                wr.writerow([name_list[i+1], iou_list[i+1]])

            else:
                score_temp += float(iou_list[i+1])
                wr.writerow([name_list[i], score_temp])

        else:
            if name_list[i] != name_list[i+1]:
                wr.writerow([name_list[i], score_temp])
                score_temp = 0

    rec_f.close()

score_csv = 'score_csv.csv'
iou_sum_scv = 'iou_list.csv'