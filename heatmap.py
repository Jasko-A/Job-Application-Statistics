import numpy as np
import pandas as pd
import calmap
 

all_days = pd.date_range('1/15/2014', periods=700, freq='D')
days = np.random.choice(all_days, 500)
events = pd.Series(np.random.randn(len(days)), index=days)



calmap.calendarplot(events)