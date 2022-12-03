class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        
        if self.m_score1 == self.m_score2:
            return self.get_even_score(self.m_score1)
            
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_advantage_score()

        else:
            return self.get_game_score()

    def get_game_score(self):
        score = self.get_string_value(self.m_score1)
        score += '-'
        score += self.get_string_value(self.m_score2)
        return score

    def get_even_score(self, even_score):
        if (even_score < 4):
            return(self.get_string_value(even_score) + '-All')
        else:
            return "Deuce"

    def get_advantage_score(self):
        point_difference = self.m_score1 - self. m_score2
        score = ''

        if (point_difference == 1 or point_difference == -1):
            score += 'Advantage '
        else:
            score += 'Win for '

        if (point_difference > 0):
            score += 'player1'
        else:
            score += 'player2'

        return score

    def get_string_value(self, score):
        if (score == 0): return 'Love'
        if (score == 1): return 'Fifteen'
        if (score == 2): return 'Thirty'
        if (score == 3): return 'Forty'
        return None