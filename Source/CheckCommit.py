from github import Github
from datetime import date, timedelta

def getCommit():
    g = Github("ssw03270", "psj0207@")
    g = Github("token")

    userList = ["bluehyena", "ch4n3-yoon", "ssw03270", "mmindoong"]
    commitData = []
    for user in userList:
        allCommitList = g.search_commits("author:" + user + " sort:author-date-desc")
        commitMessage = ""
        commitCount = 0
        i = 20
        for commit in allCommitList:
            i -= 1
            if i < 0:
                break
            if str(getCurrentDate()) in str(commit.commit.author.date):
                commitCount += 1
                if commitCount == 1:
                    commitMessage = str(commit.commit.message) + " | " + str(commit.commit.author.date)
        if(commitCount > 0):
            commitData.append(user + " : " + commitMessage + " | 그 외 " + str(commitCount - 1) + "개의 커밋을 하셨습니다.")
        else:
            commitData.append(user + " : 0개의 커밋을 하셨습니다. 벌금 5,000원 입니다.")
    return commitData

def getCurrentDate():
    yesterday = date.today() - timedelta(1)
    currentDate = yesterday.strftime('%Y-%m-%d')
    return currentDate