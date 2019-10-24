"""
FetchMaker

Congratulations! You’ve just started working at the hottest new tech startup, FetchMaker. FetchMaker’s mission is to match up 
prospective dog owners with their perfect pet. Data on thousands of adoptable dogs are in FetchMaker’s system, and it’s your job 
to analyze some of that data.
"""

import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency

rottweiler_tl=fetchmaker.get_tail_length("rottweiler")

print(np.mean(rottweiler_tl),np.std(rottweiler_tl))

whippet_rescue=fetchmaker.get_is_rescue("whippet")
num_whippet_rescues=np.count_nonzero(whippet_rescue)
num_whippets=np.size(whippet_rescue)
pval=binom_test(num_whippet_rescues,num_whippets,0.08)
print('Pvalue from rescues '+str(pval)+'\n')

whippets=fetchmaker.get_weight("whippet")
terriers=fetchmaker.get_weight("terrier")
pitbulls=fetchmaker.get_weight("pitbull")

stats,pval1=f_oneway(whippets,terriers,pitbulls)
print('Pvalue from Anova '+str(pval1)+'\n')

v = np.concatenate([whippets, terriers, pitbulls])
labels = ['whippets'] * len(whippets) + ['terriers'] * len(terriers) + ['pitbulls'] * len(pitbulls)
tukey_results=pairwise_tukeyhsd(v,labels,0.05)
print(tukey_results)

poodle_colors=fetchmaker.get_color("poodle")
shihtzu_colors=fetchmaker.get_color("shihtzu")

color_table=[[np.count_nonzero(poodle_colors == "black"),np.count_nonzero(shihtzu_colors == "black")],
             [np.count_nonzero(poodle_colors == "brown"),np.count_nonzero(shihtzu_colors == "brown")],
             [np.count_nonzero(poodle_colors == "gold"),np.count_nonzero(shihtzu_colors == "gold")],
             [np.count_nonzero(poodle_colors == "grey"),np.count_nonzero(shihtzu_colors == "grey")],
             [np.count_nonzero(poodle_colors == "white"),np.count_nonzero(shihtzu_colors == "white")]]

chi2, pval2, dof, expected = chi2_contingency(color_table)
print pval
