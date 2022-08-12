from python_graphql_client import GraphqlClient
import pandas as pd

client = GraphqlClient(endpoint="https://api.github.com/graphql")

def make_query(repo_name, repo_owner, after_cursor=None):
    return """
    query{
        repository(name: NAME, owner: OWNER) {
    discussions(first: 100, after: AFTER) {
            pageInfo {
        hasNextPage
        endCursor
      }
      edges {cursor
        node {
          title
          bodyHTML
          createdAt
          author {
            login
          }
          url
          answerChosenAt
          comments (first:100){
          edges{cursor}
          nodes {
          bodyHTML
          createdAt
          author {login}
          url
          isAnswer
          }
          }
        }
      }
    }
  }}""".replace(
        "AFTER", '"{}"'.format(after_cursor) if after_cursor else "null").replace(
        "NAME", '"{}"'.format(repo_name) if repo_name else "null").replace(
        "OWNER", '"{}"'.format(repo_owner) if repo_owner else "null")


import json

# owner = ["alexanderby"]
# name = ['darkreader']

df_data = pd.read_csv('repo_list')
owner = df_data.Owner.to_list()
name = df_data.Repo.to_list()

def data_collection(repo_owner, repo_name):

    title = []
    body = []
    bodyhtml = []
    author = []
    answer = []
    url = []
    repository_name = []
    created = []
    cursor = []
    comment = []
    commenthtml = []
    comment_create = []
    comment_reaction = []
    comment_url = []
    isanswer = []
    CommentAuthor = []
    
    
    has_next_page = True
    after_cursor = None
    count = 0

    while has_next_page:

        data = client.execute(
            
            query=make_query(repo_name, repo_owner, after_cursor),
            
            headers={"Authorization": "Bearer {}".format('input_token')},)
        
        json.dumps(data, indent=4)

        for i in range(0, len(data['data']['repository']['discussions']['edges'])):
            
            for j in data['data']['repository']['discussions']['edges'][i]['node']['comments']['nodes']:
            
                repository_name.append(repo_name)

                title.append(data['data']['repository']['discussions']['edges'][i]['node']['title'])

                created.append(data['data']['repository']['discussions']['edges'][i]['node']['createdAt'])
                
#                 body.append(data['data']['repository']['discussions']['edges'][i]['node']['body'])
                
                bodyhtml.append(data['data']['repository']['discussions']['edges'][i]['node']['bodyHTML'])

                try:
                    author.append(data['data']['repository']['discussions']['edges'][i]['node']['author']['login'])

                except Exception:

                    author.append('None')

                url.append(data['data']['repository']['discussions']['edges'][i]['node']['url'])

                answer.append(data['data']['repository']['discussions']['edges'][i]['node']['answerChosenAt'])
                               
#                 comment.append(j['bodyText'])
                
                commenthtml.append(j['bodyHTML'])
                
                comment_create.append(j['createdAt'])
                
                try:
                    
                    CommentAuthor.append(j['author']['login'])
                    
                except Exception:

                    CommentAuthor.append('None')
                
                comment_url.append(j['url'])
                
                isanswer.append(int(j['isAnswer']))
                
#                 comment_reaction.append(j['reactionGroups'])

        has_next_page = data["data"]["repository"]["discussions"]["pageInfo"]["hasNextPage"]

        after_cursor = data["data"]["repository"]["discussions"]["pageInfo"]["endCursor"]

    df = pd.DataFrame({'Repository':repository_name, 'Title':title, 'BodyHTML':bodyhtml,
                       'Created':created, 'Author':author, 
                   'Answer':answer, 'URL': url, 'CommentHTML':commenthtml,
                       'Comment_time':comment_create, 'CommentAuthor': CommentAuthor,  
                      'Comment_URL': comment_url, 'IsAnswer': isanswer})

    return df

def combine(name):
    
    count = 0
    
    df_all=[]
    
    for i in range(0, len(name)):
        
        df = data_collection(owner[i], name[i])
    
        df_all.append(df)
        
        print (count)
        
        count = count + 1
        
    data_final = pd.concat(df_all, axis = 0).reset_index()
    
    return data_final
    


if __name__=='__main__':
    
    try:
    
        df_final_all = combine(name)
        
    except Exception:
        
        pass
