def solution(friends, gifts):
    g_map, g_count, r_count, ans = {}, {}, {}, {}

    for f in friends:
        g_map[f] = {f2: 0 for f2 in friends if f != f2}
        ans[f], g_count[f], r_count[f] = 0, 0, 0

    for gift in gifts:
        g, r = gift.split()
        g_map[g][r] += 1
        g_count[g] += 1
        r_count[r] += 1

    for i in range(len(friends) - 1):
        for j in range(i + 1, len(friends)):
            A, B = friends[i], friends[j]
            A_c, B_c = g_map[A][B], g_map[B][A]

            if A_c > B_c:
                ans[A] += 1
            elif B_c > A_c:
                ans[B] += 1
            else:
                A_v, B_v = g_count[A] - r_count[A], g_count[B] - r_count[B]
                if A_v > B_v:
                    ans[A] += 1
                elif B_v > A_v:
                    ans[B] += 1

    return max(ans.values())