
def calculate_score(frames):
    score = 0
    for frame in frames:
        if is_spare(frame):
            score += 10
        else:
            roll1 = 0 if frame[0] == '-' else int(frame[0])
            roll2 = 0 if frame[1] == '-' else int(frame[1])
            score += roll1 + roll2
    return score

def is_spare(frame):
    return '/' in frame