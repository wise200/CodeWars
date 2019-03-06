from datetime import date

class Post:
    def __init__(self, string):
        args = string.split('|')
        self.title = args[0]
        self.name = args[1]
        self.likes = int(args[2])
        self.dislikes = int(args[3])
        self.followers = int(args[4])
        self.following = args[5] == 'True'
        self.blocked = args[6] == 'True'
        self.date = args[7]
        jd = args[8]
        self.join_date = date(int(jd[:4]), int(jd[5:7]), int(jd[8:]))
        self.post_count = args[9]

    def string(self, score):
        return f'({score}) {self.title}. by: {self.name} [{self.date}]'


def old(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    if year < 2019 or month == 1:
        return True
    if month == 2:
        return day < 16
    return False

def young(date):
    year = int(date[:4])
    month = int(date[5:7])
    day = int(date[8:])
    if year < 2019 or month == 1:
        return False
    if month == 2:
        return day >= 23
    return True

def weekDiff(d1, d2):
    return (d1-d2).days // 7

def score(post):
    score = 10000
    if post.followers >= 1e6:
        score += 10000
    if post.followers < 100:
        score -= 5000
    if post.likes == post.dislikes:
        score /= 100
    else:
        score /= post.likes - post.dislikes
    if post.following:
        score += 5000
    if young(post.date):
        score += 500
    if old(post.date):
        score -= 100
    today = date(2019,3,2)
    score += weekDiff(today,post.join_date)
    score += post.post_count

posts = []

word = input()
while word != '':
    p = Post(word)
    if not p.blocked:
        posts.append(p)
    word = input()

posts = sorted(posts, key=score)
for p in posts:
    print(p.string())