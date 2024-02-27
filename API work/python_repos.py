import requests

import plotly.graph_objs as go
from plotly.offline import plot

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

#visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]

my_layout = {
    'title': 'Most-Starred Python projects on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
plot(fig, filename='python_repos.html')

#print(response_dict.keys())
#print(f'Total repositores: {response_dict['total_count']}')
#print(f'Respositories returned: {len(repo_dicts)}')


#lists information available
""" repo_dict = repo_dicts[0]
print(f'\nKeys: {len(repo_dict)}')
for key in sorted(repo_dict.keys()):
    print(key) """

""" print('\nSeleccted information about first repository:')
for repo_dict in repo_dicts:
    print(f'\nName: {repo_dict['name']}')
    print(f'Owner: {repo_dict['owner']['login']}')
    print(f'Stars: {repo_dict['stargazers_count']}')
    print(f'Repository: {repo_dict['html_url']}')
    print(f'Created: {repo_dict['created_at']}')
    print(f'Updated: {repo_dict['updated_at']}')
    print(f'Description: {repo_dict['description']}') """

