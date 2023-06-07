n = int(input("任意の整数を入力してください: "))
roots = []
pwrs = []

for guess in range(2, n+1):
    if n % guess == 0:
        print("root",guess)
        for guess_pwr in range(2,6):
            if guess**guess_pwr == n:
                roots.append(guess)
                pwrs.append(guess_pwr)
                break

if len(roots) == 0:
    print("該当する整数の組は存在しません")
else:
    for i in range(len(roots)):
        print(roots[i-1],"**",pwrs[i-1])

