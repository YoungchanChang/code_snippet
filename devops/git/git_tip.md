# 깃 반영했는데 서버 장애 났을 경우.

1. git log 본 다음에

2. 장애 지점 확인

3. git reset --hard a72339e7c13fe914ad13cafacc3b9f2c8957f7b9

# 협업할 경우
## 로컬에서 작업
git checkout master # 마스터로 진입
git pull origin master # 마스터에서 당겨온다.
git merge yc_git >> 여기서 merge한다. # 마스터에서 yc_git당겨온다.
git push origin master # 

## 깃브랜치 작업 순서
1. git branch -b "내이름"
2. 브랜치에서 작업한다.
3. master로 돌아와서 (git checkout master) git pull한다. (서버로부터 최신 버전 받은 상태)
4. git merge yc_git으로 마스터에서 브랜치를 머지한다.
5. git push origin master로 master에서 올린다.
6. 푸쉬했다고 다른 사람들에게 알려준다.
