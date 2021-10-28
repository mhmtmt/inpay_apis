import requests

import xml.etree.ElementTree as ET
from urllib.request import urlopen
import datetime


class DovizKurlari():

    def __init__(self):
        pass

    def __veri_update(self, zaman="Bugun"):
        try:

            if zaman == "Bugun":
                self.url = "http://www.tcmb.gov.tr/kurlar/today.xml"
            else:
                self.url = zaman

            tree = ET.parse(urlopen(self.url))

            root = tree.getroot()
            self.son = {}
            self.Kur_Liste = []
            i = 0
            for kurlars in root.findall('Currency'):
                Kod = kurlars.get('Kod')
                Unit = kurlars.find('Unit').text
                isim = kurlars.find('Isim').text
                CurrencyName = kurlars.find('CurrencyName').text
                ForexBuying = kurlars.find('ForexBuying').text
                ForexSelling = kurlars.find('ForexSelling').text
                BanknoteBuying = kurlars.find('BanknoteBuying').text
                BanknoteSelling = kurlars.find('BanknoteSelling').text
                CrossRateUSD = kurlars.find('CrossRateUSD').text
                self.Kur_Liste.append(Kod)

                self.son[Kod] = {
                    "Kod": Kod,
                    "isim": isim,
                    "CurrencyName": CurrencyName,
                    "Unit": Unit,
                    "ForexBuying": ForexBuying,
                    "ForexSelling": ForexSelling,
                    "BanknoteBuying": BanknoteBuying,
                    "BanknoteSelling": BanknoteSelling,
                    "CrossRateUSD": CrossRateUSD
                }

            return self.son

        except:

            return "HATA"

    def DegerSor(self, *sor):
        self.__veri_update()
        if not (any(sor)):
            return self.son
        else:
            return self.son.get(sor[0]).get(sor[1])

    def Arsiv(self, Gun, Ay, Yil, *sor):
        a = self.__veri_update(self.__Url_Yap(Gun, Ay, Yil))
        if not (any(sor)):
            if a == "HATA":
                return {"Hata": "TATIL GUNU"}
            return self.son
        else:
            if a == "HATA":
                return "Tatil Gunu"
            else:
                return self.son.get(sor[0]).get(sor[1])

    def Arsiv_tarih(self, Tarih="", *sor):
        takvim = Tarih.split(".")
        Gun = takvim[0]
        Ay = takvim[1]
        Yil = takvim[2]
        a = self.__veri_update(self.__Url_Yap(Gun, Ay, Yil))
        if not (any(sor)):
            if a == "HATA":
                return {"Hata": "TATIL GUNU"}
            return self.son
        else:
            if a == "HATA":
                return "Tatil Gunu"
            else:
                return self.son.get(sor[0]).get(sor[1])

    def __Url_Yap(self, Gun, Ay, Yil):
        if len(str(Gun)) == 1:
            Gun = "0" + str(Gun)
        if len(str(Ay)) == 1:
            Ay = "0" + str(Ay)

        self.url = ("http://www.tcmb.gov.tr/kurlar/" + str(Yil) + str(Ay) + "/" + str(Gun) + str(Ay) + str(
            Yil) + ".xml")
        return self.url


def finalDolar():
    dolar_inst = DovizKurlari()
    dolar = dolar_inst.DegerSor("USD", "ForexBuying")
    return float(dolar)


def get_price():
    response = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=LTCUSDT')
    data = response.json()

    return float(data["price"]) * finalDolar()


class Charge:
    def __init__(self, sc_key, receiving_wallet):
        self.sc_key = sc_key
        self.receiving_wallet = receiving_wallet

    def charge(self, amount):
        r = requests.post("http://172.105.248.143/api/charge", data={"wallet_sc_key": self.sc_key,
                                                                     "receiving_wallet": self.receiving_wallet,
                                                                     "amount": amount / get_price()})
        if r.text == "Ödeme Onaylandı":
            return {"status": True, "reason_of_failure": "Success", "litecoin_amount": str(amount / get_price())}
        elif not r.ok:
            return {"status": False, "reason_of_failure": "Yetersiz cüzdan bakiyesi",
                    "litecoin_amount": str(amount / get_price())}
        else:
            return {"status": False, "reason_of_failure": r.text, "litecoin_amount": str(amount / get_price())}

    def installmentCharge(self, amount, installment_amount, total_months):
        r = requests.post("http://172.105.248.143/api/createInstallmentCharge",
                          data={"wallet_sc_key": self.sc_key,
                                "receiving_wallet": self.receiving_wallet,
                                "amount": amount / get_price(),
                                "installment_amount": installment_amount,
                                "total_months": total_months,
                                "day_of_month": datetime.datetime.today().day
                                })

        if r.text == "Ödeme Onaylandı":
            return {"status": True, "reason_of_failure": "Success", "litecoin_amount": str(amount / get_price())}
        elif not r.ok:
            return {"status": False, "reason_of_failure": "Yetersiz cüzdan bakiyesi",
                    "litecoin_amount": str(amount / get_price())}
        else:
            return {"status": False, "reason_of_failure": r.text, "litecoin_amount": str(amount / get_price())}
