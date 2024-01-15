def solution(players, callings):
        answer = list(players)
        mapped_by_player = {player: i for i, player in enumerate(players)}

        for calling in callings:
            current_rank = mapped_by_player[calling]
            answer[current_rank], answer[current_rank - 1] = answer[current_rank - 1], answer[current_rank]
            mapped_by_player[calling], mapped_by_player[answer[current_rank]] = current_rank - 1, current_rank

        return answer