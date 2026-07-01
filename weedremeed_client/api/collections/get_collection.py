from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection import Collection
from ...models.get_collection_response_400 import GetCollectionResponse400
from ...models.get_collection_response_401 import GetCollectionResponse401
from ...models.get_collection_response_404 import GetCollectionResponse404
from ...models.get_collection_response_500 import GetCollectionResponse500
from ...types import Response


def _get_kwargs(
    collection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/weedremeed-api/collection/{collection_id}".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Collection
    | GetCollectionResponse400
    | GetCollectionResponse401
    | GetCollectionResponse404
    | GetCollectionResponse500
    | None
):
    if response.status_code == 200:
        response_200 = Collection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetCollectionResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetCollectionResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = GetCollectionResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetCollectionResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Collection
    | GetCollectionResponse400
    | GetCollectionResponse401
    | GetCollectionResponse404
    | GetCollectionResponse500
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
    Collection
    | GetCollectionResponse400
    | GetCollectionResponse401
    | GetCollectionResponse404
    | GetCollectionResponse500
]:
    """Get collection

     Returns a record of type Collection.

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Collection | GetCollectionResponse400 | GetCollectionResponse401 | GetCollectionResponse404 | GetCollectionResponse500]
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
    Collection
    | GetCollectionResponse400
    | GetCollectionResponse401
    | GetCollectionResponse404
    | GetCollectionResponse500
    | None
):
    """Get collection

     Returns a record of type Collection.

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Collection | GetCollectionResponse400 | GetCollectionResponse401 | GetCollectionResponse404 | GetCollectionResponse500
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
    Collection
    | GetCollectionResponse400
    | GetCollectionResponse401
    | GetCollectionResponse404
    | GetCollectionResponse500
]:
    """Get collection

     Returns a record of type Collection.

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Collection | GetCollectionResponse400 | GetCollectionResponse401 | GetCollectionResponse404 | GetCollectionResponse500]
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
    Collection
    | GetCollectionResponse400
    | GetCollectionResponse401
    | GetCollectionResponse404
    | GetCollectionResponse500
    | None
):
    """Get collection

     Returns a record of type Collection.

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Collection | GetCollectionResponse400 | GetCollectionResponse401 | GetCollectionResponse404 | GetCollectionResponse500
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
        )
    ).parsed
