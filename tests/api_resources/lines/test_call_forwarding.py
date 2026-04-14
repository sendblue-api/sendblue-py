# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types.lines import (
    CallForwardingDeleteResponse,
    CallForwardingUpdateResponse,
    CallForwardingRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCallForwarding:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SendblueAPI) -> None:
        call_forwarding = client.lines.call_forwarding.retrieve(
            "+12125550101",
        )
        assert_matches_type(CallForwardingRetrieveResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SendblueAPI) -> None:
        response = client.lines.call_forwarding.with_raw_response.retrieve(
            "+12125550101",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_forwarding = response.parse()
        assert_matches_type(CallForwardingRetrieveResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SendblueAPI) -> None:
        with client.lines.call_forwarding.with_streaming_response.retrieve(
            "+12125550101",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_forwarding = response.parse()
            assert_matches_type(CallForwardingRetrieveResponse, call_forwarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sendblue_number` but received ''"):
            client.lines.call_forwarding.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: SendblueAPI) -> None:
        call_forwarding = client.lines.call_forwarding.update(
            sendblue_number="+12125550101",
            forwarding_number="+16692138010",
        )
        assert_matches_type(CallForwardingUpdateResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: SendblueAPI) -> None:
        response = client.lines.call_forwarding.with_raw_response.update(
            sendblue_number="+12125550101",
            forwarding_number="+16692138010",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_forwarding = response.parse()
        assert_matches_type(CallForwardingUpdateResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: SendblueAPI) -> None:
        with client.lines.call_forwarding.with_streaming_response.update(
            sendblue_number="+12125550101",
            forwarding_number="+16692138010",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_forwarding = response.parse()
            assert_matches_type(CallForwardingUpdateResponse, call_forwarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sendblue_number` but received ''"):
            client.lines.call_forwarding.with_raw_response.update(
                sendblue_number="",
                forwarding_number="+16692138010",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: SendblueAPI) -> None:
        call_forwarding = client.lines.call_forwarding.delete(
            "+12125550101",
        )
        assert_matches_type(CallForwardingDeleteResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: SendblueAPI) -> None:
        response = client.lines.call_forwarding.with_raw_response.delete(
            "+12125550101",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_forwarding = response.parse()
        assert_matches_type(CallForwardingDeleteResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: SendblueAPI) -> None:
        with client.lines.call_forwarding.with_streaming_response.delete(
            "+12125550101",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_forwarding = response.parse()
            assert_matches_type(CallForwardingDeleteResponse, call_forwarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sendblue_number` but received ''"):
            client.lines.call_forwarding.with_raw_response.delete(
                "",
            )


class TestAsyncCallForwarding:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        call_forwarding = await async_client.lines.call_forwarding.retrieve(
            "+12125550101",
        )
        assert_matches_type(CallForwardingRetrieveResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.lines.call_forwarding.with_raw_response.retrieve(
            "+12125550101",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_forwarding = await response.parse()
        assert_matches_type(CallForwardingRetrieveResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.lines.call_forwarding.with_streaming_response.retrieve(
            "+12125550101",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_forwarding = await response.parse()
            assert_matches_type(CallForwardingRetrieveResponse, call_forwarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sendblue_number` but received ''"):
            await async_client.lines.call_forwarding.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSendblueAPI) -> None:
        call_forwarding = await async_client.lines.call_forwarding.update(
            sendblue_number="+12125550101",
            forwarding_number="+16692138010",
        )
        assert_matches_type(CallForwardingUpdateResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.lines.call_forwarding.with_raw_response.update(
            sendblue_number="+12125550101",
            forwarding_number="+16692138010",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_forwarding = await response.parse()
        assert_matches_type(CallForwardingUpdateResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.lines.call_forwarding.with_streaming_response.update(
            sendblue_number="+12125550101",
            forwarding_number="+16692138010",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_forwarding = await response.parse()
            assert_matches_type(CallForwardingUpdateResponse, call_forwarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sendblue_number` but received ''"):
            await async_client.lines.call_forwarding.with_raw_response.update(
                sendblue_number="",
                forwarding_number="+16692138010",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSendblueAPI) -> None:
        call_forwarding = await async_client.lines.call_forwarding.delete(
            "+12125550101",
        )
        assert_matches_type(CallForwardingDeleteResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.lines.call_forwarding.with_raw_response.delete(
            "+12125550101",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call_forwarding = await response.parse()
        assert_matches_type(CallForwardingDeleteResponse, call_forwarding, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.lines.call_forwarding.with_streaming_response.delete(
            "+12125550101",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call_forwarding = await response.parse()
            assert_matches_type(CallForwardingDeleteResponse, call_forwarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sendblue_number` but received ''"):
            await async_client.lines.call_forwarding.with_raw_response.delete(
                "",
            )
