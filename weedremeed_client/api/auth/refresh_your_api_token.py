from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.refresh_your_api_token_login_ok import RefreshYourApiTokenLoginOk
from ...models.refresh_your_api_token_login_unauthorised import RefreshYourApiTokenLoginUnauthorised
from ...types import Response


def _get_kwargs(
    *,
    body: None,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/weedremeed-api/refresh",
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised | None:
    if response.status_code == 200:
        response_200 = RefreshYourApiTokenLoginOk.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = RefreshYourApiTokenLoginUnauthorised.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: None,
) -> Response[RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised]:
    """Refresh your API token

     Renew/refresh the expiry of your API token

    Args:
        body (None):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised]
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
    client: AuthenticatedClient | Client,
    body: None,
) -> RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised | None:
    """Refresh your API token

     Renew/refresh the expiry of your API token

    Args:
        body (None):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: None,
) -> Response[RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised]:
    """Refresh your API token

     Renew/refresh the expiry of your API token

    Args:
        body (None):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: None,
) -> RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised | None:
    """Refresh your API token

     Renew/refresh the expiry of your API token

    Args:
        body (None):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshYourApiTokenLoginOk | RefreshYourApiTokenLoginUnauthorised
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
