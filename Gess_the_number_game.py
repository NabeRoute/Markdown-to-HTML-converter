import random

def guess_the_number_game():
    print("Guess The Number Game")
    
    # ユーザーに最小値と最大値を入力してもらう
    n = int(input("Enter the minimum number: "))
    m = int(input("Enter the maximum number: "))
    
    # 最小値が最大値以下であることを確認
    while n > m:
        print("Minimum number must be less than or equal to maximum number. Please enter again.")
        n = int(input("Enter the minimum number: "))
        m = int(input("Enter the maximum number: "))
    
    # n から m の範囲内で乱数を生成
    secret_number = random.randint(n, m)
    
    print(f"Guess a number between {n} and {m}. You have 10 attempts.")
    
    # ユーザーが数字を推測するための試行回数を制限
    for attempt in range(1, 11):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempt} attempts.")
            break
    else:  # forループが自然に終了した場合（正解しなかった場合）
        print(f"Sorry, you didn't guess the number. It was {secret_number}.")

guess_the_number_game()