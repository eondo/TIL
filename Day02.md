#### 주의사항
- git init 안에 git init 넣을 수 없음. git init은 가장 상위 폴더에서만 한다. 즉, master가 이미 있으면 git init 하지 않는다.
- 관리할 서버, 폴더에만 git init을 한다.
- github 안에서 따로 파일 수정하거나, 그러면 안됨. 순서가 무조건 local에서 만들고 remote에 옮긴다. remote에 있는 것을 먼저 수정하면 안됨. 무조건 local에서 수정하고 remote로 옮기기. add-commit-push 순서 지키기.

## 특별한 파일
< README.md >
: 프로젝트의 설명서

- local을 remote에 반영하는 git 코드

```
$ git status
On branch master
Untracked files:
(use "git add <file>..." to include in what will be committed)
      README.md
       
nothing added to commit but untracked files present (use "git add" to track)

S@M805 MINGW64 ~/Desktop/TIL (master)
$ git add .

S@M805 MINGW64 ~/Desktop/TIL (master)
$ git commit -m "Upload README.md"
[master 6edd71c] Upload README.md
1 file changed, 3 insertions(+)
create mode 100644 README.md    

S@M805 MINGW64 ~/Desktop/TIL (master)
$ git push origin master
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 367 bytes | 367.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/eondo/TIL.git
  a3bd025..6edd71c master -> master

S@M805 MINGW64 ~/Desktop/TIL (master)
$
```


< .gitignore >
: 이 파일 버전에 안 포함시킬 거예요! 여기에 있는 파일은 버전 관리를 안하겠다. 깃허브에는 올라가지 않음.
남에게 보여주면 안되는 보안적인 파일, 굳이 올리지 않아도 되는 파일

- 주의 : 이미 버전 관리를 한 a.txt는 무를 수 없음. .gitignore에 넣어 무를 수 없음.
따라서, <.gitignore>는 프로젝트의 맨 처음에 만든다! + <README.md>도!

- 참고 : gitignore에 넣을 파일들은 https://www.toptal.com/developers/gitignore/ 에서 쓸 기술들을 검색해서 해당 내용을 복사해 넣으면 된다.

## clone과 pull
#### clone : 그대로 다운로드를 하는 것. git clone을 하면 Local에 TIL폴더가 생기고, 그 안에 v1,v2,v3...이 만들어진다. 
  - git clone을 하면 한 번에 4가지 기능이 실행된다.
    - 폴더 생성
    - git init 됨
    - git remote add
    - 버전, 파일 생성

  - 폴더 만들고 싶은 곳(ex.바탕화면)에서 GIT BASH HERE로 터미널 열기

  - git clone (remote의 Code 클릭했을 때 나오는 URL) 입력하면 폴더 그대로 local에 생성됨

#### pull : 업데이트, remote에 v4를 새로 만들었다면 이 v4를 Local의 TIL폴더에 업데이트한다.
  - git pull origin master
  - 비이상적인 경로 : 내 컴퓨터에서 자체적으로 똑같은 v3 만들고 이거 push하려고 하면 일단 pull부터 하라고 에러 뜸. 즉, 두 개의 버전이 충돌하는 상황 = conflict
    - 이때는 v3, v3' 중 어떤 것을 할 건지 사람의 선택(개입)이 필요함. 최종적으로 v4가 생성됨.
    
+ github에서 다른 contributor와 함께 push, pull하는 법
setting-collaborators에 add people 누르면 user name 적어서 초대. 
조원은 깃허브로 가입한 메일로 들어가서 초대 수락. 공동 소유권을 가지게 됨. 본인 local에 clone하고 바로 수정하면 됨!
