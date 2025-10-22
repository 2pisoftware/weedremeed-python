from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_workflow_response_400 import GetWorkflowResponse400
from ...models.get_workflow_response_401 import GetWorkflowResponse401
from ...models.get_workflow_response_403 import GetWorkflowResponse403
from ...models.get_workflow_response_404 import GetWorkflowResponse404
from ...models.get_workflow_response_500 import GetWorkflowResponse500
from ...models.workflow import Workflow
from ...types import Response


def _get_kwargs(
    workflow_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/weedremeed-api/workflow/{workflow_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetWorkflowResponse400,
        GetWorkflowResponse401,
        GetWorkflowResponse403,
        GetWorkflowResponse404,
        GetWorkflowResponse500,
        Workflow,
    ]
]:
    if response.status_code == 200:
        response_200 = Workflow.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetWorkflowResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetWorkflowResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetWorkflowResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetWorkflowResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetWorkflowResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetWorkflowResponse400,
        GetWorkflowResponse401,
        GetWorkflowResponse403,
        GetWorkflowResponse404,
        GetWorkflowResponse500,
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
    workflow_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        GetWorkflowResponse400,
        GetWorkflowResponse401,
        GetWorkflowResponse403,
        GetWorkflowResponse404,
        GetWorkflowResponse500,
        Workflow,
    ]
]:
    """Get workflow

     Returns a record of type Workflow.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWorkflowResponse400, GetWorkflowResponse401, GetWorkflowResponse403, GetWorkflowResponse404, GetWorkflowResponse500, Workflow]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        GetWorkflowResponse400,
        GetWorkflowResponse401,
        GetWorkflowResponse403,
        GetWorkflowResponse404,
        GetWorkflowResponse500,
        Workflow,
    ]
]:
    """Get workflow

     Returns a record of type Workflow.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWorkflowResponse400, GetWorkflowResponse401, GetWorkflowResponse403, GetWorkflowResponse404, GetWorkflowResponse500, Workflow]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        GetWorkflowResponse400,
        GetWorkflowResponse401,
        GetWorkflowResponse403,
        GetWorkflowResponse404,
        GetWorkflowResponse500,
        Workflow,
    ]
]:
    """Get workflow

     Returns a record of type Workflow.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWorkflowResponse400, GetWorkflowResponse401, GetWorkflowResponse403, GetWorkflowResponse404, GetWorkflowResponse500, Workflow]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        GetWorkflowResponse400,
        GetWorkflowResponse401,
        GetWorkflowResponse403,
        GetWorkflowResponse404,
        GetWorkflowResponse500,
        Workflow,
    ]
]:
    """Get workflow

     Returns a record of type Workflow.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWorkflowResponse400, GetWorkflowResponse401, GetWorkflowResponse403, GetWorkflowResponse404, GetWorkflowResponse500, Workflow]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
        )
    ).parsed
