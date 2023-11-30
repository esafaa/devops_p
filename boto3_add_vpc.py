import boto3
ec2  = boto3.client('ec2', region_name='ap-south-1')
ec2_resource = boto3.resource('ec2', region_name='ap-south-1')
new_vpc = ec2_resource.create_vpc(
    CidrBlock = "10.0.0.0/16"
)
new_vpc.create_subnet(
    CidrBlock = "10.0.1.0/24"
)
new_vpc.create_subnet(
    CidrBlock = "10.0.2.0/24"
)
new_vpc.create_tags(
    Tags=[
        {
        'Key':'Name',
        'Value':'es_vpc'
        },
    ]
)
allvpc = ec2.describe_vpcs()
vpcs = allvpc["Vpcs"]
for vpc in vpcs:
    print(vpc["VpcId"])
    cidr_set = vpc["CidrBlockAssociationSet"]
    for set in cidr_set:
        print(set["CidrBlockState"])
