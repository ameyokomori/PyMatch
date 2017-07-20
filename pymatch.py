# Get the access to the code in the partners.py file.
import partners


# Define a function which could be used to print both physical characteristics question and personality question.
def show_question(question):
    """
    Print physical characteristics question or personality question with its answers, and return user's choice.
    
    This function should be called with a list parameter which contains one question and all its answers. 
    In this function, all the elements of the list will be iterated and printed in order (with a number at the front).
 
    Parameter question: The question and answers to be shown. 
    
    Return the chosen answer, which is an integer number."""
    # Print question in list question.
    print(question[0])
    # Print all answers in list question.
    for i in range(1, len(question)):
        print('  {0}) {1}'.format(i, question[i]))

    while True:
        answer = input("Please enter your answer: ")
        print("\n")
        # Check if the answer valid.
        if answer.isnumeric():
            if int(answer) in range(1, len(question)):
                return int(answer)
        # If invalid, ask user to input again, until function receive a valid input.
        print("You should input a integer between 1 and {0} ".format(len(question) - 1))


# Define a function which is used to find the best matched partner.
def match(gender, sexual_pref, height, height_pref, personality_score):
    """
    Find the best match partners in database.
    
    This function should be called with 5 parameters which are user's gender, sexual_pref, height, height_pref 
    and personality_score. In this function, every potential partner in the database will be retrieved and compared with 
    user's personal information, and finally return the best matched partner or none.
 
    Parameter gender: User's gender.
    Parameter sexual_pref: User's sexual preference.
    Parameter height: User's height.
    Parameter height_pref: User's height preference.
    Parameter personality_score: User's personality score.
    
    Return: The best matched person's full name.
    """
    # Creates a variable that can access the potential partners.
    potential_partners = partners.Partners()
    # List variable call difference which is used to save the difference of personality score.
    # The original value 99 is an nonexistent value (because the max value of difference is 32)
    difference = [99]
    # List variable match_name is used to save the full name of potential partners.
    match_name = ['None']
    # List variable partner_height is used to save the height of potential partners.
    partner_height = ['None']
    # List variable partner_height_pref is used to save the height pref of potential partners.
    partner_height_pref = ['None']

    # The following loop iterates over all of the potential partners in the database.
    while potential_partners.available():
        # Compare both gender and sexual preference.
        if gender == potential_partners.get_sexual_pref() and sexual_pref == potential_partners.get_gender():
            # If the new difference is less than previous ones, all these lists will be override with the new values.
            if abs(personality_score - int(potential_partners.get_personality_score())) < difference[0]:
                difference = [abs(personality_score - int(potential_partners.get_personality_score()))]
                match_name = [potential_partners.get_name()]
                partner_height = [potential_partners.get_height()]
                partner_height_pref = [potential_partners.get_height_pref()]

            # If the new difference is equal to previous ones, the new values will be added at the end of the lists.
            elif abs(personality_score - int(potential_partners.get_personality_score())) == difference[0]:
                difference.append(abs(personality_score - int(potential_partners.get_personality_score())))
                match_name.append(potential_partners.get_name())
                partner_height.append(potential_partners.get_height())
                partner_height_pref.append(potential_partners.get_height_pref())

    # If there is only 1 potential partner in the list, this person must be the best matched partner.
    if len(difference) == 1:
        return match_name[0]

    # If there are more than 1 potential partner in the list, iterates over all of them and find the one whose height
    # and height preference is matched.
    elif len(difference) > 1:
        for i in range(len(difference)):
            if height == partner_height_pref[i] and height_pref == partner_height[i]:
                return match_name[i]

    return match_name[0]


# Main function.
def main():
    print("Welcome to PyMatch")
    name = input("\nPlease enter your name: ")
    print("\nHi", name + ".")

    # Create lists with one question and several answers.
    question_gender = ["What is your gender?", "male", "female", "other"]
    question_sexual_pref = ["What is your sexual preference?", "male", "female", "other"]
    question_height = ["What is your height?", "tall", "medium", "short"]
    question_height_pref = ["What height do you prefer your partner to be?", "tall", "medium", "short"]

    # Call show_question function with each question list, then turn the returned value(number) into specific answer.
    user_gender = question_gender[show_question(question_gender)]
    user_sexual_pref = question_sexual_pref[show_question(question_sexual_pref)]
    user_height = question_height[show_question(question_height)]
    user_height_pref = question_height_pref[show_question(question_height_pref)]

    print("We will now ask you some questions to try to determine your personality type.")

    # List personality_answers is the common part of personality question.
    personality_answers = ['Yes', 'Most of the time', 'Neutral', 'Some times', 'No']

    # Create lists which add one question and several answers(personality_answers).
    user_personality1 = ["Do you find it easy to introduce yourself to other people?"] + personality_answers
    user_personality2 = ["Do you usually initiate conversations?"] + personality_answers
    user_personality3 = ["Do you often do something out of sheer curiosity?"] + personality_answers
    user_personality4 = ["Do you prefer being out with a large group of friends "
                         "rather than spending time on your own?"] + personality_answers

    # Call show_question function with each question list, then calculate personality score with the returned value.
    user_personality_score = (show_question(user_personality1) + show_question(
        user_personality2) + show_question(user_personality3) + show_question(user_personality4)) * 2

    # Call match function and saved the returned name.
    best_match = match(user_gender, user_sexual_pref, user_height, user_height_pref, user_personality_score)

    # Print the result.
    print("Thank you for answering all the questions. "
          "We have found your best match from our database and hope that you enjoy getting to know each other. "
          "Your best match is: \n" + best_match)


# Call main function.
if __name__ == "__main__":
    main()
