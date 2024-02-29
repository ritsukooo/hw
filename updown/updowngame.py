import random

def random_number():
    return random.randint(1, 100)

answer = random_number()
count = 0

def play():
    global count, answer

    
    while True:
        guess = input("1부터 100사이 숫자를 입력하세요:")
        guess = int(guess)
        count += 1
        
        if guess == answer:
            print(f"정답입니다! 정답 숫자는 {answer}이었습니다!")
            break
        
        elif guess > answer:
            print("down")
        else:
            print("up")
            
            



play()
print(f"시도횟수는 {count}번 입니다!")
    

while True:
    play_again = input("게임을 계속 하시겠습니까? (yes/no):")
    if play_again.lower() == "yes":
        play()
    elif play_again.lower == "no":
        print("게임을 종료합니다")
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
    break