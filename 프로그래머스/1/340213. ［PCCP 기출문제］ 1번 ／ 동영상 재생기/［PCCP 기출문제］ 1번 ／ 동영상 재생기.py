def solution(video_len, pos, op_start, op_end, commands):
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds

    def seconds_to_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    video_len_sec = time_to_seconds(video_len)
    pos_sec = time_to_seconds(pos)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)

    # 시작 시 오프닝 구간인 경우 먼저 건너뛰기
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec

    for command in commands:
        if command == "prev":
            pos_sec = max(0, pos_sec - 10)
        elif command == "next":
            pos_sec = min(video_len_sec, pos_sec + 10)
        
        # 명령 실행 후 오프닝 구간인 경우 건너뛰기
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec

    return seconds_to_time(pos_sec)

