from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_workflows_in_a_collection_get_workflows_in_a_collection_forbidden import (
    GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden,
)
from ...models.get_workflows_in_a_collection_get_workflows_in_a_collection_unauthorised import (
    GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised,
)
from ...models.get_workflows_in_a_collection_response_404 import GetWorkflowsInACollectionResponse404
from ...models.workflow import Workflow
from ...types import Response


def _get_kwargs(
    collection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/weedremeed-api/collection_workflows/{collection_id}".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden
    | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised
    | GetWorkflowsInACollectionResponse404
    | list[Workflow]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Workflow.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetWorkflowsInACollectionResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden
    | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised
    | GetWorkflowsInACollectionResponse404
    | list[Workflow]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden
    | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised
    | GetWorkflowsInACollectionResponse404
    | list[Workflow]
]:
    """Get workflows in a collection

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised | GetWorkflowsInACollectionResponse404 | list[Workflow]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden
    | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised
    | GetWorkflowsInACollectionResponse404
    | list[Workflow]
    | None
):
    """Get workflows in a collection

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised | GetWorkflowsInACollectionResponse404 | list[Workflow]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden
    | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised
    | GetWorkflowsInACollectionResponse404
    | list[Workflow]
]:
    """Get workflows in a collection

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised | GetWorkflowsInACollectionResponse404 | list[Workflow]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden
    | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised
    | GetWorkflowsInACollectionResponse404
    | list[Workflow]
    | None
):
    """Get workflows in a collection

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkflowsInACollectionGetWorkflowsInACollectionForbidden | GetWorkflowsInACollectionGetWorkflowsInACollectionUnauthorised | GetWorkflowsInACollectionResponse404 | list[Workflow]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
        )
    ).parsed
