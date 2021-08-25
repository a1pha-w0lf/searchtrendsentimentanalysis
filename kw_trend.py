from pytrends.request import TrendReq
import matplotlib.pyplot as plt
plt.style.use('seaborn-dark')

pytrends = TrendReq( timeout=(100,250))
#pytrends.top_charts(2021, hl='en-US', tz=360, geo='GLOBAL')
#kw_list = ["Blockchain"]
#pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
#print(pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))
#print(pytrends.trending_searches(pn='india'))
def getkw_trends(keyword):
    kw_list = [keyword]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    data = pytrends.interest_over_time()
    df = data.iloc[:,0]
    print(df)
    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    ax.plot(df, c="red")
    #plt.plot(df, c="red")
    ax.set_title(f"{keyword} search trend")
    ax.set_ylabel("Time period")
    plt.savefig("static/search.png")
    return kw_list

