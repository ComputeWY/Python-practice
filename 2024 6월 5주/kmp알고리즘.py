def computeLPS(pat):
    lps = [0] * len(pat)
    length = 0  # 이전의 최장 접두사도 동시에 접미사의 길이
    i = 1

    while i < len(pat):
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

# 예제 사용법:
pattern = "aabaabaaa"
lps_array = computeLPS(pattern)
print("패턴 '{}'의 LPS 배열: {}".format(pattern, lps_array))
