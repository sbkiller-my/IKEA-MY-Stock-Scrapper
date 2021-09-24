import requests

barangIkea = ["70333977",
              "70376721",
              "50228326",
              "00217976",
              "80217977",
              "20428553",
              "00472957",
              "00488048",
              "70353606",
              "10353609",
              "70488035",
              "90494610",
              "40488008",
              "60350986",
              "70488059",
              "70353593",
              "20353623",
              "40488046",
              "60494621",
              "90488020",
              "90350999",
              "50451108",
              "70322304",
              "90165421",
              "60165615",
              "20469421",
              "40392845",
              "30392836",
              "20392865",
              "70301165",
              "10171826",
              "70425627",
              "70147758",
              "70480402",
              "10349453",
              "10509309",
              "10136512",
              "60182238",
              "50247749",
              "10335842",
              "10447279",
              "20176951",
              "80484584",
              "50484585",
              "10179436",
              "80179433",
              "30337388",
              "50357691",
              "90290359",
              "10472990",
              "60406337",
              "60454291",
              "00295441",
              "10514711",
              "90187753",
              "10389948",
              "00438746",
              "10395384",
              "10326178",
              "20358786",
              "80267707",
              "40301708",
              "60299219",
              "40326577",
              "50391906",
              "40450802",
              "10447217",
              "00355722",
              "90377654",
              "10447972",
              "90219179",
              "10449909",
              "70355747",
              "30282178",
              "20430589",
              "00186183",
              "70282181",
              "20217800",
              "80217798",
              "50316064",
              "00316066",
              "70316063",
              "60402018",
              "20402015",
              "00402021",
              "70316181",
              "10402006",
              "30213547",
              "10134018",
              "70134020",
              "10134023",
              "70178896",
              "50225592",
              "10453883",
              "50453881",
              "20464032",
              "40141673",
              "80464029",
              "10466282",
              "30466276",
              "90252574",
              "50277005",
              "90391909",
              "30483049",
              "30483054",
              "10320954",
              "30472809",
              "30472814",
              "40477910"
              ]

barangIkeas = ["79246377",
               "09246408",
               "49898416",
               ]

oos = []
headers = {"accept": "application/json;version=2",
           "sec-ch-ua": "\"Google Chrome\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"",
           "sec-ch-ua-mobile": "?0",
           "sec-ch-ua-platform": "\"Windows\"",
           "x-client-id": "b6c117e5-ae61-4ef5-b4cc-e0b1e37f0631"}

for x in barangIkea:
    title = requests.get('https://www.ikea.com/my/en/products/' + x[-3:] + '/' + x + '.json', headers=headers)
    qty = requests.get('https://api.ingka.ikea.com/cia/availabilities/ru/my?itemNos=' + x + '&expand=StoresList',
                       headers=headers)
    titleQ = title.json()['mainImage']['alt']
    qtyQ = qty.json()['availabilities'][2]['buyingOption']['cashCarry']['availability']['quantity']
    print("{} = {} tinggal".format(titleQ, qtyQ))

    if qtyQ == 0:
        oos.append(titleQ)


for x in barangIkeas:
    title = requests.get('https://www.ikea.com/my/en/products/' + x[-3:] + '/s' + x + '.json', headers=headers)
    qty = requests.get('https://api.ingka.ikea.com/cia/availabilities/ru/my?itemNos=' + x + '&expand=StoresList',
                       headers=headers)
    titleQ = title.json()['mainImage']['alt']
    qtyQ = qty.json()['availabilities'][2]['buyingOption']['cashCarry']['availability']['quantity']
    print("{} = {} tinggal".format(titleQ, qtyQ))

    if qtyQ == 0:
        oos.append(titleQ)

print("\nWarning out of stock:")
for x in oos:
    print(x)
