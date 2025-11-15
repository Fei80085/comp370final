import json
import os

folder_inner = 'Sources'
file_name = 'source'
big_dict = []

for i in range(1, 21):
    name = file_name = 'sources' + str(i) + '.json'

    true_file_name = os.path.join(folder_inner, name)

    with open(true_file_name) as f:
        myjson = json.load(f)

    just_the_news = myjson['data']

    for num in range(len(just_the_news)):
        if just_the_news[num]['locale'] == 'us':
            big_dict.append(just_the_news[num])
            print(just_the_news[num])


for b in range(len(big_dict)):
    print(big_dict[b]['domain'])


with open('us_sources.json', 'w') as fh:
    json.dump(big_dict, fh)