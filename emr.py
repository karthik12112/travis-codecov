import boto3

client = boto3.client('emr',region_name='us-west-2')
paginatorq = client.get_paginator('list_instances')
paginator = client.get_paginator('list_clusters')
response_iterator = paginator.paginate(
    ClusterStates=[
        'WAITING','RUNNING',
    ],
)
for page in response_iterator:
   for i in range(len(page['Clusters'])):
      page['Clusters'][i]['Name']



response_iterator = paginatorq.paginate(
          ClusterId='string',
)
