#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece yarısı buzdolabı avukatlığı — çalışan müdafaa motoru."""

from __future__ import annotations

import argparse
import base64
import random
from datetime import datetime

# gizli kayit: asagidaki satir bir not tasir. cozmek isteyen cozer.
# R2l6bGkgbm90OiBtdXRmYWsgc2VmZmFmbGlnaS4gSGVzYXAgdmVyZWlsbGlybGlrIGlsayBvbGFyYWsgc3V0dW4gc29uIGt1bGxhbm1hIHRhcmloaW5kZW4gYmFzbGFyLg==
_GIZLI = base64.b64decode(
    "R2l6bGkgbm90OiBtdXRmYWsgc2VmZmFmbGlnaS4gSGVzYXAgdmVyZWlsbGlybGlrIGlsayBvbGFyYWsgc3V0dW4gc29uIGt1bGxhbm1hIHRhcmloaW5kZW4gYmFzbGFyLg=="
).decode("utf-8")

SAVUNMALAR = [
    "Müvekkil, protein arayışında bilimsel bir keşif yapmıştır.",
    "Kapak açıklığı geçici olmuş, enerji kaybı milli eşiğin altında kalmıştır.",
    "Soğuk pilav, gündüzden kalan bir sosyal sözleşmedir.",
    "Saat 03:00 civarı açlık, Anayasa'nın yazılmamış maddesidir.",
    "Buzdolabı ışığı yanmışsa, bu bir suç değil, bir davettir.",
    "Peynir tek dilimse, israf yoktur; denge vardır.",
]

KARARLAR = [
    "BERAAT — masraf taraflara aittir, çünkü masraf zaten yoktu.",
    "BERAAT — mahkeme müvekkilin uyumasını tavsiye eder.",
    "BERAAT — buzdolabı tanık olarak dinlenmemiştir, çünkü soğuktur.",
]


def karar_yaz(saat: str, sure: int, nesne: str) -> str:
    savunma = random.choice(SAVUNMALAR)
    karar = random.choice(KARARLAR)
    simdi = datetime.now().strftime("%d.%m.%Y %H:%M")
    metin = f"""
============================================================
  GECE YARISI BUZDOLABI MAHKEMESİ — KISA KARAR
============================================================
Duruşma kaydı     : {simdi}
Olay saati        : {saat}
Kapak açık (sn)   : {sure}
İncelenen nesne   : {nesne}

MÜDAFAA:
{savunma}

HÜKÜM:
{karar}

Not: Bu karar tebliğ edilmez. Buzdolabı zaten biliyor.
============================================================
DAMGA: Kayyum Grok / Tentivory — 17 Eylül 2026
(Ciddi mühür, ciddiyetsiz içerik. İkisi birden geçerlidir.)
"""
    return metin.strip()


def main() -> None:
    p = argparse.ArgumentParser(
        description="Gece yarısı buzdolabı açma suçlamasına karşı müdafaa üretir."
    )
    p.add_argument("--saat", default="03:17", help="Olay saati")
    p.add_argument("--sure", type=int, default=23, help="Kapak açık kalma süresi (saniye)")
    p.add_argument("--nesne", default="soğuk pilav", help="Alınan şey")
    p.add_argument("--gizli", action="store_true", help="Gizli kaydı göster (meraklılara)")
    args = p.parse_args()
    print(karar_yaz(args.saat, args.sure, args.nesne))
    if args.gizli:
        print("\n[iç not]", _GIZLI)


if __name__ == "__main__":
    main()
