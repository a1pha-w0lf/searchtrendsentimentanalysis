from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import mpld3

pytrends = TrendReq( timeout=(100,250))
#pytrends.top_charts(2021, hl='en-US', tz=360, geo='GLOBAL')
#kw_list = ["Blockchain"]
#pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
#print(pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False))
#print(pytrends.trending_searches(pn='india'))
def global_trends():
    date = 2020
    global_trends = (pytrends.top_charts(date, hl='en-US', tz=360, geo='GLOBAL'))
    kw = list( global_trends["title"])

    print(kw)

    pytrends.build_payload(kw[:5], cat=0, timeframe='today 3-m', geo='', gprop='')
    data = pytrends.interest_over_time()
    df = data.iloc[:,:4]
    plt.style.use('seaborn-dark')
    fig, axs = plt.subplots(2, 2, figsize = (35, 30))
    axs[0,0].plot(df[kw[0]], c='red')
    axs[0,0].set_title(kw[0])
    axs[0,1].plot(df[kw[1]], c='red')
    axs[0,1].set_title(kw[1])
    axs[1,0].plot(df[kw[2]],c='red')
    axs[1,0].set_title(kw[2])
    axs[1,1].plot(df[kw[3]],c='red')
    axs[1,1].set_title(kw[3])
    #plt.savefig('test.png',bbox_inches="tight")

    extent1 = axs[0,0].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    extent2 = axs[0,1].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    extent3 = axs[1,0].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    extent4 = axs[1,1].get_window_extent().transformed(fig.dpi_scale_trans.inverted())

    fig.savefig('static/subplot1.png',bbox_inches = extent1.expanded(1.1, 1.2))
    fig.savefig('static/subplot2.png',bbox_inches = extent2.expanded(1.1, 1.2))
    fig.savefig('static/subplot3.png',bbox_inches = extent3.expanded(1.1, 1.2))
    fig.savefig('static/subplot4.png',bbox_inches = extent4.expanded(1.1, 1.2))
    return kw[:4]
    #plt.show()
    '''html_str = mpld3.fig_to_html(fig)
    Html_file= open("index.html","w")
    Html_file.write(html_str)
    Html_file.close()'''

