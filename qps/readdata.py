import pandas as  pd
"""查询每个项目QPM最大的前10个方法"""
df = pd.DataFrame.from_csv("E:\Downloads\sm_dubbo_invoke (1).csv", header=None, parse_dates=False, encoding="UTF-8")
df.columns = ["invoke_date", "service_id", "service", "method_id", "method", "consumer", "provider", "type",
              "invoke_time", "invoke_time_minute", "success", "failure",
              "elapsed", "concurrent", "max_elapsed", "max_concurrent"]
df = df[df["type"] == 'provider']
dfsm = pd.DataFrame.from_csv("F:/service-to-app.csv", encoding="UTF-8", index_col=None)
dfa = df.merge(dfsm, on=["service"])


def cal(df, name):
    dfapp = df.groupby(["app"])
    for app, approw in dfapp:
        dfmethod = approw.groupby(["service", "method"])
        result = []
        for k, row in dfmethod:
            s = row.ix[row["success"].idxmax()]
            print(s)
            row1 = {}
            row1["app"] = app
            row1["service"] = k[0]
            row1["method"] = k[1]
            row1["qpm"] = s["success"]
            row1["qps"] = s["success"] / 60
            row1["max_concurrent"] = s["max_concurrent"]
            row1["avg_res_time"] = s["elapsed"] / s["success"]
            result.append(row1)
        df1 = pd.DataFrame.from_dict(result)
        dfr = df1.sort("qpm", ascending=False)[0:10]
        dfr.to_csv("F:/qps/{}.csv".format(app))


cal(dfa, None)
