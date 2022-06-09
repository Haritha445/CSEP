def compound_interest(principal,rate,years):
	return principal*(1+rate)**years
def compound_interest_recursive(principal,rate,years):
	if years == 0:
	     return principle
	else:
	    return
principal_str=input("enter the principal:")
principal=int(principal_str)
rate_float=input("enter the interest rate:")
rate=float(rate_float)
years_str=input("enter the number of years:")
years=int(years_str)
print("principal after",years,"years(s) is", compound_interest\
	(principal,rate,years))
