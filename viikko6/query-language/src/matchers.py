
class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False


class All:
    def __init__(self):
        pass

    def test(self, player):
        return True


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class QueryBuilder:
    def __init__(self, query_olio = All):
        self.query_olio = query_olio

    def build(self):
        return self.query_olio

    def playsIn(self, value):
        self.query_olio = And(PlaysIn(value))
        return QueryBuilder(self.query_olio)

    def hasAtLeast(self, value, attr):
        self.query_olio = And(HasAtLeast(value, attr))
        return QueryBuilder(self.query_olio)

    def hasFewerThan(self, value, attr):
        self.query_olio = And(HasFewerThan(value, attr))
        return QueryBuilder(self.query_olio)