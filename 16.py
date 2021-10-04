def compound_interest(p,r,t):
  amount=p*pow((1+r/100),t)
  ci=amount-p
  return ci

compound_interest(10000,10.25,5)
