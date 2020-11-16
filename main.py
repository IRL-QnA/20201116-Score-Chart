#성적차트
elif sel == 5:
    print("\n\n>>>성적차트<<<")
    # 이중 포문
    for key, value in score.items():  # score에 있는 키=name, 값=value를 전체를 가져온다  
        sum = value['영어'] + value['수학'] # 키에 해당하는 영어, 수학 성적의 합계를 구함
        print("이름 :", key)
        print("총 점수 : ", end = "")
        for _ in range(sum // 10):  # 10점당 '*'표를 출력
            print("*", end = "")
        print("(%d점)" % sum)      # 총 점수 출력
        print("---------------------다음 학생") # 학생구분
