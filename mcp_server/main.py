# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:05:32+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header, Path, Query
from pydantic import constr

from models import (
    AssociateResourceResponse,
    BadRequestException,
    CanariesLastRunPostRequest,
    CanariesPostRequest,
    CanaryNamePatchRequest,
    CanaryNameRunsPostRequest,
    CanaryPostRequest,
    ConflictException,
    CreateCanaryResponse,
    CreateGroupResponse,
    DeleteCanaryResponse,
    DeleteGroupResponse,
    DescribeCanariesLastRunResponse,
    DescribeCanariesResponse,
    DescribeRuntimeVersionsResponse,
    DisassociateResourceResponse,
    GetCanaryResponse,
    GetCanaryRunsResponse,
    GetGroupResponse,
    GroupGroupIdentifierAssociatePatchRequest,
    GroupGroupIdentifierDisassociatePatchRequest,
    GroupGroupIdentifierResourcesPostRequest,
    GroupPostRequest,
    GroupsPostRequest,
    InternalFailureException,
    InternalServerException,
    ListAssociatedGroupsResponse,
    ListGroupResourcesResponse,
    ListGroupsResponse,
    ListTagsForResourceResponse,
    NotFoundException,
    RequestEntityTooLargeException,
    ResourceNotFoundException,
    ResourceResourceArnGroupsPostRequest,
    RuntimeVersionsPostRequest,
    ServiceQuotaExceededException,
    StartCanaryResponse,
    StopCanaryResponse,
    TagKeys,
    TagResourceResponse,
    TagsResourceArnPostRequest,
    TooManyRequestsException,
    UntagResourceResponse,
    UpdateCanaryResponse,
    ValidationException,
)

app = MCPProxy(
    contact={
        'email': 'mike.ralphson@gmail.com',
        'name': 'Mike Ralphson',
        'url': 'https://github.com/mermade/aws2openapi',
        'x-twitter': 'PermittedSoc',
    },
    description='<fullname>Amazon CloudWatch Synthetics</fullname> <p>You can use Amazon CloudWatch Synthetics to continually monitor your services. You can create and manage <i>canaries</i>, which are modular, lightweight scripts that monitor your endpoints and APIs from the outside-in. You can set up your canaries to run 24 hours a day, once per minute. The canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. The canaries seamlessly integrate with CloudWatch ServiceLens to help you trace the causes of impacted nodes in your applications. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html">Using ServiceLens to Monitor the Health of Your Applications</a> in the <i>Amazon CloudWatch User Guide</i>.</p> <p>Before you create and manage canaries, be aware of the security considerations. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html">Security Considerations for Synthetics Canaries</a>.</p>',
    license={'name': 'Apache 2.0 License', 'url': 'http://www.apache.org/licenses/'},
    termsOfService='https://aws.amazon.com/service-terms/',
    title='Synthetics',
    version='2017-10-11',
    servers=[
        {
            'description': 'The Synthetics multi-region endpoint',
            'url': 'http://synthetics.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The Synthetics multi-region endpoint',
            'url': 'https://synthetics.{region}.amazonaws.com',
            'variables': {
                'region': {
                    'default': 'us-east-1',
                    'description': 'The AWS region',
                    'enum': [
                        'us-east-1',
                        'us-east-2',
                        'us-west-1',
                        'us-west-2',
                        'us-gov-west-1',
                        'us-gov-east-1',
                        'ca-central-1',
                        'eu-north-1',
                        'eu-west-1',
                        'eu-west-2',
                        'eu-west-3',
                        'eu-central-1',
                        'eu-south-1',
                        'af-south-1',
                        'ap-northeast-1',
                        'ap-northeast-2',
                        'ap-northeast-3',
                        'ap-southeast-1',
                        'ap-southeast-2',
                        'ap-east-1',
                        'ap-south-1',
                        'sa-east-1',
                        'me-south-1',
                    ],
                }
            },
        },
        {
            'description': 'The Synthetics endpoint for China (Beijing) and China (Ningxia)',
            'url': 'http://synthetics.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
        {
            'description': 'The Synthetics endpoint for China (Beijing) and China (Ningxia)',
            'url': 'https://synthetics.{region}.amazonaws.com.cn',
            'variables': {
                'region': {
                    'default': 'cn-north-1',
                    'description': 'The AWS region',
                    'enum': ['cn-north-1', 'cn-northwest-1'],
                }
            },
        },
    ],
)


@app.post(
    '/canaries',
    description=""" <p>This operation returns a list of the canaries in your account, along with full details about each canary.</p> <p>This operation supports resource-level authorization using an IAM policy and the <code>Names</code> parameter. If you specify the <code>Names</code> parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.</p> <p>You are required to use the <code>Names</code> parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html"> Limiting a user to viewing specific canaries</a>.</p> """,
    tags=['canary_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_canaries(
    max_results: Optional[str] = Query(None, alias='MaxResults'),
    next_token: Optional[str] = Query(None, alias='NextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: CanariesPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/canaries/last-run',
    description=""" <p>Use this operation to see information from the most recent run of each canary that you have created.</p> <p>This operation supports resource-level authorization using an IAM policy and the <code>Names</code> parameter. If you specify the <code>Names</code> parameter, the operation is successful only if you have authorization to view all the canaries that you specify in your request. If you do not have permission to view any of the canaries, the request fails with a 403 response.</p> <p>You are required to use the <code>Names</code> parameter if you are logged on to a user or role that has an IAM policy that restricts which canaries that you are allowed to view. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Restricted.html"> Limiting a user to viewing specific canaries</a>.</p> """,
    tags=['canary_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_canaries_last_run(
    max_results: Optional[str] = Query(None, alias='MaxResults'),
    next_token: Optional[str] = Query(None, alias='NextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: CanariesLastRunPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/canary',
    description=""" <p>Creates a canary. Canaries are scripts that monitor your endpoints and APIs from the outside-in. Canaries help you check the availability and latency of your web services and troubleshoot anomalies by investigating load time data, screenshots of the UI, logs, and metrics. You can set up a canary to run continuously or just once. </p> <p>Do not use <code>CreateCanary</code> to modify an existing canary. Use <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_UpdateCanary.html">UpdateCanary</a> instead.</p> <p>To create canaries, you must have the <code>CloudWatchSyntheticsFullAccess</code> policy. If you are creating a new IAM role for the canary, you also need the <code>iam:CreateRole</code>, <code>iam:CreatePolicy</code> and <code>iam:AttachRolePolicy</code> permissions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Roles">Necessary Roles and Permissions</a>.</p> <p>Do not include secrets or proprietary information in your canary names. The canary name makes up part of the Amazon Resource Name (ARN) for the canary, and the ARN is included in outbound calls over the internet. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html">Security Considerations for Synthetics Canaries</a>.</p> """,
    tags=['canary_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_canary(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: CanaryPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/canary/{name}',
    description=""" <p>Permanently deletes the specified canary.</p> <p>If you specify <code>DeleteLambda</code> to <code>true</code>, CloudWatch Synthetics also deletes the Lambda functions and layers that are used by the canary.</p> <p>Other resources used and created by the canary are not automatically deleted. After you delete a canary that you do not intend to use again, you should also delete the following:</p> <ul> <li> <p>The CloudWatch alarms created for this canary. These alarms have a name of <code>Synthetics-SharpDrop-Alarm-<i>MyCanaryName</i> </code>.</p> </li> <li> <p>Amazon S3 objects and buckets, such as the canary's artifact location.</p> </li> <li> <p>IAM roles created for the canary. If they were created in the console, these roles have the name <code> role/service-role/CloudWatchSyntheticsRole-<i>MyCanaryName</i> </code>.</p> </li> <li> <p>CloudWatch Logs log groups created for the canary. These logs groups have the name <code>/aws/lambda/cwsyn-<i>MyCanaryName</i> </code>. </p> </li> </ul> <p>Before you delete a canary, you might want to use <code>GetCanary</code> to display the information about this canary. Make note of the information returned by this operation so that you can delete these resources after you delete the canary.</p> """,
    tags=['canary_management', 'group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_canary(
    name: constr(pattern=r'^[0-9a-z_\-]+$', min_length=1, max_length=21),
    delete_lambda: Optional[bool] = Query(None, alias='deleteLambda'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/canary/{name}',
    description=""" Retrieves complete information about one canary. You must specify the name of the canary that you want. To get a list of canaries and their names, use <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html">DescribeCanaries</a>. """,
    tags=['group_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def get_canary(
    name: constr(pattern=r'^[0-9a-z_\-]+$', min_length=1, max_length=21),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/canary/{name}',
    description=""" <p>Updates the configuration of a canary that has already been created.</p> <p>You can't use this operation to update the tags of an existing canary. To change the tags of an existing canary, use <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_TagResource.html">TagResource</a>.</p> """,
    tags=['canary_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def update_canary(
    name: constr(pattern=r'^[0-9a-z_\-]+$', min_length=1, max_length=21),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: CanaryNamePatchRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/canary/{name}/runs',
    description=""" Retrieves a list of runs for a specified canary. """,
    tags=['canary_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def get_canary_runs(
    name: constr(pattern=r'^[0-9a-z_\-]+$', min_length=1, max_length=21),
    max_results: Optional[str] = Query(None, alias='MaxResults'),
    next_token: Optional[str] = Query(None, alias='NextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: CanaryNameRunsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/canary/{name}/start',
    description=""" Use this operation to run a canary that has already been created. The frequency of the canary runs is determined by the value of the canary's <code>Schedule</code>. To see a canary's schedule, use <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanary.html">GetCanary</a>. """,
    tags=['group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def start_canary(
    name: constr(pattern=r'^[0-9a-z_\-]+$', min_length=1, max_length=21),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/canary/{name}/stop',
    description=""" <p>Stops the canary to prevent all future runs. If the canary is currently running,the run that is in progress completes on its own, publishes metrics, and uploads artifacts, but it is not recorded in Synthetics as a completed run.</p> <p>You can use <code>StartCanary</code> to start it running again with the canary’s current schedule at any point in the future. </p> """,
    tags=['group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def stop_canary(
    name: constr(pattern=r'^[0-9a-z_\-]+$', min_length=1, max_length=21),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/group',
    description=""" <p>Creates a group which you can use to associate canaries with each other, including cross-Region canaries. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group. </p> <p>Groups are global resources. When you create a group, it is replicated across Amazon Web Services Regions, and you can view it and add canaries to it from any Region. Although the group ARN format reflects the Region name where it was created, a group is not constrained to any Region. This means that you can put canaries from multiple Regions into the same group, and then use that group to view and manage all of those canaries in a single view.</p> <p>Groups are supported in all Regions except the Regions that are disabled by default. For more information about these Regions, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable">Enabling a Region</a>.</p> <p>Each group can contain as many as 10 canaries. You can have as many as 20 groups in your account. Any single canary can be a member of up to 10 groups.</p> """,
    tags=['resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def create_group(
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: GroupPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/group/{groupIdentifier}',
    description=""" <p>Deletes a group. The group doesn't need to be empty to be deleted. If there are canaries in the group, they are not deleted when you delete the group. </p> <p>Groups are a global resource that appear in all Regions, but the request to delete a group must be made from its home Region. You can find the home Region of a group within its ARN.</p> """,
    tags=['group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def delete_group(
    group_identifier: constr(min_length=1, max_length=128) = Path(
        ..., alias='groupIdentifier'
    ),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/group/{groupIdentifier}',
    description=""" Returns information about one group. Groups are a global resource, so you can use this operation from any Region. """,
    tags=['group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def get_group(
    group_identifier: constr(min_length=1, max_length=128) = Path(
        ..., alias='groupIdentifier'
    ),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/group/{groupIdentifier}/associate',
    description=""" <p>Associates a canary with a group. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group. </p> <p>You must run this operation in the Region where the canary exists.</p> """,
    tags=['group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def associate_resource(
    group_identifier: constr(min_length=1, max_length=128) = Path(
        ..., alias='groupIdentifier'
    ),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: GroupGroupIdentifierAssociatePatchRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/group/{groupIdentifier}/disassociate',
    description=""" Removes a canary from a group. You must run this operation in the Region where the canary exists. """,
    tags=['group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def disassociate_resource(
    group_identifier: constr(min_length=1, max_length=128) = Path(
        ..., alias='groupIdentifier'
    ),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: GroupGroupIdentifierDisassociatePatchRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/group/{groupIdentifier}/resources',
    description=""" This operation returns a list of the ARNs of the canaries that are associated with the specified group. """,
    tags=['group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_group_resources(
    group_identifier: constr(min_length=1, max_length=128) = Path(
        ..., alias='groupIdentifier'
    ),
    max_results: Optional[str] = Query(None, alias='MaxResults'),
    next_token: Optional[str] = Query(None, alias='NextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: GroupGroupIdentifierResourcesPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/groups',
    description=""" Returns a list of all groups in the account, displaying their names, unique IDs, and ARNs. The groups from all Regions are returned. """,
    tags=['group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_groups(
    max_results: Optional[str] = Query(None, alias='MaxResults'),
    next_token: Optional[str] = Query(None, alias='NextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: GroupsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/resource/{resourceArn}/groups',
    description=""" Returns a list of the groups that the specified canary is associated with. The canary that you specify must be in the current Region. """,
    tags=['canary_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_associated_groups(
    resource_arn: constr(
        pattern=r'arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:canary:[0-9a-z_\-]{1,21}',
        min_length=1,
        max_length=2048,
    ) = Path(..., alias='resourceArn'),
    max_results: Optional[str] = Query(None, alias='MaxResults'),
    next_token: Optional[str] = Query(None, alias='NextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: ResourceResourceArnGroupsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/runtime-versions',
    description=""" Returns a list of Synthetics canary runtime versions. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html"> Canary Runtime Versions</a>. """,
    tags=['runtime_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def describe_runtime_versions(
    max_results: Optional[str] = Query(None, alias='MaxResults'),
    next_token: Optional[str] = Query(None, alias='NextToken'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: RuntimeVersionsPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/tags/{resourceArn}',
    description=""" Displays the tags associated with a canary or group. """,
    tags=['canary_management', 'group_management', 'resource_association_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def list_tags_for_resource(
    resource_arn: constr(
        pattern=r'arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:(canary|group):[0-9a-z_\-]+',
        min_length=1,
        max_length=2048,
    ) = Path(..., alias='resourceArn'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/tags/{resourceArn}',
    description=""" <p>Assigns one or more tags (key-value pairs) to the specified canary or group. </p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a canary or group.</p> """,
    tags=[
        'canary_management',
        'group_management',
        'resource_tagging',
        'resource_association_management',
    ],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def tag_resource(
    resource_arn: constr(
        pattern=r'arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:(canary|group):[0-9a-z_\-]+',
        min_length=1,
        max_length=2048,
    ) = Path(..., alias='resourceArn'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
    body: TagsResourceArnPostRequest = ...,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/tags/{resourceArn}#tagKeys',
    description=""" Removes one or more tags from the specified resource. """,
    tags=['canary_management', 'group_management', 'resource_tagging'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def untag_resource(
    resource_arn: constr(
        pattern=r'arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:(canary|group):[0-9a-z_\-]+',
        min_length=1,
        max_length=2048,
    ) = Path(..., alias='resourceArn'),
    tag_keys: TagKeys = Query(..., alias='tagKeys'),
    x__amz__content__sha256: Optional[str] = Header(None, alias='X-Amz-Content-Sha256'),
    x__amz__date: Optional[str] = Header(None, alias='X-Amz-Date'),
    x__amz__algorithm: Optional[str] = Header(None, alias='X-Amz-Algorithm'),
    x__amz__credential: Optional[str] = Header(None, alias='X-Amz-Credential'),
    x__amz__security__token: Optional[str] = Header(None, alias='X-Amz-Security-Token'),
    x__amz__signature: Optional[str] = Header(None, alias='X-Amz-Signature'),
    x__amz__signed_headers: Optional[str] = Header(None, alias='X-Amz-SignedHeaders'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
