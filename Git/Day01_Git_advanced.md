### Branch

master(상용, 원본) - 고객에게 보여지는 곳 → 따로 작업하는 곳 hotfix

- 브랜치 조회: `git branch`
- 브랜치 생성 : `git branch hotfix`
- 작업 공간 변경 : `git switch hotfix` → 🚫 commit할 게 더 이상 없을 때 사용
- HEAD 공간에서의 브랜치 확인 : `git log --oneline`
- 존재하는 모든 공간에서의 브랜치 확인 : `git log --oneline --all`
- 브랜치 삭제 : `git branch -d hotfix`

#### 왜 커밋하고 swtich할까?

❓ 브랜치를 커밋을 기준으로 나뉘어져 있고 master, hotfix라는 포인터가 있는 것이다. 즉, working directory나 staging area는 공유하고 있기 때문에, 커밋하지 않고 switch하면 master에서 hotfix일 때 작성한 파일이 보인다.

### Merge

`git merge hotfix`, `git merge master`

1. __Fast-Forward__
   - hotfix 브랜치를 master에 합침으로써 master가 hotfix가 가리키는 곳으로 쭉 빨리 감기가 된다.
2. __3-way merge__
   - 브랜치가 합칠 때 3개의 커밋을 합친다. (hotfix, master, 그 둘의 공통 조상 셋을 같이 비교해서 merge)
3. __Merge Conflict__
   - merge할 때 같은 파일에서 다른 공간에서 작성한 내용이 충돌할 때 사용자가 남길 내용을 선택할 수 있는 상태가 된다.