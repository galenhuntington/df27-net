#! /usr/bin/python3

#  Sample network for identifying Z196+ within DF27+.


import re
import math

print("Please enter 111 STR values:")
raw = input("? ")
strs = [int(x) for x in re.split('\D+', raw) if x]

if len(strs) != 111:
    print(f"Invalid input; you gave me {len(strs)} values.")
    exit(1)

weights = [
    [
        [0.30592436,0.7197436,0.36593896,9.157753e-3,-9.9540595e-3,-0.17010795,-0.32330605,0.59364665,-7.6954395e-2,-0.2371084,-0.32744175,-0.20351562,4.550816e-2,-6.0263157e-2,-1.21003e-2,-2.2960869e-3,8.755396e-2,0.2044781,0.18852374,-8.937628e-2,-6.545602e-2,-5.0937854e-2,-9.54472e-2,-0.11099251,-0.11455895,4.2158354e-2,-9.793422e-2,-0.30786288,5.456128e-2,3.5558417e-2,-6.495782e-2,-0.35957837,0.1387454,-0.16360456,-0.11050675,-4.374402e-2,0.1915498,0.13699058,-0.18173751,0.12397543,0.6197487,-0.37159148,-9.770524e-2,-7.171043e-3,-0.30218375,-0.154844,0.21740226,0.25082865,-5.4209685e-4,0.10891324,-1.5342386e-2,0.19872949,-0.44343957,0.17663094,-7.444317e-2,0.79550093,0.11295305,3.7411023e-2,0.20133412,-0.225497,-0.18221961,-0.37181807,-0.19093327,-0.32551202,-6.381936e-2,-4.5961473e-2,0.23486266,3.835625e-2,3.2526284e-2,-0.14450243,0.43382072,-0.33988965,-0.34792385,-1.8793957e-2,9.739287e-2,0.12595971,-0.123801574,-0.14445302,-0.26422572,-0.25776714,-0.19255824,-6.906671e-2,-0.17002991,0.13741745,0.157491,0.31158322,0.11012073,-4.9047746e-2,-0.26145452,-0.16848245,1.97484e-2,-2.0372096e-2,0.6274587,6.293453e-2,-7.3800206e-2,-2.1703001e-2,-0.123209134,0.29778102,-0.3731908,-5.9515346e-2,-0.25471228,-0.15442482,4.832124e-3,0.13594086,0.34163827,-0.11667886,0.5946064,2.2508543e-2,0.16716215,-0.1025481,-2.329339e-2],
        [0.23167887,0.5134114,0.5741538,-0.3010648,-8.2833216e-2,-0.210392,-0.43064585,0.7875695,-0.3811015,-0.17967018,-0.6244916,-0.1827226,3.0204792e-2,2.654612e-2,4.470492e-2,-0.17502701,7.3889166e-2,0.15723279,0.15598163,-0.12550369,-0.10455544,0.25342253,4.1582294e-2,4.1187372e-2,2.9570144e-2,0.11689262,0.19944687,-0.12765446,-0.11348303,-0.10977106,0.28578898,-5.8608543e-2,0.12569657,-0.17410266,-0.1403449,-6.2336167e-3,0.34789014,9.93375e-2,-0.27093503,-6.7828834e-2,0.6056137,-0.6310702,-1.43508315e-2,-9.655355e-2,-0.34042135,-0.18819985,0.4474214,0.32926765,-2.5801968e-2,2.0387978e-3,4.126039e-2,0.30039197,-0.3707919,0.11389669,-0.11169366,0.82307065,-0.111220166,0.17186996,-0.26314527,3.447665e-2,-3.3951454e-2,-0.48501268,-0.30586326,-0.2285446,0.1692879,-7.2781265e-2,-2.0455237e-2,-0.27291024,-0.18079856,-0.26886815,0.21489708,-0.36333007,-0.37468606,-0.13383253,0.4452854,0.47132617,-0.22956479,-0.17580353,6.1588686e-2,-9.095716e-2,-0.13587147,-0.22265387,1.5268261e-2,5.257237e-2,8.106823e-2,0.29169804,2.3803148e-2,-0.12848337,-0.14137137,-7.7842236e-2,-8.992506e-3,-0.32637632,0.6434387,9.3409814e-2,-0.10656552,-7.4647546e-2,-8.313107e-2,6.1743718e-2,-0.15004648,0.2125577,8.358224e-2,-0.10181886,-0.26307797,9.346176e-2,0.33190742,0.15879135,0.5372593,-0.18860076,0.1432286,-0.30112284,-3.2343768e-2],
        [0.3114735,0.42286396,0.10968268,-0.34345418,-1.9926769e-3,0.375713,-0.17244014,0.92755806,0.13681856,-0.16534841,-2.1715972e-3,-0.19791858,0.1510044,2.6400577e-2,0.16323356,0.28782707,-0.15058942,0.17370017,0.38254112,-4.0478054e-2,-9.863157e-3,-0.76826775,-6.0161382e-2,0.12535505,1.2792645e-2,-0.19224489,0.43155646,-0.3363771,0.7171494,0.2709083,-0.60965466,-0.2804613,0.19195203,-0.4905613,-5.2609675e-2,-0.10335173,0.4158353,4.864252e-2,-0.15285946,0.5460302,0.3112612,9.56397e-2,-0.28072482,1.6038494e-2,-0.8033242,-0.13316992,-0.2872898,-0.11582218,3.6108285e-2,0.29517478,-5.4159224e-2,-0.2969217,-0.16839445,0.23181698,-1.4101858e-2,0.22460058,0.5886645,0.33464995,0.25859424,-0.79492444,-7.223203e-2,-0.3870054,-0.35708284,-7.8667976e-2,2.5502319e-2,-3.2927166e-3,0.5006598,1.8196974e-2,-6.636074e-2,-0.12087139,0.4565591,-0.34080642,-0.1331788,0.12943396,3.541199e-2,-0.10229868,1.4701454e-2,-0.14773302,-0.14549372,-3.8415982e-4,-0.1860157,0.22032957,-0.24198909,-0.17007104,0.21244428,0.36406773,8.244049e-2,0.1288282,-5.603056e-2,-6.7853555e-2,3.0548502e-2,-0.16052073,0.38806516,-4.7775358e-2,-7.1249254e-2,-4.598806e-2,-0.18416819,-0.18968102,-0.708676,-0.57519644,-0.15034764,-0.5071298,0.1634759,0.2461371,0.53351265,0.27200466,0.62675935,0.2773705,-0.66503716,0.18819413,4.9249712e-2],
        [0.35164186,0.7293993,0.29214418,-1.9261895e-3,5.5126317e-2,-0.3247964,-0.24337557,0.47060174,6.920796e-2,-0.24143651,-0.7297617,-0.31113526,-1.4170682e-2,0.39366803,0.36712867,-6.301193e-2,9.901611e-2,0.33332473,0.16555959,-0.124080285,-3.5513096e-2,-5.0154e-2,-0.39574045,-0.39137504,-0.19748755,-0.22303943,-0.38210312,-0.36168322,-6.1850857e-2,8.6600475e-2,0.16645658,-0.61726457,0.14828062,8.893042e-2,-0.1610177,8.871061e-2,7.151383e-2,0.20032656,-0.2725937,0.16381077,0.6796182,-0.3097388,-0.12593481,0.23579574,-0.7370025,-0.22832885,0.44913715,0.284244,5.776477e-3,0.12174983,5.8220424e-2,-0.20263425,-0.38389787,0.2266537,-4.5366384e-2,1.0391052,0.50067604,-0.17942385,-0.1426878,-0.15678558,-0.3881951,-0.43380338,-4.5673512e-2,-0.52227545,7.571902e-2,-5.534063e-2,0.5803208,1.387812e-2,2.3999494e-2,-0.24745154,0.5939892,-0.16084187,-0.16680183,-2.4570141e-2,-0.22650173,9.666444e-2,-0.16969576,-6.9258586e-2,-0.22791834,-0.4629046,-0.2787153,0.26436025,-0.17520078,0.20795126,0.23986034,0.36132532,0.17740229,-0.10419907,-0.8450205,-0.28341445,-1.9857418e-2,-3.809116e-2,0.7224925,0.1691182,-7.690339e-2,3.5600863e-2,5.278821e-2,0.64565194,-0.71111155,-9.9956565e-2,-0.62574065,-0.5712824,0.26096022,0.30778223,0.4681557,-0.13356012,1.0729578,-0.11375368,0.18137644,-0.11093328,-8.749036e-2],
        [0.3052775,0.47496742,0.68665284,-0.34847397,-9.464821e-2,-0.25181678,-0.3390799,0.4825262,-0.41815433,-0.13604848,-0.40099305,-0.11823418,8.1998885e-2,-3.0969728e-2,7.643167e-2,2.9341314e-2,0.23535924,0.1433504,0.17431982,-0.15619728,-0.105784975,0.10885898,0.6031998,0.15404883,7.035369e-2,0.18211795,7.686944e-2,-0.26356518,-0.3021842,7.952028e-3,0.3153615,-7.6376796e-2,0.13104077,-0.2992089,-0.11095716,-7.8098997e-3,0.48722178,2.2965645e-2,-0.26748404,0.10192998,0.59133697,-0.5018693,2.242727e-3,-0.4312055,7.863656e-2,-5.553438e-2,0.5598408,0.7085825,-1.9786993e-2,0.16638781,3.1169573e-2,0.665357,-0.3372228,0.32169396,-0.10805462,0.8141018,-6.892181e-2,0.5631034,0.20762932,-0.10222982,0.24849136,-0.3282887,-0.5402798,-2.3355104e-2,0.11041417,8.534132e-2,-0.30078253,-0.209531,-0.4462119,-0.36665285,-5.0845534e-2,-0.2888242,-0.3585394,-0.32964978,0.17073496,0.5513197,-0.24650571,-0.3973337,0.2430908,-0.18099716,-0.12347831,-0.85262716,5.2734464e-2,0.14533454,3.373824e-2,0.24148104,-2.8323269e-2,-0.14045635,8.099823e-2,-0.13605964,-3.4122407e-3,-4.7504287e-2,0.5450813,8.8309094e-2,-8.049222e-2,-4.2122032e-2,-0.14710912,-3.3617992e-2,-0.3938073,6.9717415e-2,-5.155469e-2,-7.765045e-2,-0.32275513,-2.628236e-2,0.32582834,4.6942614e-2,0.3684902,-0.276139,0.36303505,-0.2904231,3.9617866e-2],
        [0.8301054,0.7704849,0.5467638,-0.15082833,0.28982717,5.5152692e-2,7.73324e-2,0.19798228,0.4057165,-0.36276263,0.16382164,-1.0953576e-3,0.20949128,-0.41542712,-0.28907955,0.46753988,0.12081609,0.13614738,0.30478394,6.55983e-2,-8.80587e-2,-0.14541899,9.94238e-2,0.4018891,0.44327584,0.43509388,-0.21945906,0.14870092,0.17185478,0.12425204,-1.5114479,-0.10809553,0.33579654,-0.5262719,1.6009074e-2,-3.65407e-2,1.2798706e-2,0.3171169,7.162468e-2,-7.980237e-2,0.28345084,-0.9573005,-7.0203826e-2,-0.30356383,-4.6655327e-2,3.7069883e-2,0.2396928,2.131502e-2,4.6132665e-2,-0.32264522,-0.8480051,0.45983967,-0.55432093,-1.7626047e-2,-0.17325214,0.6126346,-4.471897e-2,-0.18231642,0.17519478,-0.96035576,-3.1160742e-2,-0.2722703,3.270786e-2,-7.568328e-2,-0.29886258,-4.811986e-2,-0.3887549,-0.30053207,-0.48015046,-8.208624e-2,0.18097168,-0.6017474,-0.33507007,0.32380196,-0.15384261,-0.33963084,0.2780328,0.25180966,-0.4608314,-0.4086186,-0.20648167,-0.4636212,-0.25973132,0.12629646,-0.116300166,0.47259554,6.8164214e-2,0.31403702,0.21347018,-0.14552197,0.30442035,-3.5498817e-3,0.9183055,0.2874987,-0.26664466,3.361744e-2,-0.27664772,-0.14880157,0.6229927,-0.1274714,-0.12493261,6.0280044e-2,7.268721e-3,0.17405912,0.56717056,-0.5692783,4.584772e-2,0.6366497,-3.2282196e-2,0.11406441,0.3162122],
        [0.36248913,0.609237,0.2349087,-0.22428441,4.6002273e-2,-8.409249e-2,-0.116564736,0.3064957,0.19797322,-8.292126e-2,-0.11133982,-9.165462e-2,8.07512e-2,-0.1442419,5.546706e-3,0.22968276,6.288194e-2,0.10695948,0.1334618,4.7193738e-4,-4.5398436e-2,-0.29325032,-1.4780504e-2,0.11031749,0.1209891,0.122231744,1.5024124e-2,-0.1327701,0.1287705,2.9403782e-2,-0.7876315,4.584401e-3,0.16479859,-0.20866612,-2.7894977e-2,-1.2506197e-2,3.306215e-2,0.110460855,-7.154416e-2,3.005886e-2,0.29840922,-0.31283498,-8.1483305e-2,-5.9346896e-2,-8.78895e-2,1.5330605e-2,0.23841973,0.22060928,1.658025e-2,-2.0254385e-2,-0.18585737,0.11525947,-0.5263553,0.115690745,-6.549196e-2,0.7323503,8.830247e-2,4.781865e-2,0.12518811,-0.5964312,-1.9144498e-2,-0.22086933,-0.23509066,-0.1139349,-9.6577026e-2,-4.148657e-2,-0.14611249,-6.557767e-2,-0.1465405,2.2880757e-2,0.34394783,-0.29107305,-0.23494354,-0.11796292,7.180561e-2,-0.10434737,3.3776513e-3,3.7025139e-3,-3.641071e-2,-0.25368413,-0.14798643,-0.16893446,-0.18257445,0.127215,8.9156374e-2,0.3301671,2.7680611e-2,2.2705477e-2,6.609867e-2,-0.14996113,7.5269185e-2,-2.8794993e-2,0.5242618,0.13715655,-0.12613277,-3.3005044e-2,-0.20874497,0.23945327,0.25397983,-4.475458e-2,-0.17856638,-0.100116834,-8.549786e-2,0.14374606,0.2670794,-6.864397e-2,0.12859975,0.24205685,-0.19505957,-1.8875131e-2,0.14237896],
        [-7.629417e-2,0.67536336,6.0981352e-2,-0.46898717,1.4522033e-2,-7.621978e-2,0.20685141,0.96865195,-1.8603386e-2,-1.8163402e-2,0.19516888,-0.16428739,0.15012664,-4.833574e-2,-3.2701053e-2,0.3985863,-0.17730696,0.1305773,0.17341837,-5.453704e-2,-8.39545e-2,1.8156718e-2,0.26371562,9.484205e-2,-6.0600597e-2,5.9393983e-2,-0.24863108,-0.40825504,0.63629675,0.5883266,-0.6598436,-9.125863e-2,0.2277286,-0.7172338,-2.390616e-2,-0.20756853,-0.41508618,0.31335664,-0.2746849,0.3346005,0.64059126,-0.19289264,-0.2988332,-9.065209e-2,-0.21301183,-0.325733,-1.0062294,-0.24733122,3.6997746e-3,-0.42427897,-0.23029129,1.5004206,-0.14755113,0.14222798,-8.464334e-2,-0.5442905,0.30836266,5.6232936e-3,1.0834712,-7.578413e-2,-0.15374377,-0.4619246,-0.61257344,-5.649001e-2,-0.3204134,-8.216782e-2,0.43528947,0.1760067,0.24715412,0.17239338,0.5803641,-0.5039138,-0.41696137,0.5964561,0.1763082,2.6741927e-2,0.19125482,2.495284e-2,-1.0256312,-4.728572e-2,-0.27767915,0.2656413,-0.24424875,0.12624924,0.18664822,0.2981267,7.95212e-2,0.21180454,-0.18351336,-6.855164e-2,3.962794e-2,-0.5063679,0.5720713,-1.1621046e-2,-0.12892832,-0.11404904,3.0535093e-2,-0.19396897,9.722965e-2,0.25991493,8.914068e-2,0.11647054,-0.12600335,0.13356195,0.40716234,-5.9115313e-2,0.15699486,0.18935362,-0.4987515,-1.9443464e-2,9.375928e-4],
        [6.6831365e-2,0.17257136,-0.2626405,5.473881e-2,-7.169076e-2,-0.121652864,-8.7138996e-2,0.27667165,0.6555272,-0.13309231,-0.11600176,0.4605152,7.687976e-2,0.50548273,-0.48878002,-0.43086648,-0.31802776,0.28415418,7.227133e-2,-9.069903e-2,-2.5840392e-2,0.102964714,0.40034437,-0.28183928,-0.32781082,1.3742003,0.1314043,0.10891266,-3.7525445e-2,0.38551527,0.32297087,8.472569e-2,0.14744963,-0.2849995,-0.12326242,-2.5229018e-2,-0.75040483,-0.28937617,-0.17722459,-3.41221e-2,0.11852668,-0.22577986,-7.353926e-2,6.245441e-2,-0.22844717,-0.14782059,-0.8721938,-0.11671106,-4.7985878e-4,0.26108637,0.3569133,0.15215187,-0.14611211,5.4236073e-2,-7.5360574e-2,-4.6106535e-3,0.11006961,-5.2304965e-2,-0.34463745,0.6233307,-8.909238e-2,-0.55668014,-3.0360332e-2,-6.572382e-2,-0.15819208,-0.25409606,0.22058026,-0.72088236,0.49241924,4.353729e-2,0.33998665,0.23397946,3.362409e-2,-0.8203354,5.288892e-2,0.31998137,-0.4100546,-0.12306102,0.30209416,0.17561176,-0.17398056,7.774595e-2,-0.18772307,6.0155313e-2,9.812628e-2,0.14549164,0.32074487,7.4614916e-5,-0.24323192,0.26532635,1.2324964e-2,-0.3418515,0.60974985,4.8500128e-2,0.26139796,-0.1970448,-0.24067064,0.54917693,-0.47835928,-0.16291389,0.511037,0.5232903,-4.4344258e-2,8.158992e-2,0.1825567,-0.19307981,-0.56923664,9.846284e-3,0.24406484,-0.2784818,-9.236431e-3],
        [0.67436814,0.5231984,-9.795559e-2,-0.17874978,0.3637959,-0.36442846,0.49800047,-0.41342664,0.3912266,0.14059123,-0.2960312,4.6763014e-2,0.4795784,6.1089702e-2,7.532328e-2,1.1221861,-2.2415068e-2,0.10143056,-7.675814e-3,6.770557e-2,3.3997353e-2,-1.3781526,-0.2757299,0.101615585,0.68021494,6.0403585e-3,-0.22643301,-0.16644315,0.12902157,-0.8882948,-3.128365,0.47343984,0.37023023,-4.4686295e-2,-4.233396e-3,1.6048871e-2,0.14800097,0.22506568,-7.330147e-3,0.19055216,-0.7987371,-6.0496677e-2,-0.61332095,-0.13561574,0.39798373,0.12061348,0.30141816,3.7405335e-3,7.555367e-2,-0.37237284,-9.373223e-2,-0.10671522,-0.176078,-1.4401008e-2,-9.972141e-4,0.47650877,0.23394021,1.6470535e-2,-5.800257e-2,-2.8476057,2.8168191e-3,-5.6854885e-2,-0.86895436,-0.14092284,0.3210556,-3.5569943e-2,4.559181e-2,0.10467708,-0.12656169,0.37419444,0.35460576,0.8328826,0.29074976,-0.43694672,0.78070134,-0.16006438,0.39369062,0.8417886,9.3484975e-2,-0.9270544,-0.29505485,0.317075,-1.0034802,2.8419483e-2,0.16663039,0.7432432,-0.12174456,0.11398914,0.40356803,-0.8497714,0.2376209,0.2674838,0.691608,0.2202714,-0.30436188,9.84275e-3,-0.585601,4.9417697e-2,0.36221534,0.24140307,2.6647488e-2,0.55172914,-0.12536277,0.70271313,0.14839093,-4.6630017e-2,-0.50176156,0.50718606,-1.9455643,0.6115078,0.60049033],
        [9.186073e-2,0.4035442,0.4836331,-0.42361942,-8.220755e-2,-0.30266088,-0.16447255,0.688336,-0.28171843,-1.8707562e-2,-0.352853,-0.16726448,9.293527e-2,0.10221596,-2.0678643e-2,6.603448e-2,0.20258895,0.17046899,0.16686024,-0.1449126,-7.60322e-2,-5.3551298e-2,0.37329218,2.0504618e-2,0.19673142,-2.409437e-2,0.3150696,-0.23877919,-0.27655327,0.32615358,0.30290413,-0.12360958,0.15066126,-0.46504545,-9.4616234e-2,-6.2460885e-3,0.31844136,0.12103621,-0.3659557,0.27097654,0.46915555,-0.3661217,-3.435994e-2,-0.34814024,-4.3914184e-2,0.19519845,0.35651013,0.46638313,-7.5908788e-3,0.26346946,0.17886962,0.8065692,-0.19593373,0.38040158,-7.974962e-2,0.52250266,4.308352e-2,0.36685133,0.4570191,-0.16288254,5.4168086e-2,-0.48581806,-0.37495762,-0.13157545,9.590799e-2,0.1361818,-0.345427,-0.26239854,-0.4972054,-0.32160118,1.1714606e-2,-0.25147426,-0.2615568,-0.3226971,0.1331651,0.42063656,-0.20646068,-0.32262123,0.34359908,-7.491244e-2,-0.13150862,-0.58495986,-5.0284058e-2,7.765319e-2,-1.3156367e-2,0.2277523,1.5518673e-2,-0.13026455,-3.994522e-2,-3.6996048e-2,-2.208282e-3,-4.940369e-2,0.53507,7.128951e-2,-6.683597e-2,-8.597778e-2,-1.09980535e-2,-3.8250078e-2,-0.7101884,0.10449525,0.12001596,-5.5373423e-2,-0.18500696,5.7726413e-2,0.34794372,0.12529635,0.2572504,-0.35443413,0.1855503,-0.27313805,6.9929264e-2],
        [3.9931975e-2,0.6148962,0.5163989,-0.38981587,-0.12024359,-0.23080483,-0.14484829,0.5800446,-0.3901567,0.10479417,-0.20832396,-1.7059927e-3,7.755828e-2,6.561144e-2,7.745224e-3,0.10889397,0.29855236,0.113734744,0.15546319,-0.122143306,-0.14799826,0.12982602,0.65197945,0.20454827,0.11153754,0.2248497,0.11525192,-0.32754582,-0.32785904,0.33784884,0.31215712,-8.084395e-2,0.13347681,-0.5239001,-0.1115877,-3.1237636e-2,0.18674314,8.4395014e-2,-0.34535432,0.1564348,0.5319696,-0.4292267,4.7586873e-2,-0.49740046,7.748446e-2,3.0022543e-2,3.7802815e-2,0.34101585,-2.4890218e-2,0.14110485,5.5553667e-2,1.3148911,-0.30135992,0.23667875,-0.13432372,0.579739,-3.1224176e-2,0.3724454,0.6986667,-2.5950303e-2,9.5027916e-2,-0.3756742,-0.45974192,-0.16507612,-9.826739e-2,5.571726e-2,-0.481997,-0.34015626,-0.2727825,-0.16337365,-0.16616991,-0.37104067,-0.42328095,-0.4225832,0.24656923,0.35617074,-0.17946763,-0.19527256,4.3713525e-2,-0.12994216,-0.12542483,-0.7372786,-1.7231043e-2,0.12201301,-8.735104e-2,0.20757647,-2.0344164e-2,-0.1252222,-2.6761249e-2,-8.912969e-2,2.6050348e-2,-3.30791e-3,0.5224763,6.8408474e-2,-9.99866e-2,-8.872928e-2,4.7523867e-2,-8.7498225e-2,-0.28719273,0.3032887,0.13100128,0.2243222,-0.4241921,-3.8859848e-2,0.21772638,-1.418647e-2,-1.948764e-3,-0.40701437,0.35830155,-0.42892575,-4.9819564e-3],
        [0.31673467,0.7626212,0.37181407,-0.28799903,4.5485236e-3,-0.116797104,-5.245177e-2,0.4634703,4.9641993e-2,-3.2193903e-2,-0.1800501,-0.112966225,7.558396e-2,-0.24237904,5.2632384e-2,0.14721705,9.192725e-2,0.12736624,0.19787543,-3.9358966e-2,-9.8671705e-2,-5.3310584e-2,-4.2575054e-2,0.26398724,0.11888105,0.14763223,-2.997693e-2,-0.13095382,6.907876e-2,0.123064384,-0.46033335,-0.14931953,0.16104804,-0.23709972,-5.167339e-2,-3.0891934e-2,0.13921091,0.2070132,-0.18811665,-2.8080616e-2,0.5363208,-0.5690806,-6.7670636e-2,-0.12957945,-0.11123693,8.8862807e-4,0.30287522,0.144552,3.3346233e-3,8.982234e-2,-0.16072255,0.46139345,-0.546702,0.12137332,-9.3213186e-2,0.7499581,1.8007735e-2,-6.013776e-3,0.29203138,-0.35276586,-8.02076e-2,-0.26144034,-0.2525056,-0.20875935,-0.14509673,-2.0849194e-2,-8.0877766e-2,-0.12441982,-0.11096789,-1.7535318e-2,0.276552,-0.414222,-0.33639812,-3.266129e-2,7.904677e-2,-7.643043e-2,-4.426659e-2,3.0622298e-2,-0.24484093,-0.25432637,-0.15693076,-0.33894375,-0.16578443,0.15874673,3.670345e-2,0.344868,0.101167165,1.937029e-2,-7.7436954e-2,-0.14726463,7.637368e-2,-1.319066e-2,0.6491584,0.15007986,-0.13309833,-4.3603558e-2,-0.13593222,-2.1880796e-2,0.15335742,0.14473966,-0.18744323,-3.054588e-2,-0.19918248,0.11336808,0.29912904,-7.552113e-2,0.25863397,7.245126e-2,5.3734787e-2,-0.15155508,0.14325969],
        [0.26072493,1.3320187,0.3513319,-0.30859786,0.29952434,-0.18123159,-0.43503112,0.3134011,0.57642126,0.2049491,-0.1348406,-0.3189524,-5.3306144e-2,-0.31931216,0.21905597,-0.4365825,7.806246e-2,-4.138769e-2,-4.9262684e-2,1.9159503e-2,-0.19916666,-0.122469865,-1.2787578e-2,-0.35344937,0.38828143,1.1477358,-0.32710767,5.200093e-2,0.12339307,-0.40890154,-1.0538102,0.2066836,0.23914368,-0.1552039,-0.25405172,-0.43306,0.1282971,0.16922173,5.4545294e-2,-1.3831015,-0.32928082,-0.39282623,2.3776364e-2,-0.34878343,0.3910956,-0.41822615,4.8901677e-2,0.15452938,-3.983998e-2,-0.12102047,-0.4940555,-0.17384428,-1.1802964,-5.9447188e-2,-0.2239526,2.3078995,-0.50985104,9.892673e-2,0.14485954,-0.21923712,-0.46602568,0.2792412,-0.7132832,-0.59141934,-0.17894052,0.10974042,-3.66673e-3,-0.53798354,0.3383461,0.67448294,0.8777701,-0.74053174,-0.25245684,-5.6627683e-2,0.11182839,-3.2818452e-3,2.6567768e-2,0.25022265,-0.17783801,-0.29395887,-0.31897223,0.65876,-0.4942481,0.55146354,0.17389789,0.53264314,-0.27290645,-0.14890271,0.4703653,-0.45259118,2.6167503e-2,-0.5393301,0.8473873,0.21226695,-0.43295884,-0.14018136,-0.98885137,1.3714917,0.47129083,3.0474145e-2,-0.41819674,0.6144956,-0.51767117,-6.8480514e-2,-1.6246289e-3,-0.1134732,1.5290801e-3,0.394596,-0.18151872,-0.27180332,0.6672646],
        ],
    [
        [-3.3098836,-3.5686257,-6.3070188,-6.406016,-4.2893066,-5.8164115,-1.6443344,-6.6098847,-5.351782,-10.69901,-3.569504,-6.4305625,-1.8812188,-6.1901336],
        [-1.7116499,-5.309725,-9.1307955,-10.085089,-7.707027,-9.23654,4.768501,-8.490231,-9.561909,-12.677641,-4.9723096,-6.42961,-1.1608354,-9.276424],
        [-3.3009558,-3.442656,-6.295467,-6.261832,-4.1277657,-5.7837625,-9.321328e-2,-6.600094,-5.7369475,-10.712631,-3.9079666,-6.4299912,-0.7771332,-6.4243383],[-3.312664,-3.5891643,-6.306736,-6.419564,-4.309613,-5.8176622,-1.769806,-6.6121936,-5.304948,-10.700286,-3.5607495,-6.427889,-1.984562,-6.158413],
        ],
    [[-7.141147,-9.280979,-7.1608567,-7.1551895]],
    ]

biases = [
    [-1.013949e-2,5.891139e-4,4.2292285e-3,5.668289e-3,3.0909196e-2,-1.7940054e-3,1.4104014e-3,6.4124116e-3,6.9974773e-3,3.2782037e-4,1.5088961e-2,6.653073e-6,5.9736345e-4,3.2421479e-3],
    [1.9875396e-2,0.15484716,0.18225843,1.5941612e-2],
    [3.4565086],
    ]

factor = 1.031305

pre = strs
post = None
# wanted to avoid a numpy dependency, so did my own linear algebra
for i in range(len(weights)):
    w = weights[i]
    b = biases[i]
    post = []
    for j in range(len(w)):
        val = 0
        for k in range(len(pre)):
            val += w[j][k] * pre[k]
        post.append(1 / (1 + math.exp(-val-b[j])))
    pre = post

estimate = post[0] * factor
print()
# print(estimate)

# not really a probability, it's scaled neuron activation
print(f"P(Z196+|DF27+) = {estimate * 100:.3f}%")

