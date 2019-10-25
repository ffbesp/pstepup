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
    "karten-godrea" : {
        "banner_name" : "Karten/Godrea 24K",
        "banner_type" : "limited_time_seasonal",
        "duration" : { "start" : "2019-10-24" , "end" : "2019-11-06" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20191021KartenGodreaFeaturedBanner.jpg",
        "banner_json" : "karten-godrea.json",
        "banner_icon" : { "Karten" : "401007207", "Godrea" : "401008607" },
        "banner_img" : "karten-godrea.jpg"
    },
    "chocobofina" : {
        "banner_name" : "Chocobo Fina 21K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-10-17" , "end" : "2019-10-30" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20191015ChocoboFinaGacha.jpg",
        "banner_json" : "chocobofina.json",
        "banner_icon" : { "Chocobo Fina" : "100022207" },
        "banner_img" : "chocobofina.jpg"
    },
    "galuf" : {
        "banner_name" : "Galuf 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-10-11" , "end" : "2019-10-25" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20191008FFVFeaturedSummon.jpg",
        "banner_json" : "galuf.json",
        "banner_icon" : { "Warrior of Dawn Galuf" : "205001007" },
        "banner_img" : "galuf.jpg"
    },
    "krile" : {
        "banner_name" : "Krile 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-10-11" , "end" : "2019-10-25" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20191008FFVFeaturedSummon.jpg",
        "banner_json" : "krile.json",
        "banner_icon" : { "Warrior of Light Krile" : "205001307" },
        "banner_img" : "krile.jpg"
    },
    "exdeath" : {
        "banner_name" : "Exdeath 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-10-11" , "end" : "2019-10-25" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20191008FFVFeaturedSummon.jpg",
        "banner_json" : "exdeath.json",
        "banner_icon" : { "Dark Mage Exdeath" : "205000907" },
        "banner_img" : "exdeath.jpg"
    },
    "wrfirion-dkleon" : {
        "banner_name" : "WR Firion/DK Leon 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-10-04" , "end" : "2019-10-18" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20191001FFIICGFirionFeaturedSummon.jpg",
        "banner_json" : "wrfirion-dkleon.json",
        "banner_icon" : { "WR Firion" : "202001607", "DK Leon" : "202001707" },
        "banner_img" : "wrfirion-dkleon.jpg"
    },
    "mordegon" : {
        "banner_name" : "Mordegon 20K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-09-27" , "end" : "2019-10-11" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190924DQXISMordegonGreatDragonSummon.jpg",
        "banner_json" : "mordegon.json",
        "banner_icon" : { "Mordegon" : "337000507" },
        "banner_img" : "mordegon.jpg"
    },
    "sora-khloud-rerun" : {
        "banner_name" : "Sora/KHloud 20K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-09-23" , "end" : "2019-10-04" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190917FeaturedSummonSoraCloudKH.jpg",
        "banner_json" : "sora-khloud-rerun.json",
        "banner_icon" : { "Sora" : "335000107", "KHloud" : "335000207" },
        "banner_img" : "sora-khloud-rerun.jpg"
    },
    "riku-khsephiroth" : {
        "banner_name" : "Riku/KH Sephiroth 24K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-09-20" , "end" : "2019-10-04" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/KHGachRikuSephirothKH.jpg",
        "banner_json" : "riku-khsephiroth.json",
        "banner_icon" : { "Riku" : "335000407", "KH Sephiroth" : "335000307" },
        "banner_img" : "riku-khsephiroth.jpg"
    },
    "aikaty" : {
        "banner_name" : "AI Katy 10K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-09-19" , "end" : "2019-09-30" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190917KatyPerryFeaturedSummon.jpg",
        "banner_json" : "aikaty.json",
        "banner_icon" : { "A.I. Katy" : "401007407" },
        "banner_img" : "aikaty.jpg"
    },
    "sol" : {
        "banner_name" : "Sol 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-09-13" , "end" : "2019-09-27" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/FeaturedSummonSol.jpg",
        "banner_json" : "sol.json",
        "banner_icon" : { "Sol" : "100022307" },
        "banner_img" : "sol.jpg"
    },
    "bartz-lenna" : {
        "banner_name" : "Bartz/Lenna 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-08-30" , "end" : "2019-09-13" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190827FFVFeatureSummon3.jpg",
        "banner_json" : "bartz-lenna.json",
        "banner_icon" : { "Bartz" : "205001107", "Lenna" : "205001207" },
        "banner_img" : "bartz-lenna.jpg"
    },
    "kfina" : {
        "banner_name" : "Kimono Fina 20K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-08-26" , "end" : "2019-09-02" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/KimonoFinaFeatureSummon.jpg",
        "banner_json" : "kfina.json",
        "banner_icon" : { "Kimono Fina" : "100024307" },
        "banner_img" : "kfina.jpg"
    },
    "primrose-olberic" : {
        "banner_name" : "Primrose/Olberic 21K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-08-23" , "end" : "2019-09-06" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/FeaturedSummonOctopathTraveler.png",
        "banner_json" : "primrose-olberic.json",
        "banner_icon" : { "Primrose" : "334000107", "Olberic" : "334000207" },
        "banner_img" : "primrose-olberic.png"
    },
    "fid-cilka-rerun" : {
        "banner_name" : "Fid/Cilka 25K",
        "banner_type" : "existing_permanent_units",
        "duration" : { "start" : "2019-08-19" , "end" : "2019-08-30" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190813FitraFidGachaRerun.jpg",
        "banner_json" : "fid-cilka-rerun.json",
        "banner_icon" : { "Fid" : "100020505", "Cilka" : "100020905" },
        "banner_img" : "fid-cilka-rerun.jpg"
    },
    "kaito-tsukiko" : {
        "banner_name" : "Kaito/Tsukiko 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-08-16" , "end" : "2019-08-30" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/KaitoTsukikoGacha3.jpg",
        "banner_json" : "kaito-tsukiko.json",
        "banner_icon" : { "Kaito" : "401008507", "Tsukiko" : "401007107" },
        "banner_img" : "kaito-tsukiko.jpg"
    },
    "rlightning-nhope" : {
        "banner_name" : "R. Lightning/N. Hope 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-07-31" , "end" : "2019-08-16" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/CGLightningFeaturedSummon3.jpg",
        "banner_json" : "rlightning-nhope.json",
        "banner_icon" : { "Radiant Lightning" : "213001007", "Neverending Hope" : "213001107" },
        "banner_img" : "rlightning-nhope.jpg"
    },
    "rivera" : {
        "banner_name" : "Rivera 12K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-07-26" , "end" : "2019-08-09" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/gacha_NEWS_RiveraFeatureSummon_Compilation.jpg",
        "banner_json" : "rivera.json",
        "banner_icon" : { "Rivera" : "401007707" },
        "banner_img" : "rivera.jpg"
    },
    "elena" : {
        "banner_name" : "Elena 20K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-07-19" , "end" : "2019-08-02" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190716ElenaMorganaSummon4.jpg",
        "banner_json" : "elena.json",
        "banner_icon" : { "Elena" : "401008407" },
        "banner_img" : "elena.jpg"
    },
    "elena-morgana" : {
        "banner_name" : "Elena/Morgana 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-07-19" , "end" : "2019-08-02" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190716ElenaMorganaSummon4.jpg",
        "banner_json" : "elena-morgana.json",
        "banner_icon" : { "Elena" : "401008407", "Morgana" : "401007007" },
        "banner_img" : "elena-morgana.jpg"
    },
    "yuffie" : {
        "banner_name" : "Yuffie 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-07-12" , "end" : "2019-07-26" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190709ZackYuffieFeaturedSummon.jpg",
        "banner_json" : "yuffie.json",
        "banner_icon" : { "Yuffie" : "207000607" },
        "banner_img" : "yuffie.jpg"
    },
    "zack" : {
        "banner_name" : "Zack 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-07-12" , "end" : "2019-07-26" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190709ZackYuffieFeaturedSummon.jpg",
        "banner_json" : "zack.json",
        "banner_icon" : { "Zack" : "207001107" },
        "banner_img" : "zack.jpg"
    },
    "sscharlotte" : {
        "banner_name" : "SS Charlotte 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-07-05" , "end" : "2019-07-19" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/CharlotteFeaturedSummon.jpg",
        "banner_json" : "sscharlotte.json",
        "banner_icon" : { "SS Charlotte" : "100021707" },
        "banner_img" : "sscharlotte.jpg"
    },
    "kayaka-daileen" : {
        "banner_name" : "K. Ayaka/D. Aileen 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-06-28" , "end" : "2019-08-01" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190625KimonoAyakaFeaturedSummon.jpg",
        "banner_json" : "kayaka-daileen.json",
        "banner_icon" : { "Kimono Ayaka" : "100021907", "Dressy Aileen" : "100022007" },
        "banner_img" : "kayaka-daileen.jpg"
    },
    "randi-flammie" : {
        "banner_name" : "Randi/Flammie 21K",
        "banner_type" : "limited_time_collab",
        "duration" : { "start" : "2019-06-21" , "end" : "2019-07-05" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190618FlammieFeaturedSummon.jpg",
        "banner_json" : "randi-flammie.json",
        "banner_icon" : { "Randi" : "304000107", "Flammie" : "304000407" },
        "banner_img" : "randi-flammie.jpg"
    },
    "aerith-redxiii" : {
        "banner_name" : "Aerith/Red XIII 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-06-12" , "end" : "2019-06-28" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20191006FFVIIAerith.jpg",
        "banner_json" : "aerith-redxiii.json",
        "banner_icon" : { "Aerith" : "207000407", "Red XIII" : "207000507" },
        "banner_img" : "aerith-redxiii.jpg"
    },
    "regina" : {
        "banner_name" : "Regina 24K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-06-07" , "end" : "2019-06-21" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190604ReginaSummon.jpg",
        "banner_json" : "regina.json",
        "banner_icon" : { "Regina" : "100017507" },
        "banner_img" : "regina.jpg"
    },
    "fid-cilka" : {
        "banner_name" : "Fid/Cilka 25K",
        "banner_type" : "new_permanent_units",
        "duration" : { "start" : "2019-05-31" , "end" : "2019-06-14" },
        "news_image_link" : "https://lapis-prod-staticnews-gumi-sg.akamaized.net/prod//en/img/20190528FFBESummerFinaFeatureSummon.jpg",
        "banner_json" : "fid-cilka.json",
        "banner_icon" : { "Fid" : "100020505", "Cilka" : "100020905" },
        "banner_img" : "fid-cilka.jpg"
    },
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