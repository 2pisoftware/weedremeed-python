from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patch_workflow_response_400 import PatchWorkflowResponse400
from ...models.patch_workflow_response_401 import PatchWorkflowResponse401
from ...models.patch_workflow_response_403 import PatchWorkflowResponse403
from ...models.patch_workflow_response_404 import PatchWorkflowResponse404
from ...models.patch_workflow_response_500 import PatchWorkflowResponse500
from ...models.workflow import Workflow
from ...models.workflow_partial_update import WorkflowPartialUpdate
from ...types import Response


def _get_kwargs(
    workflow_id: str,
    *,
    body: WorkflowPartialUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/weedremeed-api/workflow/{workflow_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        PatchWorkflowResponse400,
        PatchWorkflowResponse401,
        PatchWorkflowResponse403,
        PatchWorkflowResponse404,
        PatchWorkflowResponse500,
        Workflow,
    ]
]:
    if response.status_code == 200:
        response_200 = Workflow.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PatchWorkflowResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = PatchWorkflowResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = PatchWorkflowResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = PatchWorkflowResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = PatchWorkflowResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        PatchWorkflowResponse400,
        PatchWorkflowResponse401,
        PatchWorkflowResponse403,
        PatchWorkflowResponse404,
        PatchWorkflowResponse500,
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
    client: AuthenticatedClient,
    body: WorkflowPartialUpdate,
) -> Response[
    Union[
        PatchWorkflowResponse400,
        PatchWorkflowResponse401,
        PatchWorkflowResponse403,
        PatchWorkflowResponse404,
        PatchWorkflowResponse500,
        Workflow,
    ]
]:
    """Patch workflow

     Partially updates a record of type Workflow.

    Args:
        workflow_id (str):
        body (WorkflowPartialUpdate): Data transfer object for partially updating an existing
            Workflow (PATCH operation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PatchWorkflowResponse400, PatchWorkflowResponse401, PatchWorkflowResponse403, PatchWorkflowResponse404, PatchWorkflowResponse500, Workflow]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: WorkflowPartialUpdate,
) -> Optional[
    Union[
        PatchWorkflowResponse400,
        PatchWorkflowResponse401,
        PatchWorkflowResponse403,
        PatchWorkflowResponse404,
        PatchWorkflowResponse500,
        Workflow,
    ]
]:
    """Patch workflow

     Partially updates a record of type Workflow.

    Args:
        workflow_id (str):
        body (WorkflowPartialUpdate): Data transfer object for partially updating an existing
            Workflow (PATCH operation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PatchWorkflowResponse400, PatchWorkflowResponse401, PatchWorkflowResponse403, PatchWorkflowResponse404, PatchWorkflowResponse500, Workflow]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: WorkflowPartialUpdate,
) -> Response[
    Union[
        PatchWorkflowResponse400,
        PatchWorkflowResponse401,
        PatchWorkflowResponse403,
        PatchWorkflowResponse404,
        PatchWorkflowResponse500,
        Workflow,
    ]
]:
    """Patch workflow

     Partially updates a record of type Workflow.

    Args:
        workflow_id (str):
        body (WorkflowPartialUpdate): Data transfer object for partially updating an existing
            Workflow (PATCH operation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PatchWorkflowResponse400, PatchWorkflowResponse401, PatchWorkflowResponse403, PatchWorkflowResponse404, PatchWorkflowResponse500, Workflow]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    body: WorkflowPartialUpdate,
) -> Optional[
    Union[
        PatchWorkflowResponse400,
        PatchWorkflowResponse401,
        PatchWorkflowResponse403,
        PatchWorkflowResponse404,
        PatchWorkflowResponse500,
        Workflow,
    ]
]:
    """Patch workflow

     Partially updates a record of type Workflow.

    Args:
        workflow_id (str):
        body (WorkflowPartialUpdate): Data transfer object for partially updating an existing
            Workflow (PATCH operation).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PatchWorkflowResponse400, PatchWorkflowResponse401, PatchWorkflowResponse403, PatchWorkflowResponse404, PatchWorkflowResponse500, Workflow]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            body=body,
        )
    ).parsed
