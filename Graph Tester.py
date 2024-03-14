import pandas as py
import matplotlib.pyplot as plt
import numpy as np

chatgpt_responses = py.read_excel("chatgpt_responses.xlsx", usecols="B:P")

#filtering items
df = chatgpt_responses.filter(items=["accuracy", "frequency"]).groupby(["accuracy", "frequency"]).value_counts().unstack().fillna(0)
    
    #Add empty rows into column
df.loc[1] = [0, 0, 0, 0, 0, 0]
df.loc[3] = [0, 0, 0, 0, 0, 0]
print(df)
df = df.reindex(['Never', 'Rarely (1-5 times)', 'Occasionally (6-10 times)', 'Sometimes (11-15 times)', 'Often (16-20 times)', 'I use ChatGPT on a regular basis'])
print(df)
incrediblelist = []
accuracyorder = (2,4,5,6,7,8,9,10,1,3)
for i in range(len(df.columns)):
  newlist = []
for acc, x in enumerate(df[df.columns[i]]):
  for a in range(int(x)):
    newlist.append(accuracyorder[acc])
    incrediblelist.append(newlist)
print(incrediblelist)
order = ['Never', 'Rarely (1-5 times)', 'Occasionally (6-10 times)', 'Sometimes (11-15 times)', 'Often (16-20 times)', 'I use ChatGPT on a regular basis']
#labels = ['Never', 'Rarely (1-5 times)', 'Occasionally (6-10 times)', 'Sometimes (11-15 times)', 'Often (16-20 times)', 'Regular Use']
fig, ax = plt.subplots()
for position in range(6):
    ax.boxplot(incrediblelist[position], positions=[position])

ax.set_xticks(range(position+1))
#ax.set_xticklabels(labels)
ax.set_xlim(xmin=-0.5)
plt.show()


#df = chatgpt_responses.filter(items=["restrictions", "relationToEducation"]).where(chatgpt_responses["relationToEducation"] != "Student").groupby(["restrictions", "relationToEducation"]).value_counts().unstack().fillna(0)
#df = df.sum(axis = 1)

# print(df)
# myLabels = ["Outright banned", "Used with imposed regulations"]
# plt.pie(df, labels = myLabels, autopct = "%1.1f%%")#(df, kind="pie", autopct="%1.1f%%")
# plt.title("Professor and TA Opinions on ChatGPT Usage")
# #plt.legend()
# plt.show()

#df = df.(["Student"])

#print(df)

#ax.set_title("ChatGPT Responses")

# df = chatgpt_responses.filter(items=["age", "gender"]).groupby(["age", "gender"]).value_counts().unstack().fillna(0)
# print(df)

# #Dictionary of the list of benefits
# benefitsDict = {"Idea generation" : 0, "Ease of access (Available 24/7, fast response etc.)" : 0, "Ability to summarize large amounts of data" : 0, "Being able to learn without instructors" : 0, "Able to converse in multiple languages" : 0, "Research assistance/Large knowledge base" : 0, "Other" : 0, "None" : 0}

# #Create a dictionary
# for lineNum in range(len(df)):
#   for word in df[lineNum].split(", "):
#     if (word in benefitsDict):
#       benefitsDict[word] += 1
#     #For option ease of access (Available 24/7, fast response etc), which splits the options and is read is not that option)
#     elif (word == "Ease of access (Available 24/7"): #Checks for the first half of the response
#       benefitsDict["Ease of access (Available 24/7, fast response etc.)"] += 1
#     elif (word == "fast response etc.)"):
#       continue #Ignores the second half of the response
#     else:
#       benefitsDict["Other"] += 1

# print(benefitsDict)

# #Break the plot into subplots
# plt.rcdefaults()
# fig, ax = plt.subplots()


# #Create the Y_axis
# Y = list(benefitsDict.keys())
# Y_axis = np.arange(len(Y))



# # Graph data

# ax.barh(Y_axis, list(benefitsDict.values()), align='center') #For every label in the Y axis, link it to the list of values
# ax.set_yticks(Y_axis, labels=Y)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel("Count")
# ax.set_title("Benefits Count of ChatGPT")

# plt.legend()
# plt.show()



  # #Make split graph
  # fig, ax = plt.subplots()
  # ax.bar(df.index, df["Male"], label="Male", color="#61AFEF")
  # ax.bar(df.index,
  #        df["Female"],
  #        bottom=df["Male"],
  #        label="Female",
  #        color="#FF99B4")
  # ax.bar(df.index,
  #        df["Non-binary/Non-conforming"],
  #        bottom=df["Male"] + df["Female"],
  #        label="Non-binary/Non-conforming",
  #        color="#FFEF00")
  # ax.bar(df.index,
  #        df["Prefer Not To Answer"],
  #        bottom=df["Male"] + df["Female"] + df["Non-binary/Non-conforming"],
  #        label="Prefer Not To Answer",
  #        color="#787976")

  # ax.set_title("Demographic of ChatGPT Survey")
  # ax.legend()
  # plt.show()
  
