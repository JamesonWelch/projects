from fractions import Fraction

print('Welcome to the odds calculator:')
print()
odds = int(input('Enter the odds: '))
wager = int(input('Enter wager (Bet Amount): '))

print('Bet ', wager)
print()

if odds > 0:
    profit = odds/100
    winnings = wager * profit
    payout = winnings + wager
    frac_odds = Fraction(profit)
    dec_odds = payout/wager
    imp_prob = 100/(odds + 100) * 100
elif odds < 0:
    odd = odds * -1
    profit = odd/100
    winnings = wager * profit
    payout = winnings + wager
    frac_odds = Fraction(profit)
    dec_odds = payout/wager
    imp_prob = odd/(odd + 100) * 100

print('___________________\n')
print('To win: ', winnings, '\n')
print('Payout: ', payout, '\n')
print('American Odds: ', odds, '\n')
print('Fractional Odds: ', frac_odds, '\n')
print('Decimal Odds: ', dec_odds, '\n')
print('Implied Probability: ', imp_prob)
