## need download and include Pendulum.  Faster than pytz.


import boto3
import pendulum
from datetime import date, timedelta, time

## for local testing
session = boto3.Session(profile_name='saml') ## case sensative, see "Session"


ssm_client = session.client('ssm') 

ssm_client.describe_maintenance_window_targets(
    WindowId='mw-059aaac63b89a5707'
)

ActiveMaintWindows = ssm_client.describe_maintenance_windows(
    Filters=[
        {
            'Key': 'Enabled',
            'Values': ['True']
        }
    ]
)

for (MaintWindow in ActiveMaintWindows)



ssm_client.describe_maintenance_windows_for_target(
    Targets=[
        {
            'Key': 'InstanceIds',
            'Values': [
                'i-0ea32706f0e094dfc'
            ]
        }
    ],
    ResourceType='INSTANCE'
)


tz = pendulum.timezone('America/Edmonton')
tz.convert(datetime.datetime.now().replace(second=0, microsecond=0)).isoformat()

thisweek = (datetime.datetime.now() + datetime.timedelta(days = 7)).isoformat()
datefilter = '*' + tz.convert((datetime.datetime.now() + datetime.timedelta(days = 7)).replace(second=0, microsecond=0)).isoformat()

ssm_client.describe_maintenance_window_schedule(
    WindowId='mw-059aaac63b89a5707',
    Filters=[
        {
            'Key': 'executiontime', 'Values': [datefilter]
        }
    ]
)


    # Filters=[
    #     {
    #         'Key': 'execution-time', 'Values': [datefilter]
    #     }
    # ]

    





response = client.describe_maintenance_window_targets(
    WindowId='string',
    Filters=[
        {
            'Key': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    MaxResults=123,
    NextToken='string'
)


response = client.describe_maintenance_window_schedule(
    WindowId='string',
    Targets=[
        {
            'Key': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    ResourceType='INSTANCE'|'RESOURCE_GROUP',
    Filters=[
        {
            'Key': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    MaxResults=123,
    NextToken='string'
)



client.describe_maintenance_windows_for_target(
    Targets=[
        {
            'Key': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    ResourceType='INSTANCE'|'RESOURCE_GROUP',
    MaxResults=123,
    NextToken='string'
)