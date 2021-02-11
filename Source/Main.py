import SendKakao, CheckCommit
import datetime, time

def main():
    SendKakao.openKakao()
    SendKakao.enterRoom()
    commitData = CheckCommit.getCommit()
    for commit in commitData:
        SendKakao.sendText(commit)

if __name__ == '__main__':
    main()

