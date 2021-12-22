import boto3
# DB_ENDPOINT AND DB_USERTABLE both represent the two variables created
# and signify variable for a table in the database
from lab12project.settings import DB_ENDPOINT, DB_ARTSITSTABLE


# create table function for the users
def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=DB_ENDPOINT)

    table = dynamodb.create_table(
        TableName=DB_ARTSITSTABLE,
        # it is only important to include the primary keys
    
        KeySchema=[
            {
                'AttributeName': 'artistID',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                # S for type string
                'AttributeName': 'artistID',
                'AttributeType': 'S'
            },
            # {
            #     # S for type string
            #     'AttributeName': 'artistName',
            #     'AttributeType': 'S'
            # },
            # {
            #     # S for type string
            #     'AttributeName': 'state',
            #     'AttributeType': 'S'
            # },
            # {
            #     # S for type string
            #     'AttributeName': 'country',
            #     'AttributeType': 'S'
            # },
            # {
            #     # S for type string
            #     'AttributeName': 'wiki_page',
            #     'AttributeType': 'S'
            # },
            # {
            #     # S for type string
            #     'AttributeName': 'DOB',
            #     'AttributeType': 'S'
            # },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    my_table = create_table()
    my_table.meta.client.get_waiter('table_exists').wait(TableName=DB_ARTSITSTABLE)
    print("Table status:", my_table.table_status)
    print(my_table.item_count)

