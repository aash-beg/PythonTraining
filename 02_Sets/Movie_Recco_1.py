#Movie recommendation system using jaccard distances
dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor",
                "hulk","krrish","ironman",'kgf','raw','lucy'],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal",
                "hera pheri","golmaal 2","dhamaal 2","hera pheri 2"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house",
               "kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri",
                  "raw","lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead",
                "conjuring","conjuring 2","bhootnath","aatma"]
}

user_1 = {'matrix','kgf','dabang','dhamaal','uri','bala','thor'}
user_2 = {'kgf','it','uri','thor','dabang','raw','lucy','bala'}
scores_1 = {}

# 1. find out that category whose movies are most common between two users
# 2. recommend those movies which user_1 has not seen yet but user_2 has seen and
# those movies must belong to the category that we found in step 1

for key in dataset:
    movies = dataset[key]
    movies = set(movies)
    numer = len(user_1.intersection(movies))
    denom = len(user_1.union(movies))
    sim = numer / denom
    scores_1[key] = round(sim,2)

scores_2 = {}

for key in dataset:
    movies = dataset[key]
    movies = set(movies)
    numer_2 = len(user_2.intersection(movies))
    denom_2 = len(user_2.union(movies))
    sim_2 = numer_2 / denom_2
    scores_2[key] = round(sim_2,2)

print(scores_1)
print("*" * 50)
print(scores_2)

common = user_2.intersection(user_1)
scores_3 = {}

for key in dataset:
    movies = dataset[key]
    movies = set(movies)
    numer_3 = len(common.intersection(movies))
    denom_3 = len(common.union(movies))
    sim_3 = numer_3 / denom_3
    scores_3[key] = round(sim_3,2)

print("*" * 50)
print(scores_3)

