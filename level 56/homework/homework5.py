N = int(input("3535346 N: "))
arr = [int(input(f"235 #{i+1}: ")) for i in range(N)]
arr[0], arr[N-1] = arr[N-1], arr[0]

