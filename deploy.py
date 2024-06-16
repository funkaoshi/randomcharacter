#!/usr/bin/env python3

import argparse
import boto3

# Set up argparse
parser = argparse.ArgumentParser(description="Deploy a new version of the API to ECS")
parser.add_argument("-c", "--cluster", help="The name of the ECS cluster to deploy to")
parser.add_argument("-s", "--service", help="The name of the ECS service to deploy to")
parser.add_argument(
    "-a",
    "--aws_profile",
    help="The name of the AWS profile to use",
    default="osrbeyond",
)
parser.add_argument(
    "-v", "--version", help="The version tag of the API image to deploy"
)
args = parser.parse_args()

# Initialize a session using AWS profile
session = boto3.Session(profile_name=args.aws_profile, region_name="us-east-1")

# Create an ECS client
ecs = session.client("ecs")
print(
    "Deploying version {} of the API to ECS cluster {} and service {}".format(
        args.version, args.cluster, args.service
    )
)

# Fetch the current task definition of the service
response = ecs.describe_services(cluster=args.cluster, services=[args.service])
task_definition_name = response["services"][0]["taskDefinition"]
print("Current task definition: {}".format(task_definition_name))

response = ecs.describe_task_definition(
    taskDefinition=task_definition_name,
    include=[
        "TAGS",
    ],
)
task_definition = response["taskDefinition"]

# Create a new task definition with the new image
task_definition["containerDefinitions"][0][
    "image"
] = "295382441385.dkr.ecr.us-east-1.amazonaws.com/osrbeyond-random:{}".format(args.version)

response = ecs.register_task_definition(
    family=task_definition["family"],
    taskRoleArn=task_definition["taskRoleArn"],
    executionRoleArn=task_definition["executionRoleArn"],
    networkMode=task_definition["networkMode"],
    containerDefinitions=task_definition["containerDefinitions"],
    volumes=task_definition["volumes"],
    placementConstraints=task_definition["placementConstraints"],
    requiresCompatibilities=task_definition["requiresCompatibilities"],
    cpu=task_definition["cpu"],
    memory=task_definition["memory"],
    tags=response["tags"],
    runtimePlatform=task_definition["runtimePlatform"],
)
print("New task definition: {}".format(response["taskDefinition"]["taskDefinitionArn"]))

# Update the service with the new task definition
response = ecs.update_service(
    cluster=args.cluster,
    service=args.service,
    taskDefinition=response["taskDefinition"]["taskDefinitionArn"],
)
print("Updated service: {}".format(response["service"]["serviceArn"]))
