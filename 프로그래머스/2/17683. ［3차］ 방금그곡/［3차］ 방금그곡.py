def change(code):
    code = code.replace("C#", "c")
    code = code.replace("D#", "d")
    code = code.replace("F#", "f")
    code = code.replace("G#", "g")
    code = code.replace("A#", "a")
    code = code.replace("B#", "b")
    return code

def solution(m, musicinfos):
    result = []
    m = change(m)
    
    for idx, music in enumerate(musicinfos): 
        s, e, t, ms = music.split(",")
        ms = change(ms)
        #총 재생시간 계산
        start = list(map(int, s.split(":")))
        end = list(map(int, e.split(":")))
        runtime = [end[0] - start[0], end[1] - start[1]]
        
        if runtime[1] < 0:
            runtime[1] += 60
            runtime[0] -= 1 
        
        total = runtime[0] * 60 + runtime[1]
        
        #재생 멜로디
        playing = ''
        n = len(ms)
        playing = (ms * (total // len(ms) + 1))[:total]
        
        if m in playing:
            result.append([t, total, idx])
    
    if not result:
        return "(None)"
    
    result.sort(key = lambda x: (-x[1], x[2]))
    return result[0][0]