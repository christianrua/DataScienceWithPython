"""
Election Results

You’re part of an impartial research group that conducts phone surveys prior to local elections. During this election season, the 
group conducted a survey to determine how many people would vote for Cynthia Ceballos vs. Justin Kerrigan in the mayoral election.

Now that the election has occurred, your group wants to compare the survey responses to the actual results.

Was your survey a good indicator? Let’s find out! 
"""

import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos=sum([1 for n in survey_responses if n=='Ceballos'])

survey_lenght=float(len(survey_responses))
percentage_ceballos=total_ceballos/survey_lenght

print(percentage_ceballos)

possible_surveys=np.random.binomial(survey_lenght,0.54,10000)/float(survey_lenght)

ceballos_loss_surveys=np.mean(possible_surveys<0.5)
print(ceballos_loss_surveys)

plt.hist(possible_surveys,range=(0,1),bins=20)
plt.show()

large_survey=np.random.binomial(7000,0.54,10000)/float(7000)

ceballos_loss_new=np.mean(large_survey<0.5)
print(ceballos_loss_new)
