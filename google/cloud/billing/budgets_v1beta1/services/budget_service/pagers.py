# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Any, AsyncIterable, Awaitable, Callable, Iterable, Sequence, Tuple

from google.cloud.billing.budgets_v1beta1.types import budget_model
from google.cloud.billing.budgets_v1beta1.types import budget_service


class ListBudgetsPager:
    """A pager for iterating through ``list_budgets`` requests.

    This class thinly wraps an initial
    :class:`~.budget_service.ListBudgetsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``budgets`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListBudgets`` requests and continue to iterate
    through the ``budgets`` field on the
    corresponding responses.

    All the usual :class:`~.budget_service.ListBudgetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., budget_service.ListBudgetsResponse],
            request: budget_service.ListBudgetsRequest,
            response: budget_service.ListBudgetsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.budget_service.ListBudgetsRequest`):
                The initial request object.
            response (:class:`~.budget_service.ListBudgetsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = budget_service.ListBudgetsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[budget_service.ListBudgetsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[budget_model.Budget]:
        for page in self.pages:
            yield from page.budgets

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListBudgetsAsyncPager:
    """A pager for iterating through ``list_budgets`` requests.

    This class thinly wraps an initial
    :class:`~.budget_service.ListBudgetsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``budgets`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListBudgets`` requests and continue to iterate
    through the ``budgets`` field on the
    corresponding responses.

    All the usual :class:`~.budget_service.ListBudgetsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[budget_service.ListBudgetsResponse]],
            request: budget_service.ListBudgetsRequest,
            response: budget_service.ListBudgetsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.budget_service.ListBudgetsRequest`):
                The initial request object.
            response (:class:`~.budget_service.ListBudgetsResponse`):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = budget_service.ListBudgetsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[budget_service.ListBudgetsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[budget_model.Budget]:
        async def async_generator():
            async for page in self.pages:
                for response in page.budgets:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
