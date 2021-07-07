

# calculate_score([['X'],['X'],['4','3']])

def calculate_score(frames):
    score = 0
    previous_frame = None
    previous_score = 0
    before_previous_score = 0

    for frame in reversed(frames):

        if is_strike(frame):
            current_score = 10 + get_bonus_strike_score(previous_score, before_previous_score)
            score += current_score
            before_previous_score = previous_score
            previous_score = current_score
        elif is_spare(frame):
            score += 10 + get_bonus_spare_score(previous_frame)
        else:
            score += get_roll(frame[0]) + get_roll(frame[1])
            previous_score = get_roll(frame[0])
            before_previous_score = get_roll(frame[1])
        
        previous_frame = frame
    return score

def is_spare(frame):
    return '/' in frame

def is_strike(frame):
    return 'X' in frame

def get_roll(roll):
    return 0 if roll == '-' else int(roll)

def get_bonus_spare_score(previous_frame):
    return int(previous_frame[0]) if previous_frame else 0

def get_bonus_strike_score(previous_score, before_previous_score):
    return previous_score + before_previous_score