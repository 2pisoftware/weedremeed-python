from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection import Collection
from ...models.collection_partial_update import CollectionPartialUpdate
from ...models.partial_update_collection_response_400 import PartialUpdateCollectionResponse400
from ...models.partial_update_collection_response_401 import PartialUpdateCollectionResponse401
from ...models.partial_update_collection_response_403 import PartialUpdateCollectionResponse403
from ...models.partial_update_collection_response_404 import PartialUpdateCollectionResponse404
from ...models.partial_update_collection_response_500 import PartialUpdateCollectionResponse500
from ...types import Response


def _get_kwargs(
    collection_id: str,
    *,
    body: CollectionPartialUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/weedremeed-api/collection/{collection_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Collection,
        PartialUpdateCollectionResponse400,
        PartialUpdateCollectionResponse401,
        PartialUpdateCollectionResponse403,
        PartialUpdateCollectionResponse404,
        PartialUpdateCollectionResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = Collection.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = PartialUpdateCollectionResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = PartialUpdateCollectionResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = PartialUpdateCollectionResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = PartialUpdateCollectionResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = PartialUpdateCollectionResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Collection,
        PartialUpdateCollectionResponse400,
        PartialUpdateCollectionResponse401,
        PartialUpdateCollectionResponse403,
        PartialUpdateCollectionResponse404,
        PartialUpdateCollectionResponse500,
    ]
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
    client: Union[AuthenticatedClient, Client],
    body: CollectionPartialUpdate,
) -> Response[
    Union[
        Collection,
        PartialUpdateCollectionResponse400,
        PartialUpdateCollectionResponse401,
        PartialUpdateCollectionResponse403,
        PartialUpdateCollectionResponse404,
        PartialUpdateCollectionResponse500,
    ]
]:
    """Patch collection

     Partially updates a record of type Collection.

    Args:
        collection_id (str):
        body (CollectionPartialUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collection, PartialUpdateCollectionResponse400, PartialUpdateCollectionResponse401, PartialUpdateCollectionResponse403, PartialUpdateCollectionResponse404, PartialUpdateCollectionResponse500]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CollectionPartialUpdate,
) -> Optional[
    Union[
        Collection,
        PartialUpdateCollectionResponse400,
        PartialUpdateCollectionResponse401,
        PartialUpdateCollectionResponse403,
        PartialUpdateCollectionResponse404,
        PartialUpdateCollectionResponse500,
    ]
]:
    """Patch collection

     Partially updates a record of type Collection.

    Args:
        collection_id (str):
        body (CollectionPartialUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Collection, PartialUpdateCollectionResponse400, PartialUpdateCollectionResponse401, PartialUpdateCollectionResponse403, PartialUpdateCollectionResponse404, PartialUpdateCollectionResponse500]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CollectionPartialUpdate,
) -> Response[
    Union[
        Collection,
        PartialUpdateCollectionResponse400,
        PartialUpdateCollectionResponse401,
        PartialUpdateCollectionResponse403,
        PartialUpdateCollectionResponse404,
        PartialUpdateCollectionResponse500,
    ]
]:
    """Patch collection

     Partially updates a record of type Collection.

    Args:
        collection_id (str):
        body (CollectionPartialUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Collection, PartialUpdateCollectionResponse400, PartialUpdateCollectionResponse401, PartialUpdateCollectionResponse403, PartialUpdateCollectionResponse404, PartialUpdateCollectionResponse500]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CollectionPartialUpdate,
) -> Optional[
    Union[
        Collection,
        PartialUpdateCollectionResponse400,
        PartialUpdateCollectionResponse401,
        PartialUpdateCollectionResponse403,
        PartialUpdateCollectionResponse404,
        PartialUpdateCollectionResponse500,
    ]
]:
    """Patch collection

     Partially updates a record of type Collection.

    Args:
        collection_id (str):
        body (CollectionPartialUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Collection, PartialUpdateCollectionResponse400, PartialUpdateCollectionResponse401, PartialUpdateCollectionResponse403, PartialUpdateCollectionResponse404, PartialUpdateCollectionResponse500]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
        )
    ).parsed
