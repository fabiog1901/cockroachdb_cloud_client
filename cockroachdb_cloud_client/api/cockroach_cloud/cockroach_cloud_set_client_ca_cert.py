from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.client_ca_cert_info import ClientCACertInfo
from ...models.cockroach_cloud_set_client_ca_cert_set_client_ca_cert_request import (
    CockroachCloudSetClientCACertSetClientCACertRequest,
)
from ...types import Response


def _get_kwargs(
    cluster_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetClientCACertSetClientCACertRequest,
) -> Dict[str, Any]:
    url = "{}/api/v1/clusters/{cluster_id}/client-ca-cert".format(client.base_url, cluster_id=cluster_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ClientCACertInfo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ClientCACertInfo.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, response.json())
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, response.json())
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, response.json())
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, response.json())
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, response.json())
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ClientCACertInfo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    cluster_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetClientCACertSetClientCACertRequest,
) -> Response[Union[Any, ClientCACertInfo]]:
    """Set Client CA Cert for a cluster

    Args:
        cluster_id (str):
        json_body (CockroachCloudSetClientCACertSetClientCACertRequest):  Example:
            {'x509_pem_cert': '-----BEGIN CERTIFICATE-----...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClientCACertInfo]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    cluster_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetClientCACertSetClientCACertRequest,
) -> Optional[Union[Any, ClientCACertInfo]]:
    """Set Client CA Cert for a cluster

    Args:
        cluster_id (str):
        json_body (CockroachCloudSetClientCACertSetClientCACertRequest):  Example:
            {'x509_pem_cert': '-----BEGIN CERTIFICATE-----...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClientCACertInfo]
    """

    return sync_detailed(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    cluster_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetClientCACertSetClientCACertRequest,
) -> Response[Union[Any, ClientCACertInfo]]:
    """Set Client CA Cert for a cluster

    Args:
        cluster_id (str):
        json_body (CockroachCloudSetClientCACertSetClientCACertRequest):  Example:
            {'x509_pem_cert': '-----BEGIN CERTIFICATE-----...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ClientCACertInfo]]
    """

    kwargs = _get_kwargs(
        cluster_id=cluster_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    cluster_id: str,
    *,
    client: Client,
    json_body: CockroachCloudSetClientCACertSetClientCACertRequest,
) -> Optional[Union[Any, ClientCACertInfo]]:
    """Set Client CA Cert for a cluster

    Args:
        cluster_id (str):
        json_body (CockroachCloudSetClientCACertSetClientCACertRequest):  Example:
            {'x509_pem_cert': '-----BEGIN CERTIFICATE-----...'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ClientCACertInfo]
    """

    return (
        await asyncio_detailed(
            cluster_id=cluster_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
