from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_workflow_response_400 import CreateWorkflowResponse400
from ...models.create_workflow_response_401 import CreateWorkflowResponse401
from ...models.create_workflow_response_403 import CreateWorkflowResponse403
from ...models.create_workflow_response_404 import CreateWorkflowResponse404
from ...models.create_workflow_response_409 import CreateWorkflowResponse409
from ...models.create_workflow_response_500 import CreateWorkflowResponse500
from ...models.workflow import Workflow
from ...models.workflow_create import WorkflowCreate
from ...types import Response


def _get_kwargs(
    *,
    body: WorkflowCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/weedremeed-api/workflow",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        CreateWorkflowResponse400,
        CreateWorkflowResponse401,
        CreateWorkflowResponse403,
        CreateWorkflowResponse404,
        CreateWorkflowResponse409,
        CreateWorkflowResponse500,
        Workflow,
    ]
]:
    if response.status_code == 201:
        response_201 = Workflow.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = CreateWorkflowResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CreateWorkflowResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CreateWorkflowResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = CreateWorkflowResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = CreateWorkflowResponse409.from_dict(response.json())

        return response_409
    if response.status_code == 500:
        response_500 = CreateWorkflowResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        CreateWorkflowResponse400,
        CreateWorkflowResponse401,
        CreateWorkflowResponse403,
        CreateWorkflowResponse404,
        CreateWorkflowResponse409,
        CreateWorkflowResponse500,
        Workflow,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowCreate,
) -> Response[
    Union[
        CreateWorkflowResponse400,
        CreateWorkflowResponse401,
        CreateWorkflowResponse403,
        CreateWorkflowResponse404,
        CreateWorkflowResponse409,
        CreateWorkflowResponse500,
        Workflow,
    ]
]:
    """Create workflow

     Creates a new record of type Workflow.

    Args:
        body (WorkflowCreate): Data transfer object for creating a new Workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWorkflowResponse400, CreateWorkflowResponse401, CreateWorkflowResponse403, CreateWorkflowResponse404, CreateWorkflowResponse409, CreateWorkflowResponse500, Workflow]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowCreate,
) -> Optional[
    Union[
        CreateWorkflowResponse400,
        CreateWorkflowResponse401,
        CreateWorkflowResponse403,
        CreateWorkflowResponse404,
        CreateWorkflowResponse409,
        CreateWorkflowResponse500,
        Workflow,
    ]
]:
    """Create workflow

     Creates a new record of type Workflow.

    Args:
        body (WorkflowCreate): Data transfer object for creating a new Workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWorkflowResponse400, CreateWorkflowResponse401, CreateWorkflowResponse403, CreateWorkflowResponse404, CreateWorkflowResponse409, CreateWorkflowResponse500, Workflow]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowCreate,
) -> Response[
    Union[
        CreateWorkflowResponse400,
        CreateWorkflowResponse401,
        CreateWorkflowResponse403,
        CreateWorkflowResponse404,
        CreateWorkflowResponse409,
        CreateWorkflowResponse500,
        Workflow,
    ]
]:
    """Create workflow

     Creates a new record of type Workflow.

    Args:
        body (WorkflowCreate): Data transfer object for creating a new Workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWorkflowResponse400, CreateWorkflowResponse401, CreateWorkflowResponse403, CreateWorkflowResponse404, CreateWorkflowResponse409, CreateWorkflowResponse500, Workflow]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: WorkflowCreate,
) -> Optional[
    Union[
        CreateWorkflowResponse400,
        CreateWorkflowResponse401,
        CreateWorkflowResponse403,
        CreateWorkflowResponse404,
        CreateWorkflowResponse409,
        CreateWorkflowResponse500,
        Workflow,
    ]
]:
    """Create workflow

     Creates a new record of type Workflow.

    Args:
        body (WorkflowCreate): Data transfer object for creating a new Workflow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWorkflowResponse400, CreateWorkflowResponse401, CreateWorkflowResponse403, CreateWorkflowResponse404, CreateWorkflowResponse409, CreateWorkflowResponse500, Workflow]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
