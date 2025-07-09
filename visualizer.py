import pandas as pd
import plotly.express as exp
import plotly.graph_objects as go

ipldata = pd.read_csv('IPL2022_Data.csv')

print('\nFirst 10 ipl data:\n')
print(ipldata.head(10))

print('\n finding number of matches won by every team\n')
image = exp.bar(ipldata, x=ipldata['match_winner'], title='Number of Matches won in IPL 2022:')
image.show()

print('\nno. of matches won by defending or chasing\n')
ipldata['won_by'] = ipldata['won_by'].map({'Wickets': 'Chasing', 'Runs': 'Defending'})
won_by = ipldata['won_by'].value_counts()
label = won_by.index
counts = won_by.values
colors = ['Blue', 'Violet']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of matches won by defending /chasing')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=35,
                  marker=dict(colors=colors, line=dict(color='black', width=4)))
fig.show()

toss = ipldata['toss_decision'].value_counts()
label = toss.index
counts = toss.values
colors = ['Blue', 'Green']
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Toss Decision')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=35,
                  marker=dict(colors=colors, line=dict(color='black', width=4)))
fig.show()

figure = exp.bar(ipldata, x=ipldata['top_scorer'], y=ipldata['highscore'],
                 color=ipldata['highscore'], title='TATA IPL 2022 High Scores')
figure.show()

figure = exp.bar(ipldata, x=ipldata['player_of_the_match'], y=ipldata['player_of_the_match'],
                 color=ipldata['player_of_the_match'], title='TATA IPL 2022 Player of the Match')
figure.show()

figure = exp.bar(ipldata, x=ipldata['best_bowling'], title='TATA IPL 2022 Best Bowlers')
figure.show()

figure = go.Figure()
figure.add_trace(go.Bar(x=ipldata['venue'], y=ipldata['first_ings_wkts'],
                        name='First Inning Wickets', marker_color='red'))
figure.add_trace(go.Bar(x=ipldata['venue'], y=ipldata['second_ings_wkts'],
                        name='Second Inning Wickets', marker_color='orange'))
figure.update_layout(barmode='group', xaxis_tickangle=-45)
figure.show()

figure = go.Figure()
figure.add_trace(go.Bar(x=ipldata['venue'], y=ipldata['first_ings_score'],
                        name='First Inning Score', marker_color='blue'))
figure.add_trace(go.Bar(x=ipldata['venue'], y=ipldata['second_ings_score'],
                        name='Second Inning Score', marker_color='cyan'))
figure.update_layout(barmode='group', xaxis_tickangle=-45)
figure.show()
