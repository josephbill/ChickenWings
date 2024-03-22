class Participant:
    def __init__(self, name, chickenwings, hamburgers, hotdogs):
        self.name = name
        self.chickenwings = chickenwings
        self.hamburgers = hamburgers
        self.hotdogs = hotdogs
    
    def calculate_score(self):
        return self.chickenwings * 5 + self.hamburgers * 3 + self.hotdogs * 2
    

    

def create_scoreboard(participants):
    scoreboard = []
    for participant_data in participants:
        participant = Participant(participant_data['name'], participant_data['chickenwings'], participant_data['hamburgers'], participant_data['hotdogs'])
        score = participant.calculate_score()
        scoreboard.append({'name': participant.name, 'score': score})
    
    # Sort the scoreboard by score first, then by name alphabetically
    scoreboard.sort(key=lambda x: (-x['score'], x['name']))
    return scoreboard

participants_data = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]

scoreboard = create_scoreboard(participants_data)
print(scoreboard)
