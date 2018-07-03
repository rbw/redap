# -*- coding: utf-8 -*-

from redap.specs.utils import get_query_param

filter_param = get_query_param('filter', required=False)
nested_param = get_query_param('include_nested', data_type='boolean', default=False, required=False)
