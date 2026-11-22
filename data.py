# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Vaibhav Agarwal

import pandas_datareader.data as web

# It automatically handles headers and URLs in the background
df = web.DataReader("AAPL.US", "stooq")
print(df.head())
