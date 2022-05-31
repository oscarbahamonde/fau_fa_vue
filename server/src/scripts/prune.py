from dotenv import load_dotenv
from os import getenv
load_dotenv()

AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION_NAME = getenv('AWS_REGION_NAME')

from boto3 import client

def get_client(service:str):
    return client(service,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION_NAME)

ec2 = get_client('ec2')

def delete_all_resources():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            res = ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
            print(res)

def delete_all_security_groups():
    response = ec2.describe_security_groups()
    for group in response['SecurityGroups']:
        if group['GroupName'] != 'default':
            res = ec2.delete_security_group(GroupId=group['GroupId'])
            print(res)
    print(response)

def delete_all_subnets():
    response = ec2.describe_subnets()
    for subnet in response['Subnets']:
        res = ec2.delete_subnet(SubnetId=subnet['SubnetId'])
        print(res)
    print(response)

def delete_all_vpc():
    response = ec2.describe_vpcs()
    for vpc in response['Vpcs']:
        res = ec2.delete_vpc(VpcId=vpc['VpcId'])
        print(res)
    print(response)

def delete_all_route_tables():
    response = ec2.describe_route_tables()
    for table in response['RouteTables']:
        res = ec2.delete_route_table(RouteTableId=table['RouteTableId'])
        print(res)
    print(response)

def delete_all_internet_gateways():
    response = ec2.describe_internet_gateways()
    for gateway in response['InternetGateways']:
        res = ec2.delete_internet_gateway(InternetGatewayId=gateway['InternetGatewayId'])
        print(res)
    print(response)

def delete_all_vpn_connections():
    response = ec2.describe_vpn_connections()
    for connection in response['VpnConnections']:
        res = ec2.delete_vpn_connection(VpnConnectionId=connection['VpnConnectionId'])
        print(res)
    print(response)

def delete_all_nics():
    response = ec2.describe_network_interfaces()
    for nic in response['NetworkInterfaces']:
        res = ec2.delete_network_interface(NetworkInterfaceId=nic['NetworkInterfaceId'])
        print(res)
    print(response)

def delete_all_instances():
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            res = ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
            print(res)
    print(response)

def delete_all_elb():
    response = ec2.describe_load_balancers()
    for elb in response['LoadBalancers']:
        res = ec2.delete_load_balancer(LoadBalancerName=elb['LoadBalancerName'])
        print(res)
    print(response)

def delete_all_ebs():
    response = ec2.describe_volumes()
    for volume in response['Volumes']:
        res = ec2.delete_volume(VolumeId=volume['VolumeId'])
        print(res)
    print(response)

def dettach_all_nics_and_ebs():
    response = ec2.describe_volumes()
    for volume in response['Volumes']:
        res = ec2.delete_volume(VolumeId=volume['VolumeId'])
        print(res)
    print(response)
    response = ec2.describe_network_interfaces()
    for nic in response['NetworkInterfaces']:
        res = ec2.delete_network_interface(NetworkInterfaceId=nic['NetworkInterfaceId'])
        print(res)
    print(response)

elastic_load_balancer = get_client('elb')

def delete_all_elastic_load_balancers():
    response = elastic_load_balancer.describe_load_balancers()
    for elb in response['LoadBalancerDescriptions']:
        res = elastic_load_balancer.delete_load_balancer(LoadBalancerName=elb['LoadBalancerName'])
        print(res)
    print(response)






