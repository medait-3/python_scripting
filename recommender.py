from surprise import  KNNBasic
import pandas as pd 
from surprise import Dataset
from surprise import Reader

movies=['star','med','got','good']
rating=[1,3,4,1]
users=['kim','jhon','frid','med']

rating_dict={'user' : users,
             'item':movies,
              'rating':rating}

def Rcommande(user):
    df=pd.DataFrame(rating_dict)
    reader = Reader(rating_scale=(1,5))
    data= Dataset.load_from_df(df[['user','item','rating']],reader)
    trainset=data.build_full_trainset()
    sim_options={'name':'cosine','user_based':True}

    algo=KNNBasic(sim_options)
    algo.fit(trainset)

    uid=trainset.to_inner_uid(user)
    pred=algo.get_neighbors(uid, 1)

    for i in pred:
        print(trainset.to_raw_uid(i))

Rcommande('med')