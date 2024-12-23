def main(input_data, output_file):
    # Чтение входных данных
    lines = input_data.strip().split("\n")
    n = int(lines[0])
    A = list(map(int, lines[1].split()))
    m = int(lines[2])
    B = list(map(int, lines[3].split()))
    l = int(lines[4])
    C = list(map(int, lines[5].split()))

    # Динамическое программирование для нахождения LCS
    dp = [[[0] * (l + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if A[i - 1] == B[j - 1] == C[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    # Результат в правом верхнем углу
    output_file.write(f"{dp[n][m][l]}\n")


if __name__ == '__main__':
    import sys

    input_path = sys.argv[1] if len(sys.argv) > 1 else "../txtf/input.txt"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "../txtf/output.txt"

    try:
        with open(input_path, "r") as input_file:
            input_data = input_file.read()

        with open(output_path, "w") as output_file:
            main(input_data, output_file)

        print(f"Результат успешно записан в файл '{output_path}'")
    except Exception as e:
        print(f"Ошибка при обработке: {e}")