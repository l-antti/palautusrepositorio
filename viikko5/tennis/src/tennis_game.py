class TennisGame:
    SCORE_MAP = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def _get_score_text(self, score):
        return self.SCORE_MAP.get(score, str(score))

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_tied_score()

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._get_advanced_score()

        return self._get_normal_score()

    def _get_tied_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        return "Deuce"

    def _get_advanced_score(self):
        score_diff = self.m_score1 - self.m_score2
        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        elif score_diff == -1:
            return f"Advantage {self.player2_name}"
        elif score_diff >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def _get_normal_score(self):
        score1 = self._get_score_text(self.m_score1)
        score2 = self._get_score_text(self.m_score2)
        return f"{score1}-{score2}"
