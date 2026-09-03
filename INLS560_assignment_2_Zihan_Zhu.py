"""
INLS 560 - Assignment 2: Compound Interest
"""


def get_savings_parameters():
    # Collect one complete set of savings parameters from the user.
    principal = float(input("Please enter the initial amount of your investment: "))
    rate = float(input("Please enter the interest rate (e.g., '.03' for 3% interest): "))
    years = int(input("Please enter the number of years for the investment: "))
    periods = int(input("Please enter the number of compounding periods per year: "))
    return principal, rate, years, periods


def calculate_final_balance(principal, rate, years, periods):
    # Compound interest formula: P' = P(1 + r/n)^(nt)
    return principal * (1 + rate / periods) ** (periods * years)


def format_money(amount):
    # Dollar sign, comma separators, and two decimal places.
    return f"${amount:,.2f}"


def display_results(principal, final_balance):
    # The labels are padded to a common width so the amounts line up.
    print(f"{'Original Investment:':<21}{format_money(principal)}")
    print(f"{'Interest Earned:':<21}{format_money(final_balance - principal)}")
    print(f"{'Final Balance:':<21}{format_money(final_balance)}")


def main():
    print("Welcome to the Compound Interest Calculator.")

    principal, rate, years, periods = get_savings_parameters()
    first_balance = calculate_final_balance(principal, rate, years, periods)
    display_results(principal, first_balance)

    print()
    answer = input("Would you like to compare this to another savings option? (Y/N) ")

    # Anything other than a "yes" ends the program after the first result.
    if answer.strip().upper() not in ("Y", "YES"):
        return

    principal, rate, years, periods = get_savings_parameters()
    second_balance = calculate_final_balance(principal, rate, years, periods)
    display_results(principal, second_balance)

    print()
    if second_balance > first_balance:
        print("The second option will result in the largest final account balance.")
    elif first_balance > second_balance:
        print("The first option will result in the largest final account balance.")
    else:
        print("Both options will result in the same final account balance.")


if __name__ == "__main__":
    main()
