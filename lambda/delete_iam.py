import boto3
import botocore
import json

iam = boto3.client('iam')


# def getarn():
#     response = iam.list_policies(
#         Scope='Local',
#         PathPrefix='/outpost/',
# )
    # for policy in response:
    #     for item in response['Policies']:
    #         for arn in item['Arn']:
    #             print(arn, end='')              
    #             deleteme = arn
    #             print(type(deleteme))
            
# getarn()
# print(response)
# print(response.get('Policies').get('PolicyName'))

# for policy in response:
#     for item in response[policy]:
#         print(item)

# for policy in response:
#     for item in response['Policies']:
#         for arn in item['Arn']:
#             print(arn)

response = iam.list_policies(
        Scope='Local',
        PathPrefix='/outpost/',
)
            
for policy in response:
    for item in response['Policies']:
        for arn in item['Arn']:
            print(arn, end='')
            
            delete = arn.join('')
            print(type(delete))