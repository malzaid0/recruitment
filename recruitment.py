def main():
    # write your code here
    cv = {}

    print("Welcome to the special recruitment program, please answer the following questions:")
    cv["name"] = input("What's your name? ")
    cv["age"] = int(input("How old are you? "))
    cv["experience"] = int(input("How many years of experience do you have? "))
    cv["skills"] = []

    skills = ["Python", "C++", "Javascript", "Meeting", "Leeting", "Eating"]

    print("\nSkills:")
    for i in range(len(skills)):
        print(str(i + 1) + ". " + skills[i])
    # for skill in skills:
    #     print(skill)
    print()

    cv["skills"].append(skills[int(input("Choose a skill from above by entering its number: ")) - 1])
    cv["skills"].append(skills[int(input("Choose another skill from above by entering its number: ")) - 1])

    if 25 <= cv["age"] <= 40 and cv["experience"] > 5 and skills[5] in cv["skills"]:
        print("You have been accepted , %s" % cv["name"])
    else:
        print("rejected")


if __name__ == '__main__':
    main()
