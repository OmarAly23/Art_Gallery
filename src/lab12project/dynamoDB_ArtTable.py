import boto3
# DB_ENDPOINT AND DB_USERTABLE both represent the two variables created
# and signify variable for a table in the database
from lab12project.settings import DB_ENDPOINT, DB_ARTTABLE


# create table function for the users
def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=DB_ENDPOINT)

    table = dynamodb.create_table(
        TableName=DB_ARTTABLE,
        # it is only important to include the primary keys
    
        KeySchema=[
            {
                'AttributeName': 'art_title',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                # S for type string
                'AttributeName': 'art_title',
                'AttributeType': 'S'
            },
            # Here contains the attributes that the table should be comprised of
            # {
            #     # S for type string
            #     'AttributeName': 'art_image',
            #     'AttributeType': 'S'
            # },
            # {
            #     # S for type string
            #     'AttributeName': 'art_type',
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
    my_table.meta.client.get_waiter('table_exists').wait(TableName=DB_ARTTABLE)
    print("Table status:", my_table.table_status)
    print(my_table.item_count)

