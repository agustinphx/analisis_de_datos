import quantstats as qs

qs.extend_pandas()

stock = qs.utils.download_returns('NVDA')

print(stock.sharpe())

stock.plot_earnings(savefig = 'NVDA', start_balance = 1000)

qs.reports.html(stock, 'SPY', title = "NVDA", output ='G:\2. Programming\Back-end\Python Análisis de Datos  ITBA\Clase 2\Análisis de Empresas')
