import hashlib

def hash_password(password):
    # hashlib을 사용하여 비밀번호를 해시화
    #사용자가 제공한 비밀번호를 SHA-256 해시 함수를 사용하여 해시화하고, 그 결과를 16진수 문자열로 반환하는 것
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"회원이름: {self.name}, 아이디: {self.username}")


class Post:  
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


member_1 = Member("김형호", "kim", "1234")
member_2 = Member("박주영", "park", "5678")
member_3 = Member("이주희", "lee", "9101")


members = []
members.append(member_1)
members.append(member_2)
members.append(member_3)

for member in members:
    print(f"회원 이름: {member.name}")




posts = []

post11 = Post("가나11", "content11", "kim")  
post12 = Post("다라12", "content12", "kim")  
post13 = Post("마바13", "content13", "kim")  
post21 = Post("사아21", "content21", "park")  
post22 = Post("자차22", "content22", "park") 
post23 = Post("카파23", "content23", "park") 
post31 = Post("타하31", "content31", "lee") 
post32 = Post("기니32", "content32", "lee")  
post33 = Post("디리33", "content33", "lee")  

posts.append(post11)
posts.append(post12)
posts.append(post13)
posts.append(post21)
posts.append(post22)
posts.append(post23)
posts.append(post31)
posts.append(post32)
posts.append(post33)

for post in posts:
    if post.author == "park":
        print(post.title)

for post in posts:
    if "3" in post.content:
        print(post.title)


while True:
    sign_in = input("회원가입을 하시겠습니까? (yes/no): ")
    if sign_in.lower() == "yes":
        name = input("이름을 입력하세요: ")
        username = input("아이디를 입력하세요: ")
        password = input("비밀번호를 입력하세요: ")
        member = Member(name, username, password)
        members.append(member)
        print("회원 등록이 완료되었습니다.")
    elif sign_in.lower() == "no":
        break
    else:
        print("잘못된 입력입니다. 'yes' 또는 'no'로 입력해주세요.")

print("등록된 회원 정보:")
for member in members:
    print(f"이름: {member.name}, 아이디: {member.username}, 비밀번호: {member.password}")


while True:
    posting=input("포스팅하시겠습니까?(yes/no):")
    if posting.lower() == "yes":
       title = input("게시물의 제목을 입력해 주세요:")
       content =input("게시글의 내용을 입력해 주세요:")
       author=input("아이디를 입력해 주세요:")
       new_post = Post(title, content, author) 
       posts.append(new_post)
    elif sign_in.lower() == "no":
        break
    else:
        print("잘못된 입력입니다. 'yes' 또는 'no'로 입력해주세요.")
        
        
print("게시물 내용 확인")
for post in posts:
    print(f"제목: {post.title} 내용: {post.content} 저자: {post.author}")




# posts = []


# for member in members:
#     post.title=f"{member.name}의 게시글"
#     post.content=f"{member.name}이 작성한 게시글 내용"
#     post.author=member.username


# Post = post(post.title, post.content,post.author)
# posts.append(Post)

# #3번 이상 반복?