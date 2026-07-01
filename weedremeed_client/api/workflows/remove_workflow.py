from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_workflow_response_400 import RemoveWorkflowResponse400
from ...models.remove_workflow_response_401 import RemoveWorkflowResponse401
from ...models.remove_workflow_response_403 import RemoveWorkflowResponse403
from ...models.remove_workflow_response_404 import RemoveWorkflowResponse404
from ...models.remove_workflow_response_500 import RemoveWorkflowResponse500
from ...types import Response


def _get_kwargs(
    workflow_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/weedremeed-api/workflow/{workflow_id}".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    None
    | RemoveWorkflowResponse400
    | RemoveWorkflowResponse401
    | RemoveWorkflowResponse403
    | RemoveWorkflowResponse404
    | RemoveWorkflowResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(None, response.json())
        return response_204

    if response.status_code == 400:
        response_400 = RemoveWorkflowResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RemoveWorkflowResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RemoveWorkflowResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveWorkflowResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RemoveWorkflowResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    None
    | RemoveWorkflowResponse400
    | RemoveWorkflowResponse401
    | RemoveWorkflowResponse403
    | RemoveWorkflowResponse404
    | RemoveWorkflowResponse500
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
    client: AuthenticatedClient | Client,
) -> Response[
    None
    | RemoveWorkflowResponse400
    | RemoveWorkflowResponse401
    | RemoveWorkflowResponse403
    | RemoveWorkflowResponse404
    | RemoveWorkflowResponse500
]:
    """Delete workflow

     Deletes a record of type Workflow.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[None | RemoveWorkflowResponse400 | RemoveWorkflowResponse401 | RemoveWorkflowResponse403 | RemoveWorkflowResponse404 | RemoveWorkflowResponse500]
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
    client: AuthenticatedClient | Client,
) -> (
    None
    | RemoveWorkflowResponse400
    | RemoveWorkflowResponse401
    | RemoveWorkflowResponse403
    | RemoveWorkflowResponse404
    | RemoveWorkflowResponse500
    | None
):
    """Delete workflow

     Deletes a record of type Workflow.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        None | RemoveWorkflowResponse400 | RemoveWorkflowResponse401 | RemoveWorkflowResponse403 | RemoveWorkflowResponse404 | RemoveWorkflowResponse500
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    None
    | RemoveWorkflowResponse400
    | RemoveWorkflowResponse401
    | RemoveWorkflowResponse403
    | RemoveWorkflowResponse404
    | RemoveWorkflowResponse500
]:
    """Delete workflow

     Deletes a record of type Workflow.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[None | RemoveWorkflowResponse400 | RemoveWorkflowResponse401 | RemoveWorkflowResponse403 | RemoveWorkflowResponse404 | RemoveWorkflowResponse500]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    None
    | RemoveWorkflowResponse400
    | RemoveWorkflowResponse401
    | RemoveWorkflowResponse403
    | RemoveWorkflowResponse404
    | RemoveWorkflowResponse500
    | None
):
    """Delete workflow

     Deletes a record of type Workflow.

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        None | RemoveWorkflowResponse400 | RemoveWorkflowResponse401 | RemoveWorkflowResponse403 | RemoveWorkflowResponse404 | RemoveWorkflowResponse500
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
        )
    ).parsed
