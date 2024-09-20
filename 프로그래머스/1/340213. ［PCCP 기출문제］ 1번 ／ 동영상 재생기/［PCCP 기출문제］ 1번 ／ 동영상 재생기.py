def time_to_sec(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds

def sec_to_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    video_len = time_to_sec(video_len)
    curr_pos = time_to_sec(pos)
    op_start = time_to_sec(op_start)
    op_end = time_to_sec(op_end)
    
    for cmd in commands:
        if op_start <= curr_pos <= op_end:  # 명령 실행 전 오프닝 체크
            curr_pos = op_end
        
        if cmd == "prev":
            curr_pos = max(0, curr_pos - 10)  # 음수를 0으로 보정하는 테크닉 ㅇㅇ,,,
            
        elif cmd == "next":
            curr_pos = min(video_len, curr_pos + 10)  # 비디오 최대 길이를 넘어갈시, 최대길이로 보정...
           
    # 명령 실행 후 한번 더 체크
    if op_start <= curr_pos <= op_end:
        curr_pos = op_end
        
    return sec_to_time(curr_pos)