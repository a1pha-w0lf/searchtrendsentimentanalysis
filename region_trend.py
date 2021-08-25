from pytrends.request import TrendReq
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='en-US',timeout=(100,250))

pytrends.build_payload(kw_list=[''],
                       cat=0,
                       timeframe='today 3-m',
                       geo='',
                       gprop='')

def trending_searches(country):
    data = pytrends.trending_searches(pn=country)
    kw = list(data.iloc[:4,0])
    print(kw)
    pytrends.build_payload(kw_list = kw,
                        cat=0,
                        timeframe='today 3-m',
                        geo='',
                        gprop='')
    data2 = pytrends.interest_over_time()
    df = data2.iloc[:,:4]
    print(df)
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

    fig.savefig('static/subplotreg1.png',bbox_inches = extent1.expanded(1.1, 1.2))
    fig.savefig('static/subplotreg2.png',bbox_inches = extent2.expanded(1.1, 1.2))
    fig.savefig('static/subplotreg3.png',bbox_inches = extent3.expanded(1.1, 1.2))
    fig.savefig('static/subplotreg4.png',bbox_inches = extent4.expanded(1.1, 1.2))
    return kw[:4]