from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_a_collections_content_get_a_collections_content_ok import (
    GetACollectionsContentGetACollectionsContentOk,
)
from ...models.get_a_collections_content_response_400 import GetACollectionsContentResponse400
from ...models.get_a_collections_content_response_500 import GetACollectionsContentResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/weedremeed-api/content/{collection_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetACollectionsContentGetACollectionsContentOk,
        GetACollectionsContentResponse400,
        GetACollectionsContentResponse500,
    ]
]:
    if response.status_code == 200:
        response_200 = GetACollectionsContentGetACollectionsContentOk.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetACollectionsContentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = GetACollectionsContentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetACollectionsContentGetACollectionsContentOk,
        GetACollectionsContentResponse400,
        GetACollectionsContentResponse500,
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
    cursor: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        GetACollectionsContentGetACollectionsContentOk,
        GetACollectionsContentResponse400,
        GetACollectionsContentResponse500,
    ]
]:
    """Get a collections content

     Paginate through a collections content

    Args:
        collection_id (str):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetACollectionsContentGetACollectionsContentOk, GetACollectionsContentResponse400, GetACollectionsContentResponse500]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        GetACollectionsContentGetACollectionsContentOk,
        GetACollectionsContentResponse400,
        GetACollectionsContentResponse500,
    ]
]:
    """Get a collections content

     Paginate through a collections content

    Args:
        collection_id (str):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetACollectionsContentGetACollectionsContentOk, GetACollectionsContentResponse400, GetACollectionsContentResponse500]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        GetACollectionsContentGetACollectionsContentOk,
        GetACollectionsContentResponse400,
        GetACollectionsContentResponse500,
    ]
]:
    """Get a collections content

     Paginate through a collections content

    Args:
        collection_id (str):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetACollectionsContentGetACollectionsContentOk, GetACollectionsContentResponse400, GetACollectionsContentResponse500]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        GetACollectionsContentGetACollectionsContentOk,
        GetACollectionsContentResponse400,
        GetACollectionsContentResponse500,
    ]
]:
    """Get a collections content

     Paginate through a collections content

    Args:
        collection_id (str):
        cursor (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetACollectionsContentGetACollectionsContentOk, GetACollectionsContentResponse400, GetACollectionsContentResponse500]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            cursor=cursor,
        )
    ).parsed
