# 저장소 : score dict
# score 구성 : {이름:{영어:점수,수학:점수}}

# 전체 초기화
score = {}

# 합 초기화
sum = 0

# 메인화면 작업

while True: # 입력 숫자가 9가 나올때 까지 반복
    print("\n\n>>>메인메뉴<<<")
    print("==============")
    print("  1.성적입력")
    print("  2.성적출력")
    print("  3.성적삭제")
    print("  4.성적변경")
    print("  5.성적차트")
    print("  6.성적검색")
    print("  9.종    료")
    print("==============")
    sel= int(input("\n메뉴 선택=>"))
    if sel == 9: # 입력 숫자가 9가 되면 종료
        print("프로그램 종료")
        break
    
    # 성적입력
    if sel ==1:
        print("\n>>>성적입력<<<")
        iname = input("학생이름 입력=>")
        if iname in score: # 입력 받은 iname이 score 에 있는 경우
            print("이미 등록된 학생입니다")
        else: # # 입력 받은 iname이 score 에 없는 경우
            score[iname] = {}   # 성적 딕셔너리 초기화
            ieng = int(input("영어성적=>")) # 입력받은 영어 성적을 ieng라고 지정
            score[iname]['영어'] = ieng # 입력받은 ieng를 score 에 있는 [iname]["영어"]에 저장 

            imat = int(input("수학성적=>")) # 입력받은 수학 성적을 imat라고 지정
            score[iname]['수학'] = imat # 입력받은 imat를 score 에 있는 [iname]["수학"]에 저장 
            print("학생 성적이 등록되었습니다")
            
    # 성적출력
    elif sel == 2:
        print("\n\n>>>성적출력<<<")
        if len(score) == 0: # 성적이 없는 경우 
            print("출력할 학생성적이 없습니다")
        else: # 성적이 있는 경우
            for name, info in score.items(): # score에 있는 키=name, 값=info를 전체를 가져온다  
                print("이름:",name) 
                for k in info.keys(): # info안에서 키=k, 값=info[k]를 검색한다
                    print(k,":",info[k],end="\n")
                print()

    # 성적삭제
    elif sel == 3:
        print("\n\n>>>성적삭제<<<")
        iname = input("삭제할 학생이름 입력=>")
        if iname in score: # 입력 받은 iname이 score 에 있는 경우
            del(score[iname]) # 딕셔너리 삭제 ()괄호 포함하였습니다.
            print("학생의 성적이 삭제되었습니다")
        else :  # 입력 받은 iname이 score 에 없는 경우
            print("삭제할 학생의 이름이 없습니다.")
            

    #성적변경 (딕셔너리는 최근 받은 데이터 값을 저장)
    elif sel ==4:
        print("\n\n>>>성적변경<<<")
        iname = input("변경할 학생이름 입력=>")
        if iname in score: # 입력 받은 iname이 score 에 있는 경우
            ieng = int(input("변경할 영어 성적=>"))
            score[iname]['영어'] = ieng # 입력받은 ieng를 score 에 있는 [iname]["영어"]에 저장
            imat = int(input("변경할 수학성적=>"))
            score[iname]['수학'] = imat # 입력받은 imat를 score 에 있는 [iname]["수학"]에 저장
            print("학생 성적이 변경 되었습니다")
        else: # 입력 받은 iname이 score 에 없는 경우
            print("성적 변경할 학생이 없습니다")

    #성적차트
    #입력된 학생 모두의 성적 차트을 나타나도록 만들었습니다.
    #성적이 5점으로 남거나 소수점으로 떨어질 경우 반올림되게 하는 것은 적용시키지 못했습니다.
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

    #성적평균
    #입력된 학생 모두의 성적 평균을 나타나도록 만들었습니다.
    elif sel == 6:
        print("\n\n>>>성적평균<<<")
        name = input('이름=>')
        while name in score:
            value = score[name]
            sum = value['영어'] + value['수학'] # 키에 해당하는 영어, 수학 성적의 합계를 구함
            print("평균 :", sum/2)       #두 과목의 평균
            print("---------------------다음 학생") # 학생구분
            name = input('이름=>')
