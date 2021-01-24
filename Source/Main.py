import SendKakao, CheckCommit
import datetime, time

def main():
	while True:
		SendKakao.openKakao()
		SendKakao.enterRoom()
		if datetime.datetime.today().hour == 0 and datetime.datetime.today().minute == 0:
			commitData = CheckCommit.getCommit()
			for commit in commitData:
				SendKakao.sendText(commit)
		time.sleep(60)

if __name__ == '__main__':
	main()


