phe_pham = ["CUON CAM", "CACBON TAY CHOI","HAN CHOI","HAN CHAU","DE VO NHO","TU DIEN", "CONG CHAU DIEN","BUI CHI"]
all_cam = ["CAM 1","CAM 2","CAM 3","CAM 4"]

tt = 0
for pp in range(len(phe_pham)):
    for al in range(len(all_cam)):
        print(f"{tt}"," ",all_cam[al] + " " + phe_pham[pp])
        tt+=1