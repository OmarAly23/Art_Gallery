import boto3
# DB_ENDPOINT AND DB_USERTABLE both represent the two variables created
# and signify variable for a table in the database
from lab12project.settings import DB_ENDPOINT, DB_USERTABLE


def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=DB_ENDPOINT)

    table = dynamodb.create_table(
        TableName=DB_USERTABLE,
        # it is only important to include the primary keys
        KeySchema=[
            {
                'AttributeName': 'email',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                # S for type string
                'AttributeName': 'email',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 2
        }
    )
    return table


if __name__ == '__main__':
    my_table = create_table()
    my_table.meta.client.get_waiter('table_exists').wait(TableName=DB_USERTABLE)
    print("Table status:", my_table.table_status)
    print(my_table.item_count)
