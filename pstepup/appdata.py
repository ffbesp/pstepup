pull_type = {
    "regular" : {
        "rainbowRate" : 0.03,
        "bannerRainbowRate" : 0.01,
        "offBannerRainbowRate" : 0.02
    },
    "guaranteedGold" : {
        "rainbowRate" : 0.05,
        "bannerRainbowRate" : 0.0375,
        "offBannerRainbowRate" : 0.0125
    },
    "guaranteedEXRainbow" : {
        "rainbowRate" : 1.0,
        "bannerRainbowRate" : None,
        "offBannerRainbowRate" : None
    },
    "guaranteedBannerRainbow" : {
        "rainbowRate" : 1.0,
        "bannerRainbowRate" : 1.0,
        "offBannerRainbowRate" : 0
    },
    "guaranteedRainbowWithRateUp" : {
        "rainbowRate" : 1.0,
        "bannerRainbowRate" : None,
        "offBannerRainbowRate" : None
    }
}

#only step-up banners; types = limited_time_collab, limited_time_seasonal, new_permanent_units, existing_permanent_units
banner_info = {
    "edgar-sabin" : {
        "banner_name" : "Edgar/Sabin 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-05-24" , "end" : "2019-06-07" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/gacha_NEWS_FigaroFeatureSummon_Compilation.jpg",
        "banner_json" : "edgar-sabin.json",
        "banner_icon" : { "Edgar" : "206001905", "Sabin" : "206002005" },
        "banner_img" : "edgar-sabin.jpg"
    },
    "nagi" : {
        "banner_name" : "Nagi 12K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-05-17" , "end" : "2019-05-31" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/NagiSummon2.jpg",
        "banner_json" : "nagi.json",
        "banner_icon" : { "Nagi" : "100019105" },
        "banner_img" : "nagi.jpg"
    },
    "yego" : {
        "banner_name" : "Yego 12K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-05-17" , "end" : "2019-05-31" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/NagiSummon2.jpg",
        "banner_json" : "yego.json",
        "banner_icon" : { "Yego" : "100019205" },
        "banner_img" : "yego.jpg"
    },
    "akstar" : {
        "banner_name" : "Akstar 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-05-10" , "end" : "2019-05-24" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/gacha_NEWS_AkstarFeatureSummon_Compilation.jpg",
        "banner_json" : "akstar.json",
        "banner_icon" : { "Akstar" : "100020005" },
        "banner_img" : "akstar.jpg"
    },
    "zeno-akstar" : {
        "banner_name" : "Zeno/Akstar 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-05-10" , "end" : "2019-05-24" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/gacha_NEWS_AkstarFeatureSummon_Compilation.jpg",
        "banner_json" : "zeno-akstar.json",
        "banner_icon" : { "Zeno" : "401007605", "Akstar" : "100020005" },
        "banner_img" : "zeno-akstar.jpg"
    },
    "bmgolbez" : {
        "banner_name" : "BM Golbez 10K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-05-03" , "end" : "2019-05-17" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/DarkMageGolbezGacha.jpg",
        "banner_json" : "bmgolbez.json",
        "banner_icon" : { "BM Golbez" : "204001705" },
        "banner_img" : "bmgolbez.jpg"
    },
    "citan-maria" : {
        "banner_name" : "Citan/Maria 22K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-04-26" , "end" : "2019-05-10" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190423Xenogears2Collaboration.jpg",
        "banner_json" : "citan-maria.json",
        "banner_icon" : { "Citan" : "331000705", "Maria" : "331000805" },
        "banner_img" : "citan-maria.jpg"
    },
    "fei-elly-bart-rerun" : {
        "banner_name" : "Fei/Elly/Bart 22K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-04-26" , "end" : "2019-05-10" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190423Xenogears2Collaboration.jpg",
        "banner_json" : "fei-elly-bart-rerun.json",
        "banner_icon" : { "Fei" : "331000105", "Elly" : "331000205", "Bart" : "331000405" },
        "banner_img" : "fei-elly-bart.jpg"
    },
    "esther-sylvie" : {
        "banner_name" : "Esther/Sylvie 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-04-19" , "end" : "2019-05-03" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/2019EasterGacha.jpg",
        "banner_json" : "esther-sylvie.json",
        "banner_icon" : { "Esther" : "401006805", "Sylvie" : "401006905" },
        "banner_img" : "esther-sylvie.jpg"
    },
    "crimson" : {
        "banner_name" : "Crimson 12K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-04-12" , "end" : "2019-04-26" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/FFBECrimsonFeatureSummon.jpg",
        "banner_json" : "crimson.json",
        "banner_icon" : { "Crimson" : "100020605" },
        "banner_img" : "crimson.jpg"
    },
    "ultima-beowulf" : {
        "banner_name" : "Ultima/Beowulf 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-04-05" , "end" : "2019-04-19" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/FF3TWOTLUltimaGacha3.jpg",
        "banner_json" : "ultima-beowulf.json",
        "banner_icon" : { "Ultima" : "253001305", "Beowulf" : "253001005" },
        "banner_img" : "ultima-beowulf.jpg"
    },
    "fei-elly-bart" : {
        "banner_name" : "Fei/Elly/Bart 22K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-03-29" , "end" : "2019-04-12" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190328XenogearsGachaBanner.jpg",
        "banner_json" : "fei-elly-bart.json",
        "banner_icon" : { "Fei" : "331000105", "Elly" : "331000205", "Bart" : "331000405" },
        "banner_img" : "fei-elly-bart.jpg"
    },
    "karlette" : {
        "banner_name" : "Karlette 12K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-03-22" , "end" : "2019-03-29" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/gacha_NEWS_Yuraisha_Compilation.jpg",
        "banner_json" : "karlette.json",
        "banner_icon" : { "Karlette" : "100019905" },
        "banner_img" : "karlette.jpg"
    },
    "yuraisha" : {
        "banner_name" : "Yuraisha 12K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-03-22" , "end" : "2019-03-29" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/gacha_NEWS_Yuraisha_Compilation.jpg",
        "banner_json" : "yuraisha.json",
        "banner_icon" : { "Yuraisha" : "100017605" },
        "banner_img" : "yuraisha.jpg"
    },
    "cid" : {
        "banner_name" : "Cid 12K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-03-15" , "end" : "2019-03-29" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/CidGacha.jpg",
        "banner_json" : "cid.json",
        "banner_icon" : { "Cid" : "100019505" },
        "banner_img" : "cid.jpg"
    },
    "okrefia-dkluneth" : {
        "banner_name" : "OK Refia/DK Luneth 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-03-08" , "end" : "2019-03-22" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/FF3Gacha.jpg",
        "banner_json" : "okrefia-dkluneth.json",
        "banner_icon" : { "OK Refia" : "203001305", "DK Luneth" : "203001405" },
        "banner_img" : "okrefia-dkluneth.jpg"
    },
    "myra-afry" : {
        "banner_name" : "Myra/A. Fryevia 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-02-22" , "end" : "2019-03-07" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/FanFestaMyraGachaSummonv2.jpg",
        "banner_json" : "myra-afry.json",
        "banner_icon" : { "Myra" : "401004505", "Aurora Fryevia" : "401006405" },
        "banner_img" : "myra-afry.jpg"
    },
    "ignacio" : {
        "banner_name" : "Ignacio 11K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-02-15" , "end" : "2019-02-28" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/gacha_NEWS_FFBEIgnacio.jpg",
        "banner_json" : "ignacio.json",
        "banner_icon" : { "Ignacio" : "100018705" },
        "banner_img" : "ignacio.jpg"
    },
    "qin-bhzq" : {
        "banner_name" : "CNY Qin/BHZQ 20K",
        "banner_type" : "limited_time_seasonal",
        "duration" : { "start" : "2019-02-08" , "end" : "2019-02-21" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190208CNYNewUnitsGachaBanner.jpg",
        "banner_json" : "qin-bhzq.json",
        "banner_icon" : { "Qin" : "401006605", "BHZQ" : "401006705" },
        "banner_img" : "qin-bhzq.jpg"
    },
    "jecht-auron" : {
        "banner_name" : "Jecht/Auron 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-02-01" , "end" : "2019-02-14" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190131FFXGachaBanner.jpg",
        "banner_json" : "jecht-auron.json",
        "banner_icon" : { "Jecht" : "210001005", "Auron" : "210000605" },
        "banner_img" : "jecht-auron.jpg"
    },
    "sophia-rena" : {
        "banner_name" : "SOA Sophia/Rena 20K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-01-25" , "end" : "2019-02-07" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190123SOAGachaBanner4.jpg",
        "banner_json" : "sophia-rena.json",
        "banner_icon" : { "Sophia" : "401006505", "Rena" : "317000105" },
        "banner_img" : "sophia-rena.jpg"
    },
    "sophia-fayt" : {
        "banner_name" : "SOA Sophia/Fayt 20K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-01-25" , "end" : "2019-02-07" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190123SOAGachaBanner4.jpg",
        "banner_json" : "sophia-fayt.json",
        "banner_icon" : { "Sophia" : "401006505", "Fayt" : "318000105" },
        "banner_img" : "sophia-fayt.jpg"
    },
    "folka" : {
        "banner_name" : "Folka 11K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-01-18" , "end" : "2019-01-31" },
        "news_image_link" : "https://i.imgur.com/W7aHWGO.jpg",
        "banner_json" : "folka.json",
        "banner_icon" : { "Folka" : "100018305" },
        "banner_img" : "folka.jpg"
    },
    "tifa-vincent" : {
        "banner_name" : "Tifa/Vincent 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-01-11" , "end" : "2019-01-24" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190109TifaVincentSummonBanner.jpg",
        "banner_json" : "tifa-vincent.json",
        "banner_icon" : { "Tifa" : "207000305", "Vincent" : "207000805" },
        "banner_img" : "tifa-vincent.jpg"
    },
    "kingdom-hearts" : {
        "banner_name" : "KH Sora/Khloud 24K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2018-12-28" , "end" : "2019-01-10" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20181227KHFeaturedSummon3.jpg",
        "banner_json" : "kingdom-hearts.json",
        "banner_icon" : { "Sora" : "335000105", "Cloud (KH)" : "335000205" },
        "banner_img" : "kingdom-hearts.jpg"
    },
    "tiana-felix" : {
        "banner_name" : "Xmas Tiana/Felix 20K",
        "banner_type" : "limited_time_seasonal",
        "duration" : { "start" : "2018-12-21" , "end" : "2019-01-03" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20181219ChristmasNewUnitGacha.jpg",
        "banner_json" : "tiana-felix.json",
        "banner_icon" : { "Tiana" : "401006205", "Felix" : "401006105" },
        "banner_img" : "tiana-felix.jpg"
    },
    "sieghard" : {
        "banner_name" : "Sieghard 11K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-12-07" , "end" : "2018-12-20" },
        "news_image_link" : "https://i.imgur.com/k2HWBlt.jpg",
        "banner_json" : "sieghard.json",
        "banner_icon" : { "Sieghard" : "100017905" },
        "banner_img" : "sieghard.jpg"
    },
    "nier-a2-2b" : {
        "banner_name" : "Nier A2/2B 20K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2018-11-23" , "end" : "2018-12-06" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20181120NierAutomataGachaBanner.jpg",
        "banner_json" : "nier-a2-2b.json",
        "banner_icon" : { "A2" : "401001205", "2B" : "310000105" },
        "banner_img" : "nier-a2-2b.jpg"
    },
    "beryl-ellesperis" : {
        "banner_name" : "Beryl/Ellesperis 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-11-16" , "end" : "2018-11-29" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20181113FanFestaBerylEllesperisGacha.jpg",
        "banner_json" : "beryl-ellesperis.json",
        "banner_icon" : { "Beryl" : "401004805", "Ellesperis" : "401004705" },
        "banner_img" : "beryl-ellesperis.jpg"
    },
    "kurasame" : {
        "banner_name" : "Kurasame 11K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-11-02" , "end" : "2018-11-15" },
        "news_image_link" : "https://i.imgur.com/wr5KHLo.jpg",
        "banner_json" : "kurasame.json",
        "banner_icon" : { "Kurasame" : "254001905" },
        "banner_img" : "kurasame.jpg"
    }, 
    "machina" : {
        "banner_name" : "Machina 11K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-11-02" , "end" : "2018-11-15" },
        "news_image_link" : "https://i.imgur.com/wr5KHLo.jpg",
        "banner_json" : "machina.json",
        "banner_icon" : { "Machina" : "254001805" },
        "banner_img" : "machina.jpg"
    },
    "valkyrie-profile" : {
        "banner_name" : "VP Lenneth/Freya/Arngrim 25K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2018-10-26" , "end" : "2018-11-08" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/ValkyrieProfileFeatureSummon.jpg",
        "banner_json" : "valkyrie-profile.json",
        "banner_icon" : { "Lenneth" : "330000105", "Freya" : "330000205", "Arngrim" : "330000305" },
        "banner_img" : "valkyrie-profile.jpg"
    },
    "lenneth" : {
        "banner_name" : "Lenneth 11K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2018-10-26" , "end" : "2018-10-29" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/ValkyrieProfileFeatureSummon.jpg",
        "banner_json" : "lenneth.json",
        "banner_icon" : { "Lenneth" : "330000105" },
        "banner_img" : "lenneth.jpg"
    },
    "freya" : {
        "banner_name" : "Freya 11K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2018-10-28" , "end" : "2018-10-31" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/ValkyrieProfileFeatureSummon.jpg",
        "banner_json" : "freya.json",
        "banner_icon" : { "Freya" : "330000205" },
        "banner_img" : "freya.jpg"
    },
    "arngrim" : {
        "banner_name" : "Arngrim 11K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2018-10-30" , "end" : "2018-11-02" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/ValkyrieProfileFeatureSummon.jpg",
        "banner_json" : "arngrim.json",
        "banner_icon" : { "Arngrim" : "330000305" },
        "banner_img" : "arngrim.jpg"
    },
    "lilith-lucius" : {
        "banner_name" : "Lilith/Lucius 20K",
        "banner_type" : "limited_time_seasonal",
        "duration" : { "start" : "2018-10-19" , "end" : "2018-11-04" },
        "news_image_link" : "https://i.imgur.com/n1Szqvb.jpg",
        "banner_json" : "lilith-lucius.json",
        "banner_icon" : { "Lilith" : "401005905", "Lucius" : "401006005" },
        "banner_img" : "lilith-lucius.jpg"
    },
    "citra" : {
        "banner_name" : "Citra 11K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-10-12" , "end" : "2018-10-26" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/gacha_NEWS_Citra_Compilation.jpg",
        "banner_json" : "citra.json",
        "banner_icon" : { "Citra" : "100016905" },
        "banner_img" : "citra.jpg"
    },
    "malphasie-circe" : {
        "banner_name" : "Malphasie/Circe 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-09-28" , "end" : "2018-10-12" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/gacha_20180927Fanfesta_Compilation1.jpg",
        "banner_json" : "malphasie-circe.json",
        "banner_icon" : { "Malphasie" : "401004605", "Circe" : "401004405" },
        "banner_img" : "malphasie-circe.jpg"
    },
    "hyoh" : {
        "banner_name" : "Hyoh 11K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-09-14" , "end" : "2018-09-28" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/HyohFeatureSummon.jpg",
        "banner_json" : "hyoh.json",
        "banner_icon" : { "Hyoh" : "100016205" },
        "banner_img" : "hyoh.jpg"
    },
    "hyoh-arain" : {
        "banner_name" : "Hyoh/A. Rain 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-09-14" , "end" : "2018-09-28" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/HyohStepUp.jpg",
        "banner_json" : "hyoh-arain.json",
        "banner_icon" : { "Hyoh" : "100016205", "Awakened Rain" : "100015805" },
        "banner_img" : "hyoh-arain.jpg"
    },
    "deus-ex" : {
        "banner_name" : "DX Adam Jensen/Viktor 20K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2018-08-24" , "end" : "2018-09-06" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20180821DeuxEXCompilation.jpg",
        "banner_json" : "deus-ex.json",
        "banner_icon" : { "Adam Jensen" : "401004905", "Viktor Marchenko" : "401005005" },
        "banner_img" : "deus-ex.jpg"
    },
    "squall-rinoa" : {
        "banner_name" : "Squall/Rinoa 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-08-03" , "end" : "2018-08-17" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20180801Squall2.jpg",
        "banner_json" : "squall-rinoa.json",
        "banner_icon" : { "Squall" : "208000105", "Rinoa" : "208000205" },
        "banner_img" : "squall-rinoa.jpg"
    },
    "raegen" : {
        "banner_name" : "Raegen 11K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-07-13" , "end" : "2018-07-27" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/content/20180712StepUp7.html",
        "banner_json" : "raegen.json",
        "banner_icon" : { "Raegen" : "100010005" },
        "banner_img" : "raegen.png"
    },
    "sephiroth-lila" : {
        "banner_name" : "Sephiroth/Lila 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2018-05-11" , "end" : "2018-05-25" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/content/20180508StepUp4.html",
        "banner_json" : "sephiroth-lila.json",
        "banner_icon" : { "Sephiroth" : "207001005", "Lila" : "100013805" },
        "banner_img" : "sephiroth-lila.png"
    }
}