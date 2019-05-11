import boto3
client = boto3.client('rekognition')


# to enter data into collection
response = client.index_faces(
CollectionId = 'project2',
Image={
    'S3Object': {
        'Bucket': 'testsnaps',
        'Name': 'Darpan.jpeg',
    }
},
ExternalImageId='Darpan',
DetectionAttributes=[
    'ALL',
]
)



# to check data stored in collection "project"
response = client.list_faces(
    CollectionId='project1'
)


# to delete a collection
response = client.delete_collection(
    CollectionId='project2'
)


# to create a new collection
response = client.create_collection(
    CollectionId='project2'
)