PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def check_voting_eligibility(age, country, voting_age):
    status = "can" if age >= voting_age else "cannot"
    print(f"You {status} vote in {country} where the voting age is {voting_age}.")

def main():
    age = int(input("How old are you? "))

    check_voting_eligibility(age, "Peturksbouipo", PETURKSBOUIPO_AGE)
    check_voting_eligibility(age, "Stanlau", STANLAU_AGE)
    check_voting_eligibility(age, "Mayengua", MAYENGUA_AGE)

if __name__ == '__main__':
    main()
