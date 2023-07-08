rates = [10, 20, 30, 40]
max_member = 0
max_profit = 0


def solution(users, emoticons):
    global max_member, max_profit

    # n = len(emoticons)
    def calc(sale_list, n):
        count_user = 0
        count_profit = 0

        # user 한명씩 검사하기
        for user in users:
            rate, limit_money = user[0], user[1]
            total_money = 0  # 이모티콘 구매 비용
            for i in range(n):
                if rate <= sale_list[i]:  # 할인율이 더 큰 경우
                    total_money += emoticons[i] * (1 - 0.01 * sale_list[i])  # 구매
            if total_money >= limit_money:  # 이모티콘 플러스 가입하는 경우
                count_user += 1
            else:
                count_profit += total_money
        return count_user, count_profit

    def dfs(depth, n, sale_list):
        global max_member, max_profit, rates

        # sale_list 가 n 개 일때
        if depth == n:
            mem, pro = calc(sale_list, n)
            if mem > max_member:
                max_member, max_profit = mem, pro
            elif mem == max_member:
                if max_profit < pro:
                    max_profit = pro
            return

        for i in range(4):  # 할인 10, 20, 30, 40
            dfs(depth + 1, n, sale_list + [rates[i]])

    dfs(0, len(emoticons), [])

    answer = [max_member, max_profit]

    return answer