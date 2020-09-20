"""Given a street of N houses (a row of houses), each house having K amount of money kept inside;
now there is a thief who is going to steal this money but he has a constraint/rule that he cannot
steal/rob two adjacent houses. Find the maximum money he can rob."""
def get_odds_by_N(N, K):
    return (N + 1) // 2 * K
