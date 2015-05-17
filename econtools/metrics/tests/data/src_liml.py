import pandas as pd
import numpy as np

class regout(object):

	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)



stat_names=['coeff', 'se', 't', 'p>t', 'CI_low', 'CI_high']
var_names=['mpg', 'length', ]
liml_std = regout(
summary=pd.DataFrame(np.array([
[-21665.92164343596,
367584.231271271,
-.0589413794180058,
.9533247737527548,
-767161.2959397107,
723829.4526528388,
],
[-3588.324735313654,
62319.60685635515,
-.057579386589916,
.9544020865193998,
-129978.3455441476,
122801.6960735203,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[135118167079.2912,
22905018578.34641,
],
[22905018578.34641,
3883733398.730668,
],
]),
columns=var_names,
index=var_names),
N=51,
r2=np.nan,
r2_a=np.nan,
mss=-184299456431.2585,
tss=np.nan,
rss=184630258553.7683,
kappa=1.002222405278871,
F=.0056521101472562,
pF=.9943647151885066,
)
liml_robust = regout(
summary=pd.DataFrame(np.array([
[-21665.92164343596,
1271148.79627001,
-.01704436310447,
.9864953391734057,
-2599675.169712163,
2556343.326425291,
],
[-3588.324735313654,
215396.2186709901,
-.0166591816581269,
.9868004983913743,
-440432.1036558217,
433255.4541851944,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[1615819262258.695,
273799247464.0641,
],
[273799247464.0641,
46395531017.76098,
],
]),
columns=var_names,
index=var_names),
N=51,
r2=np.nan,
r2_a=np.nan,
mss=-184299456431.2585,
tss=np.nan,
rss=184630258553.7683,
kappa=1.002222405278871,
F=.0074135369767507,
pF=.9926153904958579,
)
liml_cluster = regout(
summary=pd.DataFrame(np.array([
[-21665.92164343596,
1505219.596498809,
-.0143938609979777,
.9887523005030139,
-3301257.689961569,
3257925.846674697,
],
[-3588.324735313654,
255283.2049757428,
-.0140562507261479,
.9890160980143785,
-559802.6469350308,
552625.9974644035,
],
]),
columns=stat_names,
index=var_names),
vce=pd.DataFrame(np.array([
[2265686033684.036,
384254999215.6299,
],
[384254999215.6299,
65169514742.68712,
],
]),
columns=var_names,
index=var_names),
N=51,
r2=np.nan,
r2_a=np.nan,
mss=-184299456431.2585,
tss=np.nan,
rss=184630258553.7683,
kappa=1.002222405278871,
F=.0048960694386651,
pF=.9951178835614971,
)