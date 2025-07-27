import string
from collections import Counter
def find_meeting_details(file_path):
    with open(file_path,'r') as file:
        lines=file.readlines()
    linecounts=len(lines)
    if linecounts==0:
        return "Empty file. No meeting time or place found."
    if linecounts<=12:
        meeting_time=f"{linecounts} AM"
    else:
        meeting_time=f"{linecounts - 12} PM"    
    all_text = " ".join(lines).lower()
    translator = str.maketrans('', '', string.punctuation)
    all_text_clean = all_text.translate(translator)
    words = all_text_clean.split()
    word_counts = Counter(words)
    most_common_word, _ = word_counts.most_common(1)[0]
    meeting_place = f"{most_common_word.capitalize()} Street"
    return f"Meeting time: {meeting_time}\nMeeting place: {meeting_place}"
    
